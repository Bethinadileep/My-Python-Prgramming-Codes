
#Lambda Function is Assigning Reference Variable
mysqaur = lambda num : num * num
print(mysqaur(12))
print(type(mysqaur))

myaddition = lambda num1,num2 : num1 + num2
print(myaddition(124,356))

myFactorial = lambda num : 1 if (num==0 or num==1) else num * myFactorial(num-1)
print(myFactorial(4))

