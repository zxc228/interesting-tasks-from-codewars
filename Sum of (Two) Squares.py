def all_squared_pairs(n):
    arr=[]
    end = int(n**(1/2))
    for i in range(end+1):
        if (n-i**2)**(1/2) == int((n-i**2)**(1/2)):
            arr.append([i,int((n-i**2)**(1/2))])

    if len(arr) % 2 == 0:
        return arr[0:len(arr)//2]
    else:
        return arr[0:(len(arr) // 2)+1]


print(all_squared_pairs(2))