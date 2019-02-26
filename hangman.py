
def main():
    while True:
        word = list(input("What is player one's word or phrase?: "))
        if check_input(word) == True:
            break
        else:
            print("Not a valid word or phrase try again. ")
    
    placehold = ["-"] * len(word)
    previous = []
    strikes = 3

    while True:
        print(*placehold)
        while True:
            print("These are the letters you have guessed: ")
            print(*previous)
            guess = input("What is player two's guess? (one letter or space): ")
            if check_input(guess) == True:
                m = 0
                for i in previous:
                    if i == guess:
                        m +=1
                if m == 0:
                    previous.append(guess)
                    break
                else: 
                    print("You already guessed this letter try again")
            else:
                print("Not a valid letter or space (or you already guessed this letter) try again")
        c=0
        p=0
        for i in word:
            if guess == i:
                placehold[c] = guess
                p+=1
            c+=1

        if p == 0:
            strikes -= 1
            print("That was not correct you have " + str(strikes) +" guesses left. "  )
        else: 
            print("Correct")
        if strikes == 0:
            print("You lose!")
            break
        else:
            u = 0
            for i in placehold:
                if i == "-":
                    u += 1
            if u == 0:
                print("You guessed the word!")
                print(*placehold)
                break


def check_input(a):
    for i in a:
        if i.isalpha() or i.isspace():
            return True
            
main()



    
