__author__ = 'Mac'


player1_greeting = 'Player 1: Choose between: rock, paper, scissors, spock, lizard '
player2_greeting = 'Player 2: Choose between: rock, paper, scissors, spock, lizard '

error_message = 'This isn\'t a valid answer'

player1_wins = 'Player 1 wins'
player2_wins = 'Player 2 wins'
nobody_wins = 'Nobody wins so it\'s a tie'

rock_paper = 'paper wraps around rock'
rock_scissors = 'rock crushes scissors'
rock_rock = 'rock can\'t crush rock'
paper_scissors = 'paper wraps around rock'
paper_paper = 'paper can\'t wrap around paper'
scissors_scissors = 'scissors can\'t cut scissors'


paper_spock = 'paper wraps around spock'
paper_lizard = 'lizard eats paper'

lizard_spock = 'lizard poisn spock'

spock_rock = 'spock vaporizes rock'
rock_lizard = 'rock curshes lizzard'

spock_scissors = 'spock smashes scissors'
lizard_scissors = 'scissors cuts lizard'

valid_answers = [
    'rock',
    'paper',
    'scissors',
    'spock',
    'lizard'
]

player_1 = raw_input(player1_greeting)
while player_1 not in valid_answers:
    print error_message
    player_1 = raw_input(player1_greeting)

player_2 = raw_input(player2_greeting)
while player_2 not in valid_answers:
    print error_message
    player_2 = raw_input(player2_greeting)


if player_1 == 'rock':
    if player_2 == 'scissors':
        print rock_paper, player1_wins
    if player_2 == 'paper':
        print rock_paper, player2_wins
    if player_2 == 'rock':
        print rock_rock, nobody_wins
    if player_2 == 'lizard':
        print rock_lizard, player1_wins
    if player_2 == 'spock':
        print spock_rock, player2_wins

if player_1 == 'scissors':
    if player_2 == 'rock':
        print rock_paper, player2_wins
    if player_2 == 'paper':
        print paper_scissors, player1_wins
    if player_2 == 'scissors':
        print scissors_scissors, nobody_wins
    if player_2 == 'lizard':
        print lizard_scissors, player1_wins
    if player_2 == 'spock':
        print spock_scissors, player2_wins

if player_1 == 'paper':
    if player_2 == 'paper':
        print paper_paper, nobody_wins
    if player_2 == 'rock':
        print rock_paper, player1_wins
    if player_2 == 'scissors':
        print paper_scissors, player2_wins
    if player_2 == 'lizard':
        print paper_lizard, player2_wins
    if player_2 == 'spock':
        print paper_spock, player1_wins


if player_1 == 'lizard':
    if player_2 == 'paper':
        print paper_lizard, player1_wins
    if player_2 == 'rock':
        print rock_lizard, player2_wins
    if player_2 == 'scissors':
        print lizard_scissors, player2_wins
    if player_2 == 'spock':
        print lizard_spock, player1_wins

if player_1 == 'spock':
    if player_2 == 'paper':
        print paper_spock, player2_wins
    if player_2 == 'rock':
        print spock_rock, player2_wins
    if player_2 == 'scissors':
        print spock_scissors, player1_wins
    if player_2 == 'lizard':
        print lizard_spock, player2_wins

