# ROT13 is a simple letter substitution cipher that replaces a letter \
#   with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. \
#   If there are numbers or special characters included in the string, \
#   they should be returned as they are. Only letters from the latin/english alphabet should be shifted,\
#   like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.
# BTW: you can try rot7/rot20 as you well. Think about how to build a method in rot(2~25)

import string
from string import ascii_lowercase as lc, ascii_uppercase as uc


def rot13(message: str):
    letters = string.ascii_letters
    contrasts = string.ascii_lowercase[13:]+string.ascii_lowercase[:13]+\
        string.ascii_uppercase[13:]+string.ascii_uppercase[:13]
    return message.translate(str.maketrans(letters,contrasts))


# best solution for shortened the method at string.ascii_lowercase
def rot13_1(message):
    return message.translate(str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))


print(rot13('hello world'))
print(rot13_1('hello world'))