def binary_search(x, y):
    start = 0
    end = len(x)-1

    while start <= end:
        mid = (start+end)//2
        print(f'start{start}, mid{mid}, end{end}')
        
        if x[mid] == y:
            print('value yes')
            break
        
        elif x[mid] < y:
            start = mid+1

        else:
            end = mid - 1



x = [2, 3,45, 67, 89,98,99,100]

y = 99

a = binary_search(x, y)
print(a)