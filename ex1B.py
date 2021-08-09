
def remove_dividend_numbers(num_list: list[int], divisor: int):
    for number in num_list[:]:  
        if number % divisor == 0:
            num_list.remove(number)
    return num_list
list1 = remove_dividend_numbers([2, 12, 100, 6, 8, 3], 2)
print(list1)


