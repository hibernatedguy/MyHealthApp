import string
import random

KEY_LEN = 3


def base_str():
    return (string.hexdigits)


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))
