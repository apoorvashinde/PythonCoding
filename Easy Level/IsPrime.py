def Prime(A):
    if A > 1:
        for i in range(2,A):
            if A % i == 0:
                return False
        return True
    return False

Prime(12)