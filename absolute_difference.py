n = int(input())
li = [1,2,3]
li.sort()
v = 0
for i in range(1,n):
    v += abs(li[i] - li[i-1])
print(v)
