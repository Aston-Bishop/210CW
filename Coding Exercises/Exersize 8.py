#i <- INPUT
#
#FUNCTION vowelchecker(i):
#    vowel <- ["a","e","i","o","u"]
#    IF i = "":
#        RETURN i
#    ENDIF
#    IF i[0] in vowel:
#        RETURN vowelchecker(i[1:])
#    ELSE:
#       RETURN i[0] + vowelchecker(i[1:])
#    ENDIF
#ENDFUNCTION

OUTPUT vowelchecker(i)


i = "beautiful"

def vowelchecker(i):
    vowel = ["a","e","i","o","u"]
    if i == "":                                 # Base Case
        return i
    if i[0] in vowel:
        return vowelchecker(i[1:])
    else:
        return i[0] + vowelchecker(i[1:])

print(vowelchecker(i))
