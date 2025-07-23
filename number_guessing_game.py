import random
computer_number = random.randrange(0,100)
user_guess = int(input("Enter your guess between 0 and 100: "))
count = 1
while user_guess!= computer_number:
    if computer_number > user_guess:
        print("Oops!! your guess is Low. Higher your guess")
    else:
        print("Oop!! your guess is High. Lower your guess.")
    count +=1
    user_guess = int(input("Enter your guess between 0 and 100: "))
print("Congratulation!! You guessed correct")
print(f"Number of attempts: {count}")