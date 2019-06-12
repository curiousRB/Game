#Need assitance
import time
import random
global your_score, ai_score

name = input('what is your name? ').capitalize()
print('nice to meet you', name)
print(" ")
time.sleep(1.5)
ready = input("Are you ready to play? type 'yes' or 'no': ").lower()

while len(ready) <= 0:
    if ready == 'yes':
        print('')
        print("Great! let's get started then")
        time.sleep(2)
        print('')
        print("We're gonna play rock, paper, scissors")
        time.sleep(1)
        print('')
        print('The first to 10 wins')
        time.sleep(1)
        print('')
        print("Let's test your luck!")
    elif ready == 'no':
        print("Well maybe next time")
        exit()
    else:
        ready = input("Are you ready to play? type 'yes' or 'no': ").lower()

your_score = str(0)
ai_score = str(0)
if your_score <= str(10) or ai_score <= str(10):
    def main(scores):
        global choice, your_score, ai_score
        your_score = str(0)
        ai_score = str(0)
        game = ['rock', 'paper', 'scissors']
        game_two = random.choice(game)
        time.sleep(1)
        print(' ')
        choice = input("Rock, Paper, or Scissors? Type 'r' for rock, 'p' for paper or 's' for scissors: ").lower()
        if game_two == 'rock' and choice == 'r':
            print('Draw! Try again')
            your_score += str(0)
            ai_score += str(0)
            time.sleep(1)
            print("You chose rock and your opponent chose", game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'paper' and choice == 'p':
            print('Draw! Try again')
            your_score += str(0)
            ai_score += str(0)
            time.sleep(1)
            print('You chose paper and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'scissors' and choice == 's':
            print('Draw! Try again')
            your_score += str(0)
            ai_score += str(0)
            time.sleep(1)
            print('You chose scissors and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'scissors' and choice == 'p':
            print('You lost! Try again')
            your_score += str(0)
            ai_score += str(1)
            time.sleep(1)
            print('You chose paper and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'rock' and choice == 's':
            print('You lost! Try again')
            your_score += str(0)
            ai_score += str(1)
            time.sleep(1)
            print('You chose scissors and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'paper' and choice == 's':
            print('You won! Try again')
            your_score += str(1)
            ai_score += str(0)
            print('You chose scissors and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'paper' and choice == 'r':
            print('You lost! Try again')
            your_score += str(0)
            ai_score += str(1)
            time.sleep(1)
            print('You chose rock and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'scissors' and choice == 'r':
            print('You won! Try again')
            your_score += str(1)
            ai_score += str(0)
            time.sleep(1)
            print('You chose rock and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)
        elif game_two == 'rock' and choice == 'p':
            print('You won! Try again')
            your_score += str(1)
            ai_score += str(0)
            print('You chose paper and your opponent chose', game_two, '.', 'The scores are', your_score + '-' + ai_score)

        else:
            while len(game_two) < 0 or len(choice) < 0:
                if len(game_two) < 0 or len(choice) < 0:
                    choice = input("Rock, Paper, or Scissors? Type 'r' for rock, 'p' for paper or 's' for scissors: ").lower()
  
      while your_score <= str(10) or ai_score <= str(10):
        main()
                    
    
main()
