'''Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
Input:
Enter the value of a
4
Enter the value of b
13
Output:
Player1 :
Please guess the number between 4 and 13
5
Wrong guess a greater number again
8
Wrong guess a smaller number again
6
Correct you took 3 trials to guess the number
Player 2:
Correct you took 7 trials to guess the number
Player 1 wins!'''
# def again():
#     import random
#     a = int(input("Enter a lower limit of the number:\n"))
#     b = int(input("Enter an upper limit of the number:\n"))
#     ran1 = random.randint(a+1,b-1)
#     ran2 = random.randint(a+1,b-1)
#     print(f"Guess the number between {a} and {b}")
#     attempts_player1 = 1
#     while(attempts_player1<=10):
#         print("\"Player1's turn\"")
#         Player1 = int(input("Enter you guess:\n"))
#         if Player1 < ran1:
#             print("wrong guess! Guess a bigger number.")
#         elif Player1 > ran1:
#             print("wrong guess! Guess a smaller number.")
#         elif Player1 == ran1:
#             print("Correct guess!")
#             print(f"You took {attempts_player1} attempts to guess the number")
#             break
#         print(f"You have {10 - attempts_player1} attempts left to guess the number. ")
#         attempts_player1 += 1
#     else:
#         print("Game over!You have exceed the number of attempts.")
#     attempts_player2 = 1
#     while(attempts_player2<=10):
#         print("\"Player2's turn\"")
#         Player2 = int(input("Enter you guess:\n"))
#         if Player2 < ran2:
#             print("wrong guess! Guess a bigger number.")
#         elif Player2 > ran2:
#             print("wrong guess! Guess a smaller number.")
#         elif Player2 == ran2:
#             print("Correct guess!")
#             print(f"You took {attempts_player2} attempts to guess the number")
#             break
#         print(f"You have {10 - attempts_player2} attempts left to guess the number. ")
#         attempts_player2 += 1
#     else:
#         print("Game over!You have exceed the number of attempts.")
#
#     print(f"Final score:\nPlayer1-Player2:{attempts_player1}-{attempts_player2}")
#     if attempts_player1 < attempts_player2:
#         print("Player1 won!")
#     elif attempts_player1 > attempts_player2:
#         print("Player2 won!")
#     elif attempts_player1 > 10 and attempts_player2 > 10:
#         print("Both lose as no one guess the correct number!")
#     elif attempts_player1 == attempts_player2:
#         print("Match tied!")
#     print(f"The number for Player1 was {ran1} and for Player2 was {ran2}")
# again()
# answer=input("Would you like to play again?: y or n\n")
# if answer== "y":
#     again()
# elif answer == "n":
#     exit()
# else:
#     print("Invalid input!")
import random
def GuessGame(a,b,actual):
    guess = int(input(f"Guess the number between {a} and {b}:\n"))
    attempts = 1
    while guess != actual:
        if guess > actual:
            guess = int(input("Enter a smaller number:\n"))
        else:
            guess = int(input("Enter a bigger number:\n"))
        attempts+=1
    print(f"You took {attempts} attempts to guess the number")
    return attempts
if __name__ == '__main__':
    a = int(input("Enter a  first number:\n"))
    b = int(input("Enter a  second number:\n"))
    actual1 = random.randint(a+1,b-1)
    print("Player1's turn:")
    g1 = GuessGame(a,b,actual1)
    print("Player2's turn:")
    actual2 = random.randint(a + 1, b - 1)
    g2 = GuessGame(a,b,actual2)
    if g1 > g2:
        print("Player2 won!")
    elif  g1 < g2:
        print("Player1 won!")
    elif g1 == g2:
        print("Tied!")
    print(f"The number for player1 was {actual1} and for player2 was {actual2}")














