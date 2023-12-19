def bubble_sort(lst):
    len_of_lst = len(lst)

    for i in range(len_of_lst):
        j = len_of_lst - i -1

        for k in range(j):
            
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]


lst = [-20, -32, -3, 0, 567, 87]
bubble_sort(lst)
print(lst)