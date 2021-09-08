def tower_builder(n_floors):
    start = 0
    floor_c = n_floors*2-1
    floor = floor_c
    array = []
    for i in range(n_floors):
        s = (' ' * start) + ('*' * floor) + (' ' * start)
        start += 1
        floor -= 2
        array.append(s)
    array.reverse()
    return array
print(tower_builder(5))