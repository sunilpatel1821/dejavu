from dejavu import decoder, fingerprint
from operator import itemgetter

file1 = '/Users/patels/Documents/Audio_fingerprint/test_friends/friends_audio/season2/e11.wav'
file2 = '/Users/patels/Documents/Audio_fingerprint/test_friends/friends_audio/season2/e12.wav'


def get_maxima(file):
    channels, frame_rate, hash_ = decoder.read(file, 100)
    local_maxima = fingerprint.fingerprint(channels[0])
    local_maxima.sort(key=itemgetter(1))
    return local_maxima


maxima1 = get_maxima(file1)
maxima2 = get_maxima(file2)


