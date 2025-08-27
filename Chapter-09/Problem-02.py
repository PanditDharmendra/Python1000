# importing rando module
import random as rm

def game():
    print("You are playing a number game!")
    score = rm.randint(1, 100)
 # fetch the high score
    with open("highscore.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

        print(f"Your score is {score}")
        if score > highscore:
            # Write this high score in the file
             with open ("highscore.txt", "w") as f: 
                    f.write(str(score))

        return score
game()