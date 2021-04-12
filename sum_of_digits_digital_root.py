# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit,\
#   continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# solution by STR
def digital_root(n):
    n_list = list(str(n))
    if n_list.__len__() == 1:
        return n
    else:
        resut = 0
        for i in n_list:
            resut += int(i)
        return digital_root(resut)


# solution by 迭代器
def digital_root_1(n):
    return n if n<10 else digital_root_1(sum(map(int, str(n))))
    # if n < 10:
    #     return n
    # else:
    #     digital_root_1(sum(map(int, str(n))))

# solution by MATH
def digital_root_2(n):
    return n%9 or n and 9

n = 493193
print(digital_root(n))
print(digital_root_1(n))
print(digital_root_2(n))
