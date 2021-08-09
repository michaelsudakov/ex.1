
try:
    def calculate_average ():
        counter = 0
        sum = 0
        function_stop = "q"
        num = input("enter num if you want to stop enter " + function_stop + " ")
        while num != function_stop :
            sum += float(num)
            counter += 1
            num = input("enter num ")
        return sum/counter
    print(calculate_average())
except:
    print("bad input")



