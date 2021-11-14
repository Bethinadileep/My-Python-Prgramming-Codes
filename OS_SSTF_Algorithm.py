#codeby : Dileep
#Write a Python program to simulate the SSTF program disk scheduling algorithms.
num=int(input("Enter the Number:"))
print("Enter the Queue:")
requestqueue=list(map(int,input().split()))
head_value=int(input("Head Value Starts at: "))
final=[]
for i in requestqueue:
    emptylist=[]
    for j in requestqueue:
        if(j!=None and head_value!=None):
            emptylist.append(abs(head_value-j))
        else:
            emptylist.append(float('inf'))
    final.append(min(emptylist))
    head_value=requestqueue[emptylist.index(min(emptylist))]
    requestqueue[requestqueue.index(head_value)]=None
print("Head Difference:")
for i in final:
    print(i)
print("Totoal Head Movements are:"+str(sum(final)))
