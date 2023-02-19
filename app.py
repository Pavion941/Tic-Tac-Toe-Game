#DEFINE VARIABLES (better on one line, needs to be fixed)
one = ' '
two = ' '
three = ' '
four = ' '
five = ' '
six = ' '
seven = ' '
eight = ' '
nine = ' '
space = ' '
bar = ' | '

def print_choices():
      print('  CHOICES')
      print(' 1 | 2 | 3 \n'
            '---+---+---\n'
            ' 4 | 5 | 6 \n'
            '---+---+---\n'
            ' 7 | 8 | 9 \n')

def print_board():
      # print board
      print('CURRENT BOARD')
      print(one, bar, two, bar, three)
      print('---+-----+---')
      print(four, bar, five, bar, six)
      print('---+-----+---')
      print(seven, bar, eight, bar, nine)

def X_choice():
      # ask for player 1 input
      print('Player 1 -- X')
      choice = input("Type the number for your choice.  ")

      if choice == '1':
            one = 'X'
      elif choice == '2':
            two = 'X'
      elif choice == '3':
            three = 'X'
      elif choice == '4':
            four = 'X'
      elif choice == '5':
            five = 'X'
      elif choice == '6':
            six = 'X'
      elif choice == '7':
            seven = 'X'
      elif choice == '8':
            eight = 'X'
      elif choice == '9':
            nine = 'X'
      print_board()

def O_choice():
      # ask for player 2 input
      print('Player 2 -- O')
      choice = input("Type the number for your choice.  ")

      if choice == '1':
            one = 'O'
      elif choice == '2':
            two = 'O'
      elif choice == '3':
            three = 'O'
      elif choice == '4':
            four = 'O'
      elif choice == '5':
            five = 'O'
      elif choice == '6':
            six = 'O'
      elif choice == '7':
            seven = 'O'
      elif choice == '8':
            eight = 'O'
      elif choice == '9':
            nine = 'O'
      print_board()


#use variable for each place in tic tac toe board
#set vairable to blank or nothing
#replace variable with X or O when space is selected for choice
#remove choice from options after every turn
#check for winners by if/compare statement on every row combination
#if there is winner print contents of winning tile and end game
#maybe pass choice in to get functions working or return it

#START PROGRAM
print_choices()
# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 1 input
print('Player 1 -- X')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'X'
elif choice == '2':
      two = 'X'
elif choice == '3':
      three = 'X'
elif choice == '4':
      four = 'X'
elif choice == '5':
      five = 'X'
elif choice == '6':
      six = 'X'
elif choice == '7':
      seven = 'X'
elif choice == '8':
      eight = 'X'
elif choice == '9':
      nine = 'X'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 2 input
print('Player 2 -- O')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'O'
elif choice == '2':
      two = 'O'
elif choice == '3':
      three = 'O'
elif choice == '4':
      four = 'O'
elif choice == '5':
      five = 'O'
elif choice == '6':
      six = 'O'
elif choice == '7':
      seven = 'O'
elif choice == '8':
      eight = 'O'
elif choice == '9':
      nine = 'O'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 1 input
print('Player 1 -- X')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'X'
elif choice == '2':
      two = 'X'
elif choice == '3':
      three = 'X'
elif choice == '4':
      four = 'X'
elif choice == '5':
      five = 'X'
elif choice == '6':
      six = 'X'
elif choice == '7':
      seven = 'X'
elif choice == '8':
      eight = 'X'
elif choice == '9':
      nine = 'X'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 2 input
print('Player 2 -- O')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'O'
elif choice == '2':
      two = 'O'
elif choice == '3':
      three = 'O'
elif choice == '4':
      four = 'O'
elif choice == '5':
      five = 'O'
elif choice == '6':
      six = 'O'
elif choice == '7':
      seven = 'O'
elif choice == '8':
      eight = 'O'
elif choice == '9':
      nine = 'O'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 1 input
print('Player 1 -- X')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'X'
elif choice == '2':
      two = 'X'
elif choice == '3':
      three = 'X'
elif choice == '4':
      four = 'X'
elif choice == '5':
      five = 'X'
elif choice == '6':
      six = 'X'
elif choice == '7':
      seven = 'X'
elif choice == '8':
      eight = 'X'
elif choice == '9':
      nine = 'X'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 2 input
print('Player 2 -- O')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'O'
elif choice == '2':
      two = 'O'
elif choice == '3':
      three = 'O'
elif choice == '4':
      four = 'O'
elif choice == '5':
      five = 'O'
elif choice == '6':
      six = 'O'
elif choice == '7':
      seven = 'O'
elif choice == '8':
      eight = 'O'
elif choice == '9':
      nine = 'O'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 1 input
print('Player 1 -- X')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'X'
elif choice == '2':
      two = 'X'
elif choice == '3':
      three = 'X'
elif choice == '4':
      four = 'X'
elif choice == '5':
      five = 'X'
elif choice == '6':
      six = 'X'
elif choice == '7':
      seven = 'X'
elif choice == '8':
      eight = 'X'
elif choice == '9':
      nine = 'X'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 2 input
print('Player 2 -- O')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'O'
elif choice == '2':
      two = 'O'
elif choice == '3':
      three = 'O'
elif choice == '4':
      four = 'O'
elif choice == '5':
      five = 'O'
elif choice == '6':
      six = 'O'
elif choice == '7':
      seven = 'O'
elif choice == '8':
      eight = 'O'
elif choice == '9':
      nine = 'O'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)

# ask for player 1 input
print('Player 1 -- X')
choice = input("Type the number for your choice.  ")

if choice == '1':
      one = 'X'
elif choice == '2':
      two = 'X'
elif choice == '3':
      three = 'X'
elif choice == '4':
      four = 'X'
elif choice == '5':
      five = 'X'
elif choice == '6':
      six = 'X'
elif choice == '7':
      seven = 'X'
elif choice == '8':
      eight = 'X'
elif choice == '9':
      nine = 'X'

# print board
print('CURRENT BOARD')
print(one, bar, two, bar, three)
print('---+-----+---')
print(four, bar, five, bar, six)
print('---+-----+---')
print(seven, bar, eight, bar, nine)