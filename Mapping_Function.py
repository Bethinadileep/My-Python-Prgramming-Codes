
def fun(mystr):
    return len(mystr)
list1 = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
result = list(map(fun,list1))
print(result)

