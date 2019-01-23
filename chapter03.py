'''
# create list
# You can add anything into the list
'''
int_list = [1, 2, 3, 4, 5, 6]
str_list = ['BWM', 'Benz', 'Cadillac', 'Chrysler', 'Chevroler', 'Porsche']
mix_list = ['a', 1, 'b', 'c', 2]

'''
# accessing elements in a list
# the index positions start at 0 (almost erver program language like this)
# use the index -1, return the last item in the list 
'''
print('the first of int_list: ' + str(int_list[0]))
print('the fourth of str_list: ' + str_list[3])
# print(mix_list[10]) #list index out of range
print('the last one of str_list: ' + str_list[-1]) # the last one
print('the last one of str_list: ' + str_list[-2]) # the second from the end
print('-------------------------------------------------')
'''
# appending element to the end of a list
'''
str_list.append('Volvo')
print('appending to the end of str_list:' + str_list[-1])

'''
# change element of a list
'''
print('str_list[0] before change:' + str_list[0])
str_list[0] = 'Smart'
print('str_list[0] after change:' + str_list[0])

'''
# insert element into a list
'''
print('str_list before insert:')
print(str_list)
str_list.insert(1, 'JEEP')
print('str_list after insert:')
print(str_list)

'''
# remove element from a list
'''
print('str_list before remove:')
print(str_list)
del str_list[3]
print('str_list after remove:')
print(str_list)

'''
# remove the last item of a list ( use pop() )
'''
print('str_list before pop:')
print(str_list)
print('pop item:' + str_list.pop())
print('str_list after pop:')
print(str_list)

'''
# remove an item by value
# remove the first item equal value
'''
str_list.insert(0, 'DODGE')
str_list.insert(0, 'DODGE')
print('before remove DODGE:')
print(str_list)
str_list.remove('DODGE')
print('after remove DODGE:')
print(str_list)
print('-------------------------------------------------')
'''
# sort a list permanently 
# 'sort' is a function of the object 'list', you will learn it at chapter 9.
'''
str_list_copy_1 = str_list[:] # I copy a list， you will learn the function at chapter 4.
print('str_list_copy_1 before sort:')
print(str_list_copy_1)
str_list_copy_1.sort()
print('str_list_copy_1 after sort:')
print(str_list_copy_1)
print('-------------------------------------------------')
'''
# sort a list tempararily
'''
str_list_copy_2 = str_list[:] 
print('str_list_copy_2 before sort:')
print(str_list_copy_2)
str_list_sorted = sorted(str_list_copy_2)
print('the sorted list:')
print(str_list_sorted)
print('str_list_copy_2 after sort:')
print(str_list_copy_2)
print('-------------------------------------------------')
'''
# display a list in reverse 
'''
str_list_copy_3 = str_list[:] 
print('str_list_copy_3 before sort:')
print(str_list_copy_3)
str_list_sorted_reverse = sorted(str_list_copy_3, reverse=True)
print('the sorted list:')
print(str_list_sorted_reverse)
print('str_list_copy_3 after sort:')
print(str_list_copy_3)
print('-------------------------------------------------')

'''
# reverse a list
# 'reverse' is a function of the object 'list', you will learn it at chapter 9.
'''
str_list_copy_4 = str_list[:] 
print('str_list_copy_4 before reverse:')
print(str_list_copy_4)
str_list_copy_4.reverse()
print('str_list_copy_4 after reverse:')
print(str_list_copy_4)
print('-------------------------------------------------')

'''
# get the length of a list 
'''
length = len(str_list)
print('There are ' + str(length) + ' items in the list "str_list"')
print('-------------------------------------------------')
