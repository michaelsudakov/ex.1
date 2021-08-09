def numdivision(numlist , num ):
    numinlist  = len(numlist)
    counter = 0
    for numbers in range(numinlist ) :
        if numlist[counter] % num == 0 :
            for extranum in range(numinlist - numbers - 1):
                numlist[counter + extranum] = numlist[counter + extranum + 1]
            counter = counter-1
            numlist.pop()
        counter = counter + 1
    return numlist

numlist = [2, 9, 100, 12, 8, 3]
num = 3
print(numdivision(numlist, num))