def unique_in_order(iterable):
    arr = []
    if len(iterable)==0:
        return arr
    sym=iterable[0]
    arr.append(sym)
    for i in range(1,len(iterable)):
        if iterable[i] != sym:
            sym = iterable[i]
            arr.append(sym)
    return arr
print(unique_in_order(''))