# You are given an array (which will have a length of at least 3, but could be very large) \
#   containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# # Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    integers_mod = [i%2 for i in integers]
    if integers_mod.count(0) == 1:
        return integers[integers_mod.index(0)]
    elif integers_mod.count(1) == 1:
        return integers[integers_mod.index(1)]
    return None
list = [161, 3, 1719, 19, 11, 13, -21]
print(find_outlier(list))