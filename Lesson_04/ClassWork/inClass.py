# list_my = [(i,i**2) for i in range(5) if not i%2]
#
# print(list_my)

# with open('test.txt', 'r') as f:
#     temp = f.read()
#
# res = [(i, i**2) for i in map(lambda x:int(x),temp.split()) if i%2==0]
#
from math import factorial
from random import random

numbers = list(map(lambda i: not i%2, (random.randint(1,100) for i in range(5))))

print(numbers)

numbers = [1,2,3]

arr = list(map(factorial,numbers))


# # list_arr = list(map(int,temp.split()))
# # print(list_arr)
# print(res)


