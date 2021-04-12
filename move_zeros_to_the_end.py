# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    for i in range(array.count(0)):
        array.remove(0)
        array.append(0)
    return array

# sorted method
def move_zeros_1(array):
    # function lambda It returns True if 'x==0 and type(x) is not bool'
    return sorted(array, key= lambda x: x==0 and type(x) is not bool)

print(move_zeros([2,0,0,3,2,1,0,8,0]))
print(move_zeros([1,2,3,4]))
print(move_zeros_1([0,1,2,0,4,50,0,5,4]))