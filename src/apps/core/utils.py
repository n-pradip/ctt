import string
from random import choice


def CodeGenerator():
    chars = string.digits
    random_code = ''.join(choice(chars) for _ in range(4))
    return random_code
