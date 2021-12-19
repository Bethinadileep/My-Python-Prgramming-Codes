#codeby : Dileep

num = int(input())
sum = 0
for i in range(1,num-1):
  rem = num % i
  if(rem == 0):
    sum = sum + i
  
if(sum == num):
  print("Perfect Number")
else:
  print("Not Perfect Number")
