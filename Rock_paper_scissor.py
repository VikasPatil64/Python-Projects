import random
print("Welcome to rock, paper and scissors game !")
while True:
    user_choice = input("Enter your choice [rock/paper/scissors] :")
    computer_choice = random.choice(['rock', 'paper','scissor'])
    
    print("User choice :",user_choice)
    print("Computer choice : ", computer_choice)
    
    if user_choice==computer_choice:
        print("Game tied")

    elif (user_choice=='paper' and computer_choice=='rock') or\
        (user_choice=='rock' and computer_choice=='scissor') or\
        (user_choice=='scissor' and computer_choice=='paper') :
            print("User Wins !")
        
    else:
        print("Computer wins !")
        
    play_again = input("Do you wish to play again (yes/no)")
    if play_again!='yes' :
        print("Thank you for playing")
        break
   