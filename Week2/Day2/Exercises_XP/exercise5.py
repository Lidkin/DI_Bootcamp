for i in range(1, 21):
    print(i)

my_list = [i for i in range(1, 21)]
print(my_list)

for i in range(1, 21, 2):
    print(i)

even_idx_list = [i for i in range(1, 21, 2)]
print("Those elements has an even index:", str(even_idx_list))

even_int_list = [i for i in range(2, 21, 2)]
print("Those integers is even:", str(even_int_list))
