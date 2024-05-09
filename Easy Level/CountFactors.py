def CountFactors(A):
    count_factors = 0
    for i in range(1,A):
        if i * i > A:
            break
        if A % i == 0:
            if i == (A%i):
                count_factors += 1
                break
            else:
                count_factors +=2
    return count_factors

CountFactors(9)