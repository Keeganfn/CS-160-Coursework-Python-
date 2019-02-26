nums = []
while True:    
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    num3 = input("Enter your third number: ")
    num4 = input("Enter your fourth number: ")
    num5 = input("Enter your fifth number: ")

    if num1 != num2 != num3 != num4 != num5:
        try:
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
            num4 = int(num4)
            num5 = int(num5)
            nums.append(num1)
            nums.append(num2)
            nums.append(num3)
            nums.append(num4)
            nums.append(num5)
            break
        except ValueError:
            print("That is not a valid input try again")
    else:
        print("That is not a valid input try again")

finalList = []
o = 0

for i in range(4):
    for i in range(len(nums)-1):

        a = nums[i-abs(o)]
        b = nums[i+1]

        if float(a) < float(b):
            finalList.append(a)
            o = 0
            if i == len(nums)-2:
                finalList.append(b)
        elif float(a) > float(b):
            finalList.append(b)
            o -= 1
            if i == len(nums)-2:
                finalList.append(a)
    nums.clear()
    nums = finalList[:]
    finalList.clear()
    o = 0
         
print("Your numbers ordered lowest to highest is " + str(nums))
print("The highest number is " + str(nums[4]))






        

