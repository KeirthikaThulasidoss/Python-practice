lst = list()
lst = ('vege','fruit','spinach','nuts','seeds')
print(lst)

empty_list = list()
print(len(empty_list))

empty_list1 = []
print(empty_list1)

fruits = [] 
fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
print(fruits)
print(len(fruits))
print('Fruits:',fruits)
print('No.of fruits:',len(fruits))
print(type(fruits)) #[] indicates it as lists

fruits = ('apple','orange','guava','litchy','rambutan','melons','berry')
print("Fruits:", fruits)
print('No.of fruits:',len(fruits))
print(type(fruits)) #it is tuple 

#list can have dif datatypes
lst = ['keirthi', 22, True , {'course':'python' , 'city': 'thanjavur'}]
print(type(lst)) 
print(len(lst)) # o/p 4 , dic considered as one list

fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
first_fruit = fruits[0]
print(first_fruit) # positive indexing

fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
last_fruit = fruits[-1]
print(last_fruit) #accessing items using negative indexing

num = ['num1','num2','num3','num4','num5']
first_num, sec_num, third_num , *rest =num
print(first_num)
print(sec_num)
print(third_num)
print(rest) # *operator collects rest of the elements as lists

num = ['num1','num2','num3','num4','num5']
abc, dif, ghi , *lmn =num
print(abc)
print(dif)
print(ghi)
print(lmn)

fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
new_fruits = fruits[0:4]
print(new_fruits) # [start:stop] exclude the stop number

new_fruits1 = fruits[0:]#starting to all the elements of the list
print(new_fruits1)

new_fruits2 = fruits[2:]
print(new_fruits2)

new_fruits3 = fruits[::3]
print(new_fruits3)

new_fruits4 = fruits[::-1]
print(new_fruits4)

all_fruits = fruits[-3:]
print(all_fruits)

all_fruits1= fruits[-4:-2]
print(all_fruits1)

#modifying lists
fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
fruits[2] = 'grapes'
print(fruits)

last_index = len(fruits) - 1
print(last_index)

#checking items in the list
is_there = 'guava' in fruits
print(is_there) #False

is_there = 'litchy' in fruits
print(is_there)

fruits = ['apple','orange','guava','litchy','rambutan','melons','berry']
fruits.append('chickoo') #item will be added in the last
print(fruits)

fruits.append('lime')
print(fruits)

# syntax to insert a list in prefered order
# lst = ['item1', 'item2']
# lst.insert(index, item)

fruits =  ['apple','orange','guava','litchy']
fruits.insert(2,'cherry')
print(fruits) #specify the index no

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
fruits.remove('guava')
print(fruits) #just specify the item that has to be removed

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
fruits.pop(4)
print(fruits) #removes the element from the list based on the mentioned index no

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
fruits.pop()
print(fruits) #.pop() removes the last element

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
del fruits[2]
print(fruits)

#del fruits
#print(fruits) #NameError: name 'fruits' is not defined

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
print(fruits)

del fruits[1:3]
print(fruits)

#clear() clears the list
fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
print(fruits)
fruits.clear()
print(fruits)

fruits = ['apple', 'orange', 'cherry', 'guava', 'litchy']
copyied = fruits.copy()
print(copyied)

positive_num = [ 1,2,3,4,5]
zero = [0]
negative_num = [-5,-4,-3,-2,-1]
integers = negative_num + zero + positive_num
print(integers)

fruit1 = ['apple', 'avacado','mulbeery']
fruit2 = ['orange', 'papaya', 'tomato']
fruit3 = ['blueberry','dragon fruit']
list_of_fruits = fruit1 + fruit3 + fruit2
print(list_of_fruits)

fruit1 = ['apple', 'avacado','mulbeery']
fruit2 = ['orange', 'papaya', 'tomato']
fruit1.extend(fruit2) #add iterable of elements - checks one by one on elements
#all_fruits = fruit1.extend(fruit2)
#print(all_fruits)

positive_num = [ 1,2,3,4,5]
zero = [0]
positive_num.extend(zero)
print('Numbers are:',positive_num)

#count() no of times a item appears on list
num = [ 1,1,2,3,4,5,2,5,2,2,6,7,2]
print(num.count(2))

fruits = ['apple', 'orange','lime','apple','pomegranate','orange']
print(fruits.count('lime'))

#index() returns the index of a item
fruits = ['apple', 'orange','lime','pomegranate','orange']
print(fruits.index('lime'))

fruits = ['apple', 'orange','lime','pomegranate','orange']
fruits.reverse()
print(fruits)

fruits = ['apple', 'orange','lime','pomegranate','orange']
fruits.sort()
print(fruits) #o/p in ascending alphabetical order 
fruits.sort(reverse =True)
print(fruits)

fruits = ['apple', 'orange','lime','pomegranate','orange']
print(sorted(fruits))
print(sorted(fruits,reverse=True))