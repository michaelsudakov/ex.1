from typing import List
def remove_dividend_numbers(num_list: List[int], divisor: int) -> List[int]:
    return [number for number in num_list if number % divisor != 0]

list1 = remove_dividend_numbers([2, 12, 100, 6, 8, 3], 4)
print(list1)

