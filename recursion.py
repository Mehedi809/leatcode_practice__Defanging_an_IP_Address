def recursive_func(MinNumber):
    #base case
    if MinNumber == 100:
        return 
    
    print(f'{MinNumber} - Mehedi,', end = ' ')

    #recursion case

    recursive_func(MinNumber+1)


recursive_func(1)