
import random

def swap(n1, n2):                                           # simple function to swap two numbers
    return n2, n1

def shuffle (ordered_list):                                 # Base on the Fisher–Yates shuffle
    for x in range(0, len(ordered_list)-1):
        j = random.randint(0,x)
        ordered_list[x],ordered_list[j] = swap(ordered_list[x],ordered_list[j])
        
    print(ordered_list)
        
ordered_list = [5,3,8,6,1,9,2,7]

shuffle(ordered_list)

# The Big O notation for this code is O(N) as it runs through the loop only once
