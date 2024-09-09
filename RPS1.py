import random

def play():
    user = input ("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice (['r', 'p', 's'])

    

    def is_win(player, computer):
        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            return True

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

print(play())
        
  