my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

try:
    my_tuple.add(6)
    print("6 was added using add(): ", str(my_tuple))

except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple += (6,)
    print("6 was added using concatenation of tuples:", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple += (6)
    print("6 was added using concatenation of tuple and int: ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple.append(6)
    print("6 was added using append(): ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple.extend(6)
    print("6 was added using extend(): ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))
