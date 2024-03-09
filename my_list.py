# Week Two Assignment

# create an empty list 
my_list = []

# append elements to list 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 - at second position (index = 1)
my_list.insert(1, 15)

# another list
other_list = [50, 60, 70]

# extend my_list with another_list
my_list.extend(other_list)

# remove last element from list  (index = -1 ) denotes the last element.
# del my_list[-1]
my_list.remove(my_list[-1])

# sort my_list in ascending order.
my_list.sort()

print("\n my_list = ", my_list)

# find and print index of value = 30
print(" index of 30 is : ", my_list.index(30))

print("\n")

