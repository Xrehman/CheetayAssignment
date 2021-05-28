#Question no 1:
#Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person,
#assuming that a person can only work on a single activity at a given day. 

#Soliution:
#in python

def activityselection(s , f ,n): 
    i = 0
    k=0
    z=0
      
    for j in range(n): 
        if(k==0):
            z=z+1
            k=1
        else:    
            if s[j] >= f[i]:
                i=j
                z=z+1
    print ("Total No of Activities that are performed")       
    print(z)
n=4
s = [1, 3, 2, 5]
f = [2, 4, 3, 6]
activityselection(s , f, n)
