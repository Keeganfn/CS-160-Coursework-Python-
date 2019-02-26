import math
def programmerCalculator():
    while True:
        progInput = input("Enter an unsigned decimal number: ")
        if progInput.isdigit() and (int(progInput) >= 0):
            break
    progInput = int(progInput)
    binaryLength = int(math.log(progInput,2))
    output = []
    inputCheck = 0
    while binaryLength >= 0:
        if ((2 ** binaryLength) <= progInput) and (((2 ** binaryLength) + inputCheck) <= progInput):
            output.append(1)
            inputCheck += (2 ** binaryLength)
            binaryLength-=1
        else:
            output.append(0)
            binaryLength-=1
    print(*output)
    while True:
        newChoice = input("do you want to do another calcuation or go to different mode? (ac or dm): ")
        if newChoice == "ac":
            programmerCalculator()
            break
        elif newChoice == "dm":
            break

#programmerCalculator()

def scientificCalculator():
    finalAnswer = 0

    while True:
        operand = input("What math operation would you like to perform (+,-,**,*,/): ")
        number1 = float(input("Enter the first number of the operation: "))
        number2 = float(input("Enter the second number of the operation: "))
        if operand == "+" or operand == "-" or operand == "**" or operand == "*" or operand == "/":
            break
    if operand == "+":
        finalAnswer = number1 + number2
    elif operand == "-":
        finalAnswer = number1 - number2
    elif operand == "**":
        finalAnswer = number1 ** number2
    elif operand == "*":
        finalAnswer = number1 * number2
    elif operand == "/":
        finalAnswer = number1 / number2
    print("The answer is: " + str(finalAnswer))
    while True:
        newChoice = input("do you want to do another calcuation or go to different mode? (ac or dm): ")
        if newChoice == "ac":
            scientificCalculator()
            break
        elif newChoice == "dm":
            break
#scientificCalculator()

while True:
    calcChoice = input("Do you want Scientific or Programmer calculator (Type either s or p): ")
    if calcChoice == "s" or calcChoice == "S":
        scientificCalculator()
    elif calcChoice == "p" or calcChoice == "P":
        programmerCalculator()