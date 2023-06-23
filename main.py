from random import randint

def play_game():
    winning_number = randint(1,100)
    intents = range(8)
    accert = False

    for intent in intents:
        user_number = int(input('Type a number between 1 and 100: '))
        if user_number < winning_number:
            print('Sorry, the number is less than the secret number')
        elif user_number > winning_number :
            print('Oops.. your number is greater')
        elif user_number < 1 or user_number > 100:
            print('Remember that you can use numbers between 1 and 100 only.')
        else:
            print(f'Excellent, the winning number is {winning_number}, it took {intent + 1} intents.')
            accert = True
            break
    return (accert, winning_number)

play = True

print('Welcome to guess the number, you have 8 intents to win. Lets see if you can hit the number and how many intents you need 😉')

while play:
    accert, winning_number = play_game()
    if not accert: 
        print(f'Sorry you could not guess the number, the winning number is {winning_number}, please try again')
    play = input('Do you want to play again? (s/n): ').lower() == 's'
else:
    print('End game')

    