# Complete the method/function so that it converts dash/underscore delimited words into camel casing. \
#   The first word within the output should be capitalized only if the original word was capitalized \
#   (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text: str):
    text_list = text.replace('_', '-').split('-')
    # text_list = text.split('-')
    text_result: str = text_list[0]
    for i in range(1, len(text_list)):
        text_result += text_list[i].capitalize()
    return text_result


def to_camel_case_1(text: str):
    return text[0] + text.title()[1:].replace('-','').replace('_','') if text != '' else text


print(to_camel_case('hello-world-to-you'))
print(to_camel_case('hello_world_to_you'))
print(to_camel_case('helloworld'))
print(to_camel_case(''))
print(to_camel_case('   '))

print(to_camel_case_1('hello-world-to-you'))
print(to_camel_case_1('hello_world_to_you'))
print(to_camel_case_1('helloworld'))
print(to_camel_case_1(''))
print(to_camel_case_1('   '))