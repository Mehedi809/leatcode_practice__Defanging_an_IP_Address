# def findSingle(A, ar_size): 
#     for i in range(ar_size): 
#         count = 0
#         for j in range(ar_size):      
#             if(A[i] == A[j]): 
#                 count += 1
#         if(count == 1): 
#             return A[i] 
            
#     return -1
  
# ar = [2, 3, 5, 4, 5, 3, 4] 
# n = len(ar) 

# print("Element occurring once is", findSingle(ar, n)) 



#----------------------


def insertion_sort_algorithm(lst):
    len_lst = len(lst)

    for index in range(1, len_lst):#1...4
        key_value = lst[index]   #12
        previous_index = index - 1#1-1 = 0 ,   O = 6

        while previous_index >= 0 and key_value < lst[previous_index]: #0>=0 TRUE and 12<=6 false
            lst[previous_index + 1] = lst[previous_index]
            previous_index -= 1

        lst[previous_index+1] = key_value
        print('------------------')
        print(lst)



a = [12, 6, 4, 18, 22, 9]

insertion_sort_algorithm(a)