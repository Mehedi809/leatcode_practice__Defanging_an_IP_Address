def linear_search(l, x):
    # a = len(l)

    for i in l:
        if i == x:
            return 'Yes'
         
    return 'No'
    
l = [1, 2, 3, 6]
x = 2


print(linear_search(l, x)
)