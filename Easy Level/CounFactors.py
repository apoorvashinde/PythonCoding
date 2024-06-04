def count_fact(num):
    count = 0
    for i in range(1,num):
        if i * i > num:
            break
        if num % i == 0:
            if i == (num/i):
                count += 1
                break
            else:
                count += 2
    return count 


count_fact(19)
