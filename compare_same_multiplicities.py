# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks \
#   whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
#
# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, \
#   20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. \
#   It gets obvious if we write b's elements in terms of squares:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# Invalid arrays
# If, for example, we change the first number to something else, comp may not return true anymore:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 132 is not the square of any number of a.
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 36100 is not the square of any number of a.
#
# Remarks
# a or b might be [] or {} (all languages except R, Shell).
# a or b might be nil or null or None or nothing \
#   (except in C++, Elixir, Haskell, PureScript, Pascal, R, Rust, Shell).
# If a or b are nil (or null or None, depending on the language), \
#   the problem doesn't make sense so return false.
#
# Note for C
# The two arrays have the same size (> 0) given as parameter in function comp.

def comp(a: list, b: list):
    if a is None or b is None or len(a) != len(b):
        return False
    else:
        a_temp = [x ** 2 for x in a]
        a_temp.sort()
        b.sort()
        for i in range(len(a)):
            if b[i] != a_temp[i]:
                return False
        return True


# best solution
def comp_1(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x*x for x in a1) == sorted(a2)


# used try
def comp_2(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


print(comp([-121, -144, 19, -161, 19, -144, 19, -11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
