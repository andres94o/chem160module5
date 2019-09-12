import sys
import math
def distance(p1, p2): #this defines the function
    if len(p1) != len(p2): #cheks if the vector lengths match 
        sys.exit("Vectors have different length")
    sum = 0
    for i in range(len(p1)): #will go through each # in p1
        sum = sum + (p1[i] -p2[i])**2 #will sum up the current sum + first number in the 1st vector - first # in 2nd vector and raise the differnce to the 2nd power
        return math.sqrt(sum) #returns square root of sum
