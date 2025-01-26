import random  

def get_choice(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"
    else:
        return "Invalid Choice"
    
def rock_paper_scissors():
    print("Welcome to Rock🪨, Paper📄, Scissor Game✂️")
    print("-" * 30)
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors!")
    while True:
        try:
            computer_choice = int(random.choice("123"))
            player_choice = int(input("Enter your choice: "))
            
            print("\nComputer Chose: ",get_choice(computer_choice))
            print("\nPlayer Chose: ",get_choice(player_choice))
            
            if player_choice == computer_choice:
                print("\nIt is a tie")
            elif (player_choice == 1) and (computer_choice == 3) or \
                 (player_choice == 3) and (computer_choice == 2) or \
                 (player_choice == 2) and (computer_choice == 1):
                     print("Congratulations. You win!")      
            else:
                print("Sorry. You Lose!")
        except ValueError:
            print("Please, enter a numeric value.")
        quit = input("\nDo you wish to continue. (Y/N): ").lower()
        if quit == "yes" or quit == "y":
            continue
        else:
            break
        
rock_paper_scissors()