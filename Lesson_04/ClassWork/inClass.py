# list_my = [(i,i**2) for i in range(5) if not i%2]
#
# print(list_my)

with open('test.txt', 'r') as f:
    temp = f.read()

res = [(i, i**2) for i in map(lambda x:int(x),temp.split()) if i%2==0]

# list_arr = list(map(int,temp.split()))
# print(list_arr)
print(res)