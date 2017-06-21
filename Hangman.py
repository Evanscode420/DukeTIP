import numpy
#This gets the game set up
words = ['microsoft', 'apple', 'banana', 'lamborghini', 'aston martin', ]
mistakes = 0

#This List holds the board
board = [[" "," "," ","-","-","-","-","-","-"," "],[" "," "," ","|"," "," "," "," ","|"," "],
         [" "," "," ","|"," "," "," "," "," "," "],[" "," "," ","|"," "," "," "," "," "," "],
         [" "," "," ","|"," "," "," "," "," "," "],[" "," "," ","|"," "," "," "," "," "," "],
         [" "," "," ","|"," "," "," "," "," "," "],[" "," "," ","|"," "," "," "," "," "," "],
         [" "," "," ","|"," "," "," "," "," "," "],[" ","-","-","-","-","-"," "," "," "," "]]

#Checks for One Player or Two Player
gmode = ''
while gmode != 'ONE' and gmode != 'TWO':
    gmode = raw_input('Do you want one player or two player? (Answer \'One\' or \'Two\'):')
    gmode = gmode.upper()
if gmode == 'ONE':
    word = numpy.random.choice(words)
elif gmode == 'TWO':
    print "Player One turn around!"
    word = raw_input("Player Two, enter your word:")
    for x in range(0,20):
        print "~"

#Prints the board
def print_board(board):
    counter = 0
    for row in board:
        print " ".join(board[counter])
        counter += 1

#Gets blanks at the bottom
blanks = []
for letter in word:
    blanks.append("_ ")

#Updates user progress var
prog = ''
def update_prog(prog):
    counter = 0
    for letter in blanks:
        prog = prog + blanks[counter]
        counter += 1

#Gets user guess and filters input
def get_input():
    valid_input = False
    while valid_input != True:
        user_guess = raw_input("Please enter a letter: ")
        if len(user_guess) != 1:
            print "Only one letter please!"
        else:
            user_guess.lower()
            valid_input = True
        return user_guess

#Checks user input against the word and changes board/blanks
def check_input(guess, mistakes):
    counter = 0
    no_hits = True
    while counter < len(word):
        if word[counter] == guess:
            blanks[counter] = guess
            counter += 1
            no_hits = False
        else:
            counter += 1
        update_prog(prog)
    if no_hits == False:
        print "Nice job!"
        print_board(board)
        print ' '.join(blanks)
    else:
        print "Try again!"
        if mistakes == 0:
            board[2][8] = "0"
        elif mistakes == 1:
            board[3][8] = '|'
        elif mistakes == 2:
            board[4][7] = "/"
            board[4][8] = "|"
            board[4][9] = "\\"
        elif mistakes == 3:
            board[5][8] = '|'
        elif mistakes == 4:
            board[6][7] = "/"
            board[6][9] = "\\"
        else:
            board[2][8] = ":"
            board[2][9] = ")"
            print "You're dead bud :("
        mistakes += 1
        print_board(board)
        print ' '.join(blanks)
    return mistakes

#Runs the game
print_board(board)
print ' '.join(blanks)
while word != prog and mistakes < 6:
    guess = get_input()
    mistakes = check_input(guess, mistakes)





