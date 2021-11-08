#In Recursive Method
def fun_no1(num):
    if(num==0 or num==1): #Base Case
        return num
    return num * fun_no1(num-1) #Recursive Case
print(fun_no1(6))
