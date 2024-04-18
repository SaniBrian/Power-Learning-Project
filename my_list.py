#creating anempty list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

new_items = [10, 20, 30, 40]

#inserting a variable at the second index
my_list.insert(2, 15)

#extending the list
new_items = [50, 60, 70]
my_list.extend(new_items)


my_list.pop(-1)
sorted_list = sorted(my_list)

#finding the index of an element
print(sorted_list.index(30))
