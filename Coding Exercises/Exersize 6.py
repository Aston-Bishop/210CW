#i <- INPUT
#FUNCTION reverse (i):
#    IF len(i) = 0:
#        RETURN i
#    ELSE:
#        RETURN reverse(i[1:]) + [i[0]]
#    ENDIF
#ENDFUNCTION
#
#i <- i.split()
#OUTPUT reverse(i)

i = input("Phrase to be reversed: ")

def reverse (i):
    if len(i) == 0:
        return i
    else:
        return reverse(i[1:]) + [i[0]]
        
i = i.split()
print(reverse(i))

# The Big O Notation for this code would be O(log N)
