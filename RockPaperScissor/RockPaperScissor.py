import random

def play():
    user = input("Whats's your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        print('It\'s a tie!')
    #r>s, p>r, s>p
    if is_win(user,computer):
        print('You won!')
    print('You lose!')
def is_win(player,comp):
    #return true if player wins
    #r>s, p>r, s>p
    if (player=='r' and comp=='s') or (player=='s' and comp=='p') or (player == "p" and comp=='r'):
        return True