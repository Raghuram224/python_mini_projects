import random

attemt_list=[]

def show_score():
    if len(attemt_list)<=0:
        print("There is no high score!")
    else:
        print(" Recentoly played high score is {}".format(min(attemt_list)))

def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    # Where the show_score function USED to be
    attempts = 0
    show_score()


    while wanna_play=="yes":
        try:

            guess=input("pick a number between 1,10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess)==random_number:
                print("oh nice you got it")
                attempts+=1
                attemt_list.append(attempts)
                print("you took ({}) attempts".format(attempts))
                play_again=input("if you want to play again Enter(yes/no)")
                attempts=0
                show_score()
                random_number=int(random.randint(1,10))
                if play_again=="no":
                    print("ok come and play next time")
                    show_score()
                    break
            elif int(guess)> random_number:
                print("random number should be lower")
                attempts+=1
            elif int(guess)< random_number:
                print("random value should be higher")
                attempts+=1
        except ValueError as err:
            print("ohh thats not a valid value")
            print("{}".format(err))
    else:
        print("that's  cool")
if __name__=="__main__":
    start_game()
