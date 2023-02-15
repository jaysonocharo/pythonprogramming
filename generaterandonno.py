from random import randint

nums = []

for i in range(5):
    number = randint(1,100)
    nums.append(number)
    
    for x in nums:
        print(x)
