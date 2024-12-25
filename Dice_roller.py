 # VIRTUAL DICE ROLLER
import random

def roll_dice():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    return die1,die2

def display_result(die1, die2):
    print(f"You rolled a {die1} and a {die2}.")
    print(f"Your total is {die1 + die2}.")

def main():
    while True:
        print("\n Virtual Dice Roller")
        roll=input("Press ENTER to roll the dice or 'q' to quit: " )
        if roll.lower() == 'q':
            print("Exiting the dice roller.")
            break
        die1, die2 = roll_dice()
        display_result(die1 , die2)
        
if __name__ == "__main__":
    main()
    
        
