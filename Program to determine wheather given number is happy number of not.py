def isHappyNumber(num):
  sum=rem=0

  while(num>0):
    rem = num%10
    sum = sum + (rem*rem)
    num = num // 10

  return sum

result = 7
while(result!=1 and result !=4):
  result = isHappyNumber(result)

if(result == 1):
  print("Happy Number")
elif(result == 4):
  print("UnHappy Number")
