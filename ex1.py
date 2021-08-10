FUNCTION_STOP_CHAR = "q"


def calculate_average() -> int:
    counter = 0
    sum = 0
    num = input(f'enter num if you want to stop enter {FUNCTION_STOP_CHAR} ')
    while num != FUNCTION_STOP_CHAR:
        try:
            sum += float(num)
            counter += 1
            num = input("enter num ")
        except ValueError:
            print("bad input")
            num = 0
            counter -= 1
    return sum / counter


print(calculate_average())
