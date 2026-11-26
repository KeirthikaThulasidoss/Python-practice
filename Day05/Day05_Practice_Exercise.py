#Declare an empty list. Declare a list with more than 5 items
# Find the length of your list
# Get the first item, the middle item and the last item of the list

lst = list()
print(lst)

num = [ 1,2,3, 4,5]
print(num)
print(len(num))
print(num[0])
print(num[2])
print(num[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types= [ 'keirthika' , 22 , 5.1 , 'single', 'No.28, Natarajan Nagar,Thanjavur ']
print(mixed_data_types)
print(type(mixed_data_types))

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# Print the list using print()
# Print the number of companies in the list
# Print the first, middle and last company
# Print the list after modifying one of the companies
# Add an IT company to it_companies
# Insert an IT company in the middle of the companies list
# Change one of the it_companies names to uppercase (IBM excluded!)
# Join the it_companies with a string '#;  '
# Check if a certain company exists in the it_companies list.
# Sort the list using sort() method
# Reverse the list in descending order using reverse() method
# Slice out the first 3 companies from the list
# Slice out the last 3 companies from the list
# Slice out the middle IT company or companies from the list
# Remove the first IT company from the list
# Remove the middle IT company or companies from the list
# Remove the last IT company from the list
# Remove all IT companies from the list
# Destroy the IT companies list

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

it_companies[2]='ConcertIDC'
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
new_addon = ['Accenture']
new_list = it_companies + new_addon
print(new_list)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.insert(3 ,'ashley')
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies= it_companies[1].upper()
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies = ' # '.join(it_companies)
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
is_there = 'IBM' in it_companies
print(is_there)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.sort()
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.sort(reverse=True)
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
new_company = it_companies[0:4]
print(new_company)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
new = it_companies[3:4]
print(new)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
new1 = it_companies[-3:]
print(new1)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
it_companies.clear()
print(it_companies)

#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React','Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
copied = full_stack.copy()
print(copied)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.append('python')
print(full_stack)

full_stack.append('SQL')
print(full_stack)