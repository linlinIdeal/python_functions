'''
# loop a list
'''
car_list = ['BWM', 'Benz', 'Cadillac', 'Chrysler', 'Chevroler', 'Porsche']
for car in car_list:
    print(car)
print('-------------------------------------------------')

'''
# the range() function
'''
# one argument
for value in range(5):
    print(value)
print('-------------------------------------------------')

# two arguments
for value in range(1,5):
    print(value)
print('-------------------------------------------------')

# three arguments
for value in range(0,11,2):
    print(value)
print('-------------------------------------------------')

for index in range(len(car_list)):
    print('car_list['+str(index) + '] = ' + car_list[index])
print('-------------------------------------------------')

'''
# use range to make a list of number
'''
number_list = list(range(1, 11))
print(number_list)

'''
# some functions of number list
'''
min_number = min(number_list)
max_number = max(number_list)
sum_number = sum(number_list)
print('the minimum：' + str(min_number))
print('the maximum：' + str(max_number))
print('the sum：' + str(sum_number))
print('-------------------------------------------------')

'''
# list comprehensions
'''
squares = [value**2 for value in range(1, 11)]
print(squares)
print('-------------------------------------------------')

'''
# you can also use this function at other place
'''
print(car_list)
car_list = [item.lower() for item in car_list]
print(car_list)
print('-------------------------------------------------')

'''
# slice a list
# I really don't know how to describe it in English. 
'''
print('car_list')
print(car_list)
print('-------------------------------------------------')
print('car_list[0:3]')
print(car_list[0:3])
print('-------------------------------------------------')
print('car_list[1:3]')
print(car_list[1:3])
print('-------------------------------------------------')
print('car_list[:3]')
print(car_list[:3])
print('-------------------------------------------------')
print('car_list[:3:2]')
print(car_list[:3:2])
print('-------------------------------------------------')
print('car_list[::2]')
print(car_list[::2])
print('-------------------------------------------------')
print('car_list[:]')
print(car_list[:])
print('-------------------------------------------------')
print('car_list[-1:]')
print(car_list[-1:])
print('-------------------------------------------------')
print('car_list[-6:-1]')
print(car_list[-6:-1])
print('-------------------------------------------------')
print('car_list[::-1]')
print(car_list[::-1])

'''
# define a tuple
'''
longitude_beijing = (116.577925,39.7652)

# accessing elements
print(longitude_beijing[0])
print(longitude_beijing[1])
print('-------------------------------------------------')
# you can't change the item in the tuple
# longitude[0] = 1 # 'tuple' object does not support item assignment
'''
# but you can change the tuple
'''
longitude = (1,2)
longitude = longitude_beijing
print(longitude)
print('-------------------------------------------------')
'''
# loop a tuple
'''
for value in longitude_beijing:
    print(value)



