i <- INPUT

FUNCTION primecheck(d,i):
    IF d = 1:
        RETURN OUTPUT "True"
    ELSEIF n%d = 0:
        RETURN OUTPUT "False"
    ELSE:
        primecheck(d-1,i)
    ENDIF
ENDFUNCTION

primecheck(i-1,i)


i = input("Input integer: ")

def primecheck(d,i):
    if d == 1:
        return print("True")
    elif n%d == 0:
        return print("False")
    else:
        primecheck(d-1,i)
        
primecheck(i-1,i)
