import random

game = ['rock','paper','scissors']

computer_score = 0
user_score = 0    

while True:
    random_choice = random.choice(game)
    user_choice = input('Rock Paper or Scissors?\n').lower()
    
    if user_choice == 'rock' and random_choice == 'scissors' or user_choice  == 'paper' and random_choice == 'rock' or user_choice == 'scissors' and random_choice == 'paper':
        print('User Won')
        user_score += 1
        
    elif random_choice == 'rock' and user_choice == 'scissors' or random_choice == 'paper' and user_choice == 'rock' or random_choice =='scissors' and user_choice == 'paper':
        print('Computer Won')
        computer_score += 1
    else:
        print('You Typed Wrong Word')
        
        
    if user_score == 3:
        print(f'User Won The Game... User Score = {user_score} - Computer Score = {computer_score}')
        break
    elif computer_score ==3:
        print(f'Computer Won The Game... User Score = {user_score} - Computer Score = {computer_score}')
        break