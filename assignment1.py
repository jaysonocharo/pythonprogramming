#user_list.py
nums = []

list_length = 5

for i in range(list_length):
    number = eval(input("Enter number: "))
    nums.append(number)
    #print(nums)
    nums.sort()