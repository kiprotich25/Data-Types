print("Welcome to the data structures section!")
my_list= []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
list_2=[50,60,70]
my_list.extend(list_2)
print(my_list)
del my_list[-1]
my_list.sort()
print(my_list)
position=my_list.index(30)
print("The index of 30 is:", position)
