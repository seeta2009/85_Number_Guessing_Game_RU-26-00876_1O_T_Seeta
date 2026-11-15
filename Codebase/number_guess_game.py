import random
 
def generate_number():
    """Generate a random number between (1 - 100)."""
    return random.randint(1,100)

 
def enter_valid_input():
    """Take input and validate it."""
    while True:
        try:
            guess = int(input("ENTER  YOUR GUESSED NUMBER (1 - 100): "))
            
            if guess < 1 or guess > 100:
                
                print("Out of range. Enter a number between 1 and 100.")

            else:
                return guess

        except ValueError:
            print("Invalid input. Enter a whole number.")

        print("Attempts Left: 5, No attempts lost")


def play_game():
     
    secret_number = generate_number()
    max_attempts = 5
    attempts_used = 0

    print("=====================================")
    print("========NUMBER GUESSING GAME===========")
    print("=======================================")
    print("YOU HAVE TO SELECT A NUMBER BETWEEN (1 - 100)")
    print("----YOU HAVE 5 ATTEMPTS TO GUESS THE NUMBER----")
    print("======FIRST ROUND OF NUMBER GUESSING GAME STARTS HERE!!======")

    while attempts_used < max_attempts:
        guess = enter_valid_input()

        attempts_used += 1
        attempts_left = max_attempts - attempts_used

        if guess < secret_number:
            print("Too Low! Try a higher number.")

        elif guess > secret_number:
            print("Too High! Try a lower number.")

        else:
            print("===CONGRACULATIONS!! YOU GUESSED IT.===")
            print("Secret Number = ", secret_number)
            print("Attempts Used: ", attempts_used)
            return

        print("Attempts Remaining: ", attempts_left)

    print("GAME OVER! The secret number was: ", secret_number)
    

def main():
    """CONTROL THE COMPLETE GAME!!"""

    print("===WELCOME TO THE NUMBER GUESSING GAME!===")

    while True:
        play_game()

        play_again = input(
            "/n Do You Want To Play Again? (yes/no): "
        ).strip().lower()

        if play_again == "yes":
            print(" STARTING A NEW GAME!!")

        elif play_again == "no":
            print(" THANKYOU FOR PLAYING THE GAME")

        else:
            print("Invalid Input! Please enter yes or no.")


#To again start the whole program
if __name__ == "__main__":
    main()

