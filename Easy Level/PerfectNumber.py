def PerfectNumber(A):
    divisor_sum = 0
    for i in range(1,A):
        if A % i == 0:
            divisor_sum += i
            if divisor_sum > A:
                break
    if divisor_sum == A:
        return 1
    else:
        return 0
    
PerfectNumber(4)
