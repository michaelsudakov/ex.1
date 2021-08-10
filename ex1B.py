from typing import List
def remove_dividend_numbers(num_list: List[int], divisor: int) -> List[int]:
    for number in num_list.copy():
        if number % divisor == 0:
            num_list.remove(number)
    return num_list
list1 = remove_dividend_numbers([2, 12, 100, 6, 8, 3], 2)
print(list1)


