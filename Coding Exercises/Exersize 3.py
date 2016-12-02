#PROGRAM HighestSquare:
#    Read I;
#    Sqr = 0;
#    WHILE (I >= Sqr **2)
#        DO Sqr = Sqr + 1;
#    ENDWHILE;
#    Print Sqr - 1;    
#END.

i = 1023

sqr = 0
while i >= sqr ** 2:
    sqr += 1

print(sqr-1)
