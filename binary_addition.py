# Implement a function that adds two numbers together and returns their sum in binary. \
#   The conversion can be done before, or after the addition.#
# The binary number returned should be a string.

def add_binary(a, b):
    return format(a + b, 'b')


a, b = 10, 6
print(add_binary(a,b))
