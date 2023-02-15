name = input("Enter a word:")
#A-Total number of characters
print(len(name))

#B-String multiplied by 10
print(name*10)

#C-First character of string
print(name[0])

#D-First 3 characters
print(name[:3])

#E-Last 3 letters
print(name[3:])

#F-The string backwards
print(name[::-1])

#G-7th character if string long enough and message otherwise
length = (len(name))

if length < 7:
    print("String has less than seven characters.")
else:
    print(name[6])

#H-String with 1st and last caharacters removed
str = name
str = str[:-1]
str = str[1:]
print(str)

#I-String in all caps
print(name.upper())

#J-Replace every 'a' with 'e'
print(name.replace("a","e"))


#2.A simple way to estimate the number of words in a string is to count the number of spaces in the string.
# Write a program that asks the user for a string and returns an estimate of how many words are in the string.

sentence = input("Write a sentence:")

count = 0
space = " "
