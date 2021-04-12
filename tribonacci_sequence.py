# you need to create a fibonacci function that given a signature array/list, \
#   returns the first n elements - signature included of the so seeded sequence.
#
# Signature will always contain 3 numbers; n will always be a non-negative number; \
#   if n == 0, then return an empty array (except in C return NULL) and be ready for \
#   anything else which is not clearly specified ;)

def tribonacci(signature, n):
    print('signaure is:{},n is:{}'.format(signature,n))
    if n < 3:
        return signature[0:n]
    for i in range(0,n-3):
        signature.append(sum(signature[i:i+3]))
        print(signature)
    return signature

print(tribonacci([1,1,1],5))
print(tribonacci([300, 200, 100], 1))