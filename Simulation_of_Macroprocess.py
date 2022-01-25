#codeby : Dileep

import re
values = open('input3.txt','r').read()
lines = values.splitlines()
function_name = []
function_body = []
for line in lines:
 if "#define" in line:
 line = line.split(' ')
 fun_name=line[1][:line[1].find('(')]
 function_name.append(fun_name)
 function_body.append(line[2])
d=dict(zip(function_name,function_body))
for line in lines:
 if "#define" not in line:
 for name in function_name:
 if name in line:
 line =
line.replace(name,"").replace('(',"").replace(')',"")
 line = line.replace(';',"")
 line = 
d[name].replace('X',line[0])+";"
 line =
line.replace('(',"").replace(')',"")
 print(line)
