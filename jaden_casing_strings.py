# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) \
#   and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. \
#   When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, \
#   you'll have to capitalize each word, check out how contractions are expected to be in the example below.
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes \
#   from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(not_jaden):
    temp = not_jaden.split(' ')
    style_jaden = ''
    for i in temp:
        style_jaden += i.capitalize() + ' '
    return style_jaden.rstrip()


# best resolution
from string import capwords


def to_jaden_case_1(not_jaden):
    return capwords(not_jaden)


not_jaden_case = "How can mirrors be real if our eyes aren't real"
jaden_case = to_jaden_case(not_jaden_case)
print(jaden_case)

print(to_jaden_case_1(not_jaden_case))
