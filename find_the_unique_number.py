# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique

from heapq import heapify, heappop


def find_uniq(arr: list):
    print(arr)
    heapify(arr)
    temp = [heappop(arr), heappop(arr)]
    print(temp)
    if temp[0] == temp[1]:
        return max(arr)
    else:
        return min(temp)


def find_uniq_1(arr: list):
    a,b = set(arr)
    return a if arr.count(a) == 1 else b

print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))
print(find_uniq([7, 7, 7, 7, 7, 7, 6, 7]))

print(find_uniq_1([1, 1, 1, 2, 1, 1]))
print(find_uniq_1([0, 0, 0.55, 0, 0]))
print(find_uniq_1([3, 10, 3, 3, 3]))
print(find_uniq_1([7, 7, 7, 7, 7, 7, 6, 7]))
