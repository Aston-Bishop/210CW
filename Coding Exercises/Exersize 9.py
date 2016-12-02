def binaryInterval(l, low, high):
    first = 0
    last = len(l)-1
    found = False
    
    while first<=last and not found:
        mid = (first + last)//2

        if l[mid] >= low and l[mid] <= high:
            found = True

        else:
            if low < l[mid]:
                last = mid-1
            else:
                first = mid+1   

    return found
    
l = [2,3,5,7,9,13] 
print(binaryInterval(l, 15, 16))

