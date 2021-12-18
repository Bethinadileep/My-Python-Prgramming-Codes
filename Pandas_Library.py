#codeby : Dileep

import pandas as pd

mydataset = {'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

age = {"one": 46,"two": 45,"three": 47}
print(pd.Series(age,index=["one","two"]))

a = [1,7,2]
myvar = pd.Series(a,index=["x","y","z"])
print(myvar)
print(myvar["y"])

print(pd.__version__)

import pandas as pd

collection = {
    "colories" : [10,20,30],
    "duration" : [50,40,45]
}
ans = pd.DataFrame(collection, index=["day1","day2","day3"])
print(ans)

print(ans.iloc[2])
print(ans.loc["day2"])
