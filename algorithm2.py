#斐波那契数列 实现方式 （1）递归 （2）矩阵

def item(num):
    if num == 0:
        res = 0
    elif num == 1:
        res = 1
    else:
        res = item ( num - 1) + item (num -2)
    return res
a =item(6)
print a


import copy
def linearComputer(n):
    if n<=2:
        return 1
    current2A = [1,1]
    prev2A =copy.deepcopy(current2A)
    for ind in range(n-1):
        current2A[0] = 0*prev2A[0]+1*prev2A[1]
        current2A[1] = 1*prev2A[0]+1*prev2A[1]
        prev2A = copy.deepcopy(current2A)
        print prev2A
    return prev2A[1]
    
a = linearComputer(10)
print a 