Num_List = [2, 12, 100, 6, 8, 3]
divisor = 10

print(list(filter(lambda numbers: numbers % divisor != 0, Num_List)))
