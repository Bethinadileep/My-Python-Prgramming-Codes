#code by: Bethina Dileep
def convert_peeks_valleys(arr):
    n = len(arr)
    for i in range(0,n,2):
        if i>0 and arr[i]<arr[i-1]: #swap if current element is less than previous
            arr[i],arr[i-1]=arr[i-1],arr[i]

        if i<n-1 and arr[i]<arr[i+1]: #swap if next element is lower than current
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

a = [8,5,2,1,4,5,3,4]
print(convert_peeks_valleys(a))
