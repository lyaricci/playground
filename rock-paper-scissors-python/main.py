import random

OPTIONS = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0


def get_computer_choice():
    computer_choice = random.choice(OPTIONS)
    return computer_choice


def get_player_choice():
    # Get the player input and prompt for a choice while it's not in the options list

    while True:
        player_choice = input(
            'Please, choose between rock, paper, or scissors: ').lower()

        if player_choice in OPTIONS:
            return player_choice
        else:
            print('Invalid choice!')


def play_round():
    # Play a round and update the scoreboard

    global player_score, computer_score

    player_selection = get_player_choice()
    computer_selection = get_computer_choice()

    print(
        f'You chose {player_selection} and the computer chose {computer_selection}')

    round_result = check_round_winner(player_selection, computer_selection)

    if round_result == 'You win!':
        player_score += 1
    elif round_result == 'Computer wins!':
        computer_score += 1

    print(f'Your score: {player_score}')
    print(f'Computer score: {computer_score}')


def check_round_winner(player_selection, computer_selection):
    # Check the round results

    results = {
        'rockscissors': 'You win!',
        'paperrock': 'You win!',
        'scissorspaper': 'You win!',
        'rockpaper': 'Computer wins!',
        'paperscissors': 'Computer wins!',
        'scissorsrock': 'Computer wins!',
        'rockrock': 'It\'s a tie!',
        'paperpaper': 'It\'s a tie!',
        'scissorsscissors': 'It\'s a tie!',
    }

    result_key = player_selection + computer_selection
    return results[result_key]


def play_game():
    # Executes the game 5 times

    for i in range(5):
        play_round()

    if player_score > computer_score:
        print('Congrats! You won the game!')
    elif computer_score > player_score:
        print('Sorry, the computer won the game :(')
    else:
        print('The game ended in a tie!')


play_game()
