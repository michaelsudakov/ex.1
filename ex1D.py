from typing import List


def remove_dividend_numbers(num_list: List[int], divisor: int) -> List[int]:
    num_list = (list(filter(lambda numbers: numbers % divisor != 0, num_list)))
    return num_list


list1 = remove_dividend_numbers([2, 9, 100, 6, 8, 3], 2)
print(list1)
