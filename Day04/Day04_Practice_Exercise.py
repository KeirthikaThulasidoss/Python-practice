#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first = 'Thirty'
sec = 'Days'
third = 'Of'
fourth = 'Python'
string = first+' ' + sec+' ' + third+' ' + fourth
print(string)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
one = 'coding'
two = 'for'
three = 'all'
single_string = 'Coding' +' '+ 'For' + ' ' + 'All'
print(single_string)

#Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Company = 'Coding For All'
print(Company)
print(len(Company))
print(Company.upper())
print(Company.lower())
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())
print(len(Company))
#Cut(slice) out the first word of Coding For All string.
new=Company[7:15]
print(new)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
#Replace the word coding in the string 'Coding For All' to Python.
print(Company.find('Coding'))
print(Company.replace('Coding','Python'))

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
sentence = 'Python for Everyone'
print(sentence)
print(sentence.replace('Everyone' , 'All'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(Company.split(' '))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(','))

#What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.

charac = Company[0]
print(charac)

print(len(Company))
charac =Company[-1]
print(charac)

print(Company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
#Create an acronym or an abbreviation for the name 'Coding For All'.

PFE = 'Python For Everyone'
print(PFE)

CFA = 'Coding For All'
print(CFA)

#Use index to determine the position of the first occurrence of C in Coding For All.
#Use index to determine the position of the first occurrence of F in Coding For All.
print(Company.find('C'))
print(Company.find('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(Company.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start= sentence.find('because')
end = start + len('because because because')
print(sentence[start:end])

#Does 'Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
print(Company.startswith('Coding'))
print(Company.endswith('Coding'))

#   Coding For All      '  , remove the left and right trailing spaces in the given string.
Com = '    Coding For All          '
print(Com.strip(' '))

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_lib))

#Use the new line escape sequence to separate the following sentences.I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
