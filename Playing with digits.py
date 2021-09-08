def dig_pow(n, p):
    arr_num = []
    num = n
    while num != 0:
        arr_num.append(num % 10)
        num //= 10
    arr_num.reverse()
    for i in range(len(arr_num)):
        num+=arr_num[i]**p
        p+=1
    if num % n == 0:
        return num//n
    else:
        return -1
print(dig_pow(46288,3))