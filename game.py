import sys
import random
import os
import time
import string
from grid import build_grid, print_grid
def starter_grid():
    if len(sys.argv) != 2 or sys.argv[1] not in ['2', '4', '6']:
        sys.stdout.write("Invalid grid size. Please specify 2, 4, or 6.\n")
        sys.exit(1)
    grid_size=int(sys.argv[1])
    grid= build_grid(grid_size)
    print_grid(grid)
def title():
    print("----------------------")
    print("|    Brain Buster    |")
    print("----------------------")
def main():
    title()
    starter_grid()

if __name__ == "__main__":
    main()