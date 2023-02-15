#1.ACCESSING NUMBER
numbers = [9,10,2,5]
x = numbers[0]
print(x)

#2.ASSIGNINHG A DIFFERENT VALUE TO AN INDEX
numbers=[10,20,50,6]
numbers[2]=9
print(numbers)

#3.APPEND
cars=["BMW","Porshe","Jeep"]
cars.append("Toyota")
print(cars)

cars.remove("BMW")
print(cars)

#LENGTH
numbers = [3,5,6,77,8,8]
length = len(numbers)
print(length)

print(len("cars"))#we have 4 letters in the word 'cars'

repetitions = numbers.count(8)
print(repetitions)

numbers.reverse()
print(numbers)

#loop
numbers = [3,5,6,77,8,8,45,8]

for i in numbers:
    print(i)




