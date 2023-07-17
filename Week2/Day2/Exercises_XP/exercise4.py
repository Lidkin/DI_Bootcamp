# Float is a data type that represents real numbers with fractional parts.
# Integers are whole numbers without any fractional part, while floats can represent both whole numbers and numbers with decimal places.

my_floats_list = []
k = 1.0

for i in range(9):
    my_floats_list.append(k)
    k += 0.5

print(my_floats_list)

# ++++++++++++++++++++++++++++++++++++++++
start = 1.0
stop = 5.5
step = 0.5

for i in range(int((stop - start)/step)):
    my_floats_list[i] = start + i * step
# other_floats_list = [start + i * step for i in range(int((stop - start)/step))]
print(my_floats_list)
