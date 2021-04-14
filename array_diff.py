# Your goal in this kata is to implement a difference function, \
#   which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a: list, b: list):
    if len(a) == 0 or len(b) == 0:
        return a
    else:
        for i in b:
            if a.count(i) != 0:
                n = 0
                while n <= a.count(i):
                    a.remove(i)
                    n += 1
        return a

def array_diff_1(a: list, b: list):
    # if len(a)*len(b) == 0:
    #     return a
    return [i for i in a if b.count(i) == 0]


print(array_diff_1([1,2], [1]))
print(array_diff_1([1,2,2], [1]))
print(array_diff_1([1,2,2], [2]))
print(array_diff_1([1,2,2], []))
print(array_diff_1([], [1,2]))
print(array_diff_1([1,2,3], [1, 2]))