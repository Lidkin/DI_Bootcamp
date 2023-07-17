my_fav_numbers = {22, 99, 15, 5, 100}
my_fav_numbers.add(19)
my_fav_numbers.add(89)
print(my_fav_numbers)

friend_fav_numbers = {5, 19, 30, 33, 100}

# Because set is unorderd collection we can't now which number is the last one
# There are three options for deleting the last number
# 1. Remove number which added last
my_fav_numbers.remove(89)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Set without number which was added last: {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))
# return the removed number
my_fav_numbers.add(89)

# 2. remove an arbitrary element
my_fav_numbers.pop()
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Set without arbitrary element: {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))
# return the removed number
my_fav_numbers.add(99)

# 3. remove biggest number
my_fav_numbers.remove(max(my_fav_numbers))
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Set without biggest number {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))
