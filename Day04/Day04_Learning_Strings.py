letter = 'P'
print(letter)
print(len(letter))

greetings = 'Hello'
print(greetings)
print(len(greetings))

sentence = 'I am excited to learn about LLM'
print(sentence)

multiline_string = '''As a fresher corporate world is new to me.
I am very excited to experience new atmosphere.
Thanks to Concert IDC for choosing me.'''
print(multiline_string)

multi_line_string = """As a fresher corporate world is new to me.
I am very excited to experience new atmosphere.
Thanks to Concert IDC for choosing me."""
print(multi_line_string)

first_name = 'keirthika'
last_name = 'thulasidoss'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(first_name)>len(last_name))

a = '3'
b= '4'
space = '    '
c = a + space + b
print(c) #to give space , just give balnk space within the quotes

print('I hope everyone are enjoying it. \nAre you?')
print('Days\tExercise\tTopics')
print('Day 1\tA\t\tFundmentals')
print('Day 2\tB\t\tStrings')
print('Day 3\tC\t\tOperators')
print('Day 4\tD\t\tList')
print('This is a backslash symbol \\')
print('In every programming language it starts with \"Hello World\"') #to write double quotes

#string formatting
first_name = 'keirthika'
last_name = 'thulasidoss'
language = 'python'
full_name = 'I am %s %s.I teach %s.' %(first_name,last_name,language)
print(full_name)

#string and number formatting
age = 22 
fav = 'car'
sentence = 'I am %d years old. \n\t I like %s' %(age,fav)
print(sentence)

radius = 8.8
pi = 3.14
area = pi * radius * 2
formatted_string = (' the area of circle with radius %.1f is %.2f') %(radius,area)
print(formatted_string)

python_lib = ['Django','Flask','Pandas','Matplotlib','Numpy']
formattedstrings = ('The following are python libraies:%s') %(python_lib)
print(formattedstrings)
python_lib[2] = ('API')
print(python_lib)

first_name = 'keirthika' 
last_name = 'thulasidoss'
language = 'python'
formatted_string =( 'I am {} {}. I teach {}.'.format(first_name,last_name,language))
print(formatted_string)

a = 3
b = 4

print('{} + {} = {}'.format(a,b,(a + b)))
print('{} - {} = {}'.format(a,b,(a-b)))
print('{} / {} = {}'.format(a,b,(a/b)))
print('{} * {} = {}'.format(a,b,(a*b)))
print('{} // {} = {}'.format(a,b,(a//b)))
print('{} % {} = {}'.format(a,b,(a%b)))
print('{} ** {} = {}'.format(a,b,(a**b)))

#string and numbers
radius = 10 
pi = 3.14
area = radius * pi * 2
formatted_string= 'The area of circle having radius {} is {:.2f}'.format(radius,area)
print(formatted_string)

a = 3
b = 4

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} % {b} = {a%b}')

language = 'python'
first_letter = language[0]
print(first_letter)

last_index = len(language) - 1
print(last_index)

last_letter = language[last_index]
print(last_letter)

language = 'python' 
print(language[-2])
print(language[0])

language = 'python'
first_three = language[0:3]
print(first_three)

last_three=language[-3:]
print(last_three)

random=language[1:5]
print(random)

#reversing the string
greetings ="Hello World"
reversed_string = greetings[::-1]
print(reversed_string)

name= 'keirhtikathulasidoss'
rev = name[0:15:3]
print(rev)

#string methods
challenge = 'learn python in thirty days'
print(challenge.capitalize())

#string count (start,value,end)
challenge = 'Learn python in thirty days'
print(challenge.count('r'))
print(challenge.count('th'))
print(challenge.count('y',3,12))

#endswith
challenge= 'Learn python in thirty days'
print(challenge.endswith('ys'))
print(challenge.endswith('on'))

#expandtabs removes the tab and gives default of 8 spacing
challenge = 'Learn\tpython\tin\tthirty\tdays'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#find() returns the first occurence of the substring index whereas count() returns the no of occurences
challenge = 'Learn python in thirty days'
print(challenge.find("y")) #returns the index of y
print(challenge.find('z')) #if not available returns -1
print(challenge.find('th')) # th is occured twice but shows the first occured index value

#rfind() returns the last occurence index of the substring
challenge = 'Learn python in thirty days'
print(challenge.rfind('y')) #last occured index value
print(challenge.rfind('th'))
print(challenge.rfind('m')) #no such value so returns -1

#index()
challenge = 'Learn python in thirty days'
sub_string = 'rn'
print(challenge.index(sub_string))
#print(challenge.index(sub_string,9))

#rindex() returns the highest index of the sub string
challenge = 'Learn python in thirty days'
sub_string = 'i'
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string,7)) # here 7 is the index to search from 
print(challenge.rindex('on',8))

#isalnum - if there is space then it is not alphanumeric
challenge = 'Learnpythonintirtydays'
print(challenge.isalnum())

challenge = 'Learnpythonin30days'
print(challenge.isalnum())

challenge = ' Learn python in thirty days'
print(challenge.isalnum())

challengge = 'Learn python in 30 days'
print(challenge.isalnum())#if there are spaces then it is not alnum

#isalpha checks all elements are string excluding space
challenge ='Learn python in thirty days'
print(challenge.isalpha())

challenge = 'Learnpythonin30days'
print(challenge.isalpha())

challenge= 'Learnpythoninthirydays'
print(challenge.isalpha())

num = '2345'
print(num.isalpha())

#isdecimal() checks if all the strings are decimal (0-9)
challenge = ' Learnprogramming'
print(challenge.isdecimal())

deci = '2345129034'
print(deci.isdecimal())

dec = '123 234'
print(dec.isdecimal())

code='\u00B2'
print(code.isdecimal())

abc = '123.5'
print(abc.isdecimal())

#isdigit checks all characters are numbers and also unicode
challenge = '30'
print(challenge.isdigit())

challenge = '\u00B2'
print(challenge.isdigit())

#isnumeric just like digit accepts more symbols like 1/2
num = '344'
print(num.isnumeric())

num = '\u00B2'
print(num.isnumeric())

num = '23.32'
print(num.isnumeric())

#isidentifier checks for valid variable name
num = '23hiall'
print(num.isidentifier())

num = '_23_ae'
print(num.isidentifier())

num = 'adadf_2e_ad3e4'
print(num.isidentifier())

#islower checks all the strings are in lower case
num = 'hello world'
print(num.islower())

num = 'Hello world'
print(num.islower())

#isupper checks whether all the srings  r in uppercase
word = 'PYTHON'
print(word.isupper())

word = 'python'
print(word.isupper())

#join() returns the concatenated string
#lang = 'python'
web_tech = ['HTML', 'CSS', 'Java']
result = ' '.join(web_tech)
print(result)

web_tech = ('HTML', 'CSS' , 'Java')
result = '#' .join(web_tech)
print(result)

#strip removes the character from last or first of the string , not from the middle
challenge = 'thirty days pythoon'
print(challenge.strip('noth'))

#replace()
challenge = 'Learn python in thirty days'
print(challenge.replace('python', 'java'))

#split() splits the string using the given string or space as a separator
challenge = 'Learn python in thirty days'
print(challenge.split(' '))

challenge = 'Learn python in thirty days'
print(challenge.split(', '))

#title() returns a title cased string
challenge = 'learn python in thirty days'
print(challenge.title())

#swapcase converts all lower case to upper case and vice-versa
challenge = 'LEArn pYthon In thiRTy days'
print(challenge.swapcase())

# startswith() checks whether the string starts with the specified string
challenge = 'Learn python in thirty days'
print(challenge.startswith('learn'))

challenge = 'Learn python in thirty days'
print(challenge.startswith('Learn'))
