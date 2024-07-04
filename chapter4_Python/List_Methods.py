my_list = [1, 3, 9]                     # append will add number 11 at the end of the list
my_list.append(11)
print(my_list)

clear_list = [1, 2, 3]                  # clear will remove all items from list
clear_list.clear()
print(clear_list)

copy_list = [1, 2, 3]                   # copy will copy it into new list
new_copy = copy_list.copy()
print(new_copy)

count_2 = [1, 2, 2, 3, 2]               # count will find occurence of 2 in list
print_twos = count_2.count(2)
print(print_twos)


list1 = [1, 2, 3]                       # extend will Add elements from another iterable to the end of the current list
list2 = [4, 5]
list1.extend(list2)
print(list1)

index_list = [10, 20, 30, 20]           # index will Return the index of the first occurrence of a specified value
index_of_20 = index_list.index(20)
print(index_of_20)

insert_list = [1, 2, 3]                 # insert will add an element at a specific position, in this case it will add 10 in index position 1
insert_list.insert(1, 10)
print(insert_list)

pop_list = [1, 2, 3]                    # pop will Remove and return the element at a specified position
popped_element = pop_list.pop(1)
print(popped_element)
print(pop_list)

remove_list = [1, 2, 3, 2]              # remove will Remove the item with a specified value
remove_list.remove(2)
print(remove_list)

reverse_list = [1, 2, 3]                # reverse will  Reverse the order of the list
reverse_list.reverse()
print(reverse_list)

sort_list = [3, 1, 2]                   # sort will Sort the list in ascending order
sort_list.sort()
print(sort_list)

