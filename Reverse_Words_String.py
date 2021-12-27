#codeby : Dileep

#Reversing String Words
def reverseWords(words):
    words1=""
    for i in range(4,-1,-1):
        words1+= words[i]
    return words1
    
val = "I am a Python Programmer"
val1 = val.split()
val2 = list(reverseWords(val1))
print(" ".join(val2))

#Reversing String in Python
str = "Dileep"
str1 = ""
for i in range(5,-1,-1):
    str1 += str[i]
print(str1)
