
def main():
    #user chooses between summation and integration
    while True:
        choice = input("Do you want to do Summation or Integration? (S or I): ")
        if choice.lower() == "s":
            summation()
        elif choice.lower() == "i":
            integration()

def checkinput(a,b,c):
    #checks to see if inputs are digits
    if a.lstrip("-").isdigit() and b.lstrip("-").isdigit() and c.lstrip("-").isdigit():
        return True
    else:
        return False


def summation():
    while True:
        #gets values from the user and checks for valid inputs
        lowerb = input("What is your starting point?: ")
        upperb = input("What is your ending point?: ")
        if checkinput(lowerb, upperb, "0") == True and float(upperb) >= float(lowerb):
            break
        else:
            print("That is not a valid number combination, try again")
    lowerb = float(lowerb)
    upperb = float(upperb)
    total = 0
    #calculation
    while lowerb <= upperb:
        total += (lowerb ** 2)
        lowerb += 1
    print("The answer is: " + str(total))

def integration():
    while True:
        #getting values and checking them for validity
        lowerb2 = input("What is your lower bound: ")
        upperb2 = input("What is your upper bound: ")
        n2 = input("What is the number of trapezoids or rectangles (must be a positive number): ")
        if checkinput(lowerb2, upperb2, n2) == True and float(lowerb2) < float(upperb2) and float(n2) >= 0:
            while True:
                #user chooses which method
                triorrec = input("Do you want to use the trapezoid method or the rectangle method? (t or r): ")
                if triorrec.lower() == "r":
                    y = float(upperb2) - float(lowerb2)
                    x = float(lowerb2)
                    j = float(upperb2)
                    total = 0
                    #rectangle calculations
                    while x < j:
                        width = (y) / float(n2)
                        height = ((x + (x+width))/2)**2
                        print(height)
                        x += width
                        total += (width * height)
                        print("Total: " + str(total))
                    break
                elif triorrec.lower() == "t":
                    difference = float(upperb2) - float(lowerb2)
                    x = float(lowerb2)
                    j = float(upperb2)
                    total = 0  
                    #trapezoid calculations
                    while  x < j:
                        width = difference / float(n2)
                        height = ((x**2) + ((x+width)**2))/2
                        x+= width
                        total += (width * height)
                    print("Total: " + str(total))                  
                    break
                else:
                    print("That is not a valid input, try again")
        else: 
            print("That is not a number combination, try again")
        break

main()