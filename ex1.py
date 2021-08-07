

def avg():
    counter = 0
    sum = 0
    num = input("enter num if you want to stop enter q ")
    while num != "q" :
        sum += float(num)
        counter += 1
        num = input("enter num ")
    return sum/counter

print(avg())
