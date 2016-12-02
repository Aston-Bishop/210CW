
def trailing (factorial):
    fives = factorial // 5
    zeros = fives
    while fives >= 5:
        fives = fives // 5
        zeros = zeros + fives
    print("Trailing zeros: " + str(zeros))

factorial = int(input("Factorial: "))
trailing(factorial)

# The Big O Notation for this code would be O(n)
