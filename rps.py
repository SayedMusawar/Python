import random
rounds = 1
while rounds != 5:

    print("----- Rock Paper Scissor Game -----")
    print(f"----- Round {rounds} -----")

    player_choice = str(input("Enter your choice. Rock,Paper, Scissor: ")).capitalize()

    computer_Choice = random.randrange(0,30)
    if computer_Choice in range(0,10):
        computer_Choice = 'Rock'
    elif computer_Choice in range(10,20):
        computer_Choice = 'Paper'
    else:
        computer_Choice = 'Scissor'

    print(f"Computer Chose: {computer_Choice}")

    if player_choice not in ['Rock','Paper','Scissor']:
        print("Invalid choice! Please enter Rock/Paper/Scissor")
        continue

    if computer_Choice == player_choice:
        print("Draw...")
    elif (computer_Choice == 'Rock' and player_choice == 'Paper') or (computer_Choice == 'Paper' and player_choice == 'Scissor') or (computer_Choice == 'Scissor' and player_choice == 'Rock'):
        print("Player wins")
    else:
        print("Computer wins")
    rounds = rounds + 1
