#code by: Dileep
first,second=0,1
n=int(input("Please Give a Number for Fibanacci Series:"))
print("Fibanacci Series are:")
for i in range(0,n):
  if(i<=1):
    result=i
  else:
    result=first+second
    first=second
    second=result
  print(result)
