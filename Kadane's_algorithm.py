#Kadane's algorithm
#Mainly used to find maximum subarray in contiguous array
def kadanes_algorithm(arr):
  maxEndingHere=maxSofar=arr[0]

  for num in arr[1:]:
    maxEndingHere=max(maxEndingHere, maxEndingHere + num)
    maxSofar=max(maxSofar, maxEndingHere)
  
  return maxSofar

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(array)
print("Maximum subarray sum:", result)  
