B <- INPUT matrix
C <- INPUT matrix

ADD_MAT(B,C)
    for i <- 1 to n
        for j <- 1 to p
            A[i[j]] <- B[i[j]] + C[i[j]]
    RETURN A

MULT_MAT(B,C)
    for i <- 1 to n
        for j <- 1 to p
           sum <- 0
           for k <- 1 to m
               sum <- sum + B[i[k]] * C[k[j]]
           A[i[j]] <- sum
    RETURN C

SUB_MAT(B,C)
    for i <- 1 to n
        for j <- 1 to p
            A[i[j]] <- B[i[j]] - C[i[j]]
    RETURN A

MULT_NR(R2,2)
    for i <- 1 to n
        for j <- 1 to p
            R3[i[j]] <- R2[i[j]] * 2
    RETURN R3

R1 <- MULT_MAT(B,C)
R2 <- ADD_MAT(B,C)
R3 <- MULT_NR(R2,2)

A <- SUB_MAT(R1,R3)

# The Big O Notation for this code is O(N^3)
