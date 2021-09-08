def last_digit(n1, n2):
    if n2==0:
        return 1
    first = n1 % 10
    for i in range(2,10):
        if (first**i) % 10 == first:
            return (first**(n2%i+i))%10



print(last_digit(2 , 5))