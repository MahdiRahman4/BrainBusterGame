import sys
import random
import os
import time
import string
from grid import *
cell1=None
cell2=None
permanent_cell=None
guess_count=0
def starter_grid():
    if len(sys.argv) != 2 or sys.argv[1] not in ['2', '4', '6']:
        sys.stdout.write("Invalid grid size. Please specify 2, 4, or 6.\n")
        sys.exit(1)
    size= int(sys.argv[1])
    grid=Grid(size)
    return grid
def title():
    print("----------------------")
    print("|    Brain Buster    |")
    print("----------------------\n")
def options():
    print("\n1. Let me select two elements\n2. Uncover one element for me\n"+
          "3. I give up - reveal the grid\n4. New game\n5. Exit\n")
def selection_switch_case(grid):
    global valid_guess_made
    while True: 
        try:
            selection = int(input("Select:"))
        except ValueError:
            print("Please input a number")
            continue
        else:
            break
    while (selection !=1 and selection !=2 
        and selection!=3 and selection!=4 and selection!=5):
            print("Invalid input. Try again")
            selection = input("Select: ")
    
    if (selection==1):
        cell1, cell2 = guess(grid)
        row1, col1 = int(cell1[1]), ord(cell1[0])-97
        row2, col2 = int(cell2[1]), ord(cell2[0])-97
        
        grid.reveal_number(row1, col1)
        grid.reveal_number(row2, col2)
        
        title()
        grid.display()
        options()
        
        if grid.hidden_grid[row1][col1] == grid.hidden_grid[row2][col2]:
            valid_guess_made = True 
            return
        else:
            time.sleep(2)
            grid.hide_number(row1, col1)
            grid.hide_number(row2, col2)
            clear(grid)
            
    elif (selection==2):
        permanent_cell = uncover(grid)
        row, col = int(permanent_cell[1]), ord(permanent_cell[0])-97
        grid.reveal_number(row, col)
        clear(grid)
    elif(selection==3):
        grid.display_hidden()
        sys.exit(1)
    elif (selection==4):
        reset_game(grid)
    elif(selection==5):
        sys.exit(1)
def guess(grid):
    global guess_count
    cell1 =input("Enter cell coordinates (e.g., a0): ") 
    
    while not cell1[1].isdigit():
        print("Input error: row must be a number. Please try again.")
        cell1 = input("Enter cell coordinates (e.g., a0): ")
        
    while(cell1 [0]>chr(102) or cell1 [0]<chr(97)):
        print("Input error: column entry is out of range for this grid. Please try again.")
        cell1 =input("Enter cell coordinates (e.g., a0): ")
        
    while(int(cell1[1])>5 or int(cell1[1])<0):
        print("Input error: row entry is out of range for this grid. Please try again.")
        cell1 =input("Enter cell coordinates (e.g., a0): ")
        
    cell2 = input("Enter cell coordinates (e.g., a0): ")
    
    while not cell2[1].isdigit():
        print("Input error: row must be a number. Please try again.")
        cell2 = input("Enter cell coordinates (e.g., a0): ")

    while(int(cell2[1])>5 or int(cell2[1])<0):
        print("Input error: row entry is out of range for this grid. Please try again.")
        cell2 =input("Enter cell coordinates (e.g., a0): ")
    guess_count+=1
    return cell1,cell2
def uncover(grid):
    global guess_count
    permanent_cell =input("Enter cell coordinates (e.g., a0): ") 
    
    while not permanent_cell[1].isdigit():
        print("Input error: row must be a number. Please try again.")
        permanent_cell = input("Enter cell coordinates (e.g., a0): ")
        
    while(permanent_cell [0]>chr(102) or permanent_cell [0]<chr(97)):
        print("Input error: column entry is out of range for this grid. Please try again.")
        permanent_cell =input("Enter cell coordinates (e.g., a0): ")
        
    while(int(permanent_cell[1])>5 or int(permanent_cell[1])<0):
        print("Input error: row entry is out of range for this grid. Please try again.")
        permanent_cell =input("Enter cell coordinates (e.g., a0): ")
    guess_count+=2
    return permanent_cell
def always_on_screen(grid):
    title()
    grid.display()
    options()
    selection_switch_case(grid)
def clear(grid):
    os.system('cls')
    always_on_screen(grid)
def gameDone(grid):
    for i in range(grid.size):
        for j in range(grid.size):
            if grid.grid[i][j] != grid.hidden_grid[i][j]:
                return False
    return True

def reset_game(grid):
    global guess_count, valid_guess_made
    guess_count = 0
    valid_guess_made = False
    new_grid = Grid(grid.size)
    grid.grid = new_grid.grid
    grid.hidden_grid = new_grid.hidden_grid
    clear(grid)
def main():
    global guess_count, valid_guess_made
    title()
    grid = starter_grid()
    grid.display()
    options()
    while True:
        selection_switch_case(grid)
        if(gameDone(grid)):
            break
    
    if not valid_guess_made:
        print("You cheated - Loser! Your score is 0!")
    else:
        print("Oh Happy Day. You've won!! Your score is: ", end='')
        print(calcScore(grid))

def calcScore(grid):
    optimal_guesses = (grid.size * grid.size)/2.0
    score = (optimal_guesses/guess_count)*100
    score = round(score, 2)
    return score

if __name__ == "__main__":
    main()