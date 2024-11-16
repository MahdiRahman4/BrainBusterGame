import sys
import random
import os
import time
import string
from grid import *
#global variables
global guess_count
guess_count = 0
cell1 = None
cell2 = None
permanent_cell = None
uncover_count=0
cell=None

#starter grid is for the initialization of the grid which will be used in the game, it checks for the correct size input and shuts down the process if the correct size is not given
def starter_grid():
    if len(sys.argv) != 2 or sys.argv[1] not in ['2', '4', '6']:
        sys.stdout.write("Invalid grid size. Please specify 2, 4, or 6.\n")
        sys.exit(1)
    size = int(sys.argv[1])
    grid = Grid(size)
    return grid
#helper function to reduce the amount of times i remake that
def title():
    print("----------------------")
    print("|    Brain Buster    |")
    print("----------------------\n")
#helper function to reduce the amount of times i remake that
def options():
    print("\n1. Let me select two elements\n2. Uncover one element for me\n" +
          "3. I give up - reveal the grid\n4. New game\n5. Exit\n")
#Since python does not have switch cases and i like switches, i made a pseudo-switch case
def selection_switch_case(grid):
    #calling global variable
    global uncover_count
    guess_made = False 
#checks if the input is a number or not, if its not it reprompts
    while True:
        try:
            selection = int(input("Select: "))
        except ValueError:
            print("Please input a number")
            continue
        else:
            break
# if the selection is not valid but is a number, it reprompts
    while selection not in [1, 2, 3, 4, 5]:
        print("Invalid input. Try again")
        try:
            selection = int(input("Select: "))
        except ValueError:
            continue
#this is for guesses
    if selection == 1:  
        #guess returns cell1,cell2 so im just holding it in a variable
        cell1, cell2 = guess(grid)
        #split up the first char and second char in the string and flips them because row comes before char
        row1, col1 = int(cell1[1]), ord(cell1[0]) - 97
        row2, col2 = int(cell2[1]), ord(cell2[0]) - 97

        grid.reveal_number(row1, col1)
        grid.reveal_number(row2, col2)

        title()
        grid.display()
        options()
#if the two cells match, checks if the game is done, if the game is done and uncover_count is the same as the amount of numbers in the grid, the po\
        if grid.hidden_grid[row1][col1] == grid.hidden_grid[row2][col2]:  
            guess_made = True  
            if gameDone(grid):  
                if uncover_count == grid.size * grid.size and not guess_made:  
                    print("\nYou cheated - Loser! Your score is 0!")
                else:
                    score = calcScore(grid)
                    print(f"\nOh Happy Day. You've won!! Your score is: {score}")
                sys.exit(0)
            clear(grid)
        else:
            time.sleep(2)
            grid.hide_number(row1, col1)
            grid.hide_number(row2, col2)
            clear(grid)

    elif selection == 2:  
        permanent_cell = uncover(grid)
        row, col = int(permanent_cell[1]), ord(permanent_cell[0]) - 97
        grid.reveal_number(row, col)

        
        all_revealed = all('X' not in row for row in grid.grid)

        if all_revealed:
            grid.display()  
            if uncover_count == grid.size * grid.size and not guess_made:  
                print("\nYou cheated - Loser! Your score is 0!")
            else: 
                #if no cheat print this 
                score = calcScore(grid)
                print(f"\nOh Happy Day. You've won!! Your score is: {score}")
            sys.exit(0)

        clear(grid)

    elif selection == 3:
        grid.display_hidden()
        sys.exit(0)
    elif selection == 4:
        restart_game()
    elif selection == 5:
        sys.exit(0)

#guess logic, returns the cells to be guessed
def guess(grid):
    global guess_count
    global cell
    cell1 = input("Enter cell coordinates (e.g., a0): ")
    cell=cell1
    validate_cell(cell,grid)
    cell2 = input("Enter cell coordinates (e.g., a0): ")
    cell=cell2
    validate_cell(cell,grid)
    guess_count += 1
    return cell1, cell2
#uncover logic, returns the cell to be uncovered
def uncover(grid):
    global guess_count
    global uncover_count
    global cell
    permanent_cell = input("Enter cell coordinates (e.g., a0): ")
    cell=permanent_cell
    validate_cell(cell,grid)
    guess_count += 2
    uncover_count+=1
    return permanent_cell
#validates most error possibilities
def validate_cell(cell,grid):
    while not (len(cell)==2):
        print("Invalid input. Try again")
        cell = input("Enter cell coordinates (e.g., a0): ")
    while not cell[1].isdigit():
        print("Input error: row must be a number. Please try again.")
        cell = input("Enter cell coordinates (e.g., a0): ")

    while(cell[0] > chr(96 + grid.size) or cell[0] < chr(97)):
        print("Input error: column entry is out of range for this grid. Please try again.")
        cell = input("Enter cell coordinates (e.g., a0): ")

    while(int(cell[1]) >= grid.size or int(cell[1]) < 0):
        print("Input error: row entry is out of range for this grid. Please try again.")
        cell = input("Enter cell coordinates (e.g., a0): ")
    return cell
#helper function to ease typing
def always_on_screen(grid):
    title()
    grid.display()
    options()
    selection_switch_case(grid)
#clears terminal and sets main screen
def clear(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    always_on_screen(grid)
#checks if game is done by checking if board is fully revealed
def gameDone(grid):
    
    for i in range(grid.size):
        for j in range(grid.size):
            if grid.grid[i][j] == 'X':
                return False
    return True
#restarts the game
def restart_game():
    global guess_count
    guess_count = 0  
    os.system('cls' if os.name == 'nt' else 'clear')  
    main()  
    #calculates score with the formula given
def calcScore(grid):
    if(uncover_count==grid.size*grid.size):
        score=0
    optimal_guesses = (grid.size * grid.size) / 2.0
    score = (optimal_guesses / guess_count) * 100
    score = round(score, 2)
    return score
#runs the game
def main():
    title()
    grid = starter_grid()
    grid.display()
    options()
    
    while True:
        selection_switch_case(grid)

if __name__ == "__main__":
    main()