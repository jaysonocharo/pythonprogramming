#my first python list
#names = ["python","java","c++"]
numbers = [45,67,34,76,23,45]

#print(len(numbers)) #get the length of my list
#numbers.append(90)
for i in range(len(numbers)):
    
    print(numbers[i])

#print("/n")
#LIST METHODS
 
#print(numbers.index(67))
#print(names.index("java")) 
#Index
#Append
#SORT - arranges the list in ascending order

numbers.sort()#sort the list
print(numbers)

#COUNT - returns number of times an element occurs in a list

print(numbers.count(67))

#POP - removes an element at a given index and returns that element

print(numbers.pop(2))
#INSERT - inserts an element x at an index y

#numbers.insert(2,100)
print(numbers)
#REMOVE - removes the first element from the list

numbers.remove(67)
print(numbers)

#TIPS AND TRICKS FOR LISTING:

#Multiplying a list...

zeros = [2]*21
print(zeros)

#adding a list
list1 = [74,29]
list2 = [64,85]
list1 + list2
list3 = list1 + list2
print(list1 + list2)

#to split a list
list3[2:]
print(list3[1:3])

#creating lists
for i in range(10):
    #insert elements
    numbers.append(i)

for i in range (len(numbers)):
    print(numbers[i])
    
 #create a list for even numbers
    
even_nums = []
for num in range(20):
    if(num % 2) == 0:
        even_nums.append(num)
    
for i in even_nums:
    print(even_nums[i])
    