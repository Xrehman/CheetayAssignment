#Question: 2 
#Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
#Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.


def equilibriumPoint(arr,n):
    
    totalsum = sum(arr)
    lsum = 0
    for i in range (n):
         
       
        totalsum -= arr[i]
         
        if lsum == totalsum:
            return i
        lsum += arr[i]

    return -1
     
n=5
arr = [1,3,5,2,2]
print ('Equilibrim point is  ',equilibriumPoint(arr,n))
