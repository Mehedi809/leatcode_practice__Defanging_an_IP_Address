num = int(input("enter a number:" ))
sum = 0
sum_list = []
for i in range(num):
    c = int(input("enter a value: "))
    sum += c
    sum_list.append(sum)

print(sum_list)