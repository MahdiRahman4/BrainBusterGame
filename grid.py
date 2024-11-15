import random
#object oriented file
class Grid:
    
    #initialize grid with properties
    def __init__(self,size):
        self.size = size
        self.grid= [['X'] * size for _ in range(size)]
        self.hidden_grid=self.make_hidden_grid()
        #makes the hidden grid , meaning it generates the
    def make_hidden_grid(self):
        hidden_grid= [[None]* self.size for _ in range(self.size)]
        index=0
        temp_list= [0]*(self.size**2)
        for i in range(0, len(temp_list), 2):
            temp  = random.randint(0,9)
            temp_list[i],temp_list[i+1]=temp,temp
        random.shuffle(temp_list)
        for j in range(self.size):
            for r in range(self.size):
                hidden_grid[j][r]=temp_list[index]
                index+=1
        return hidden_grid
#displays the board with x's
    def display(self):
        print("   " + " ".join(chr(65 + i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            print(f"{idx}  " + " ".join(map(str, row)))
            #displays all the numbers
    def display_hidden(self):
        print("   " + " ".join(chr(65 + i) for i in range(self.size)))
        for idx, row in enumerate(self.hidden_grid):
            print(f"{idx}  " + " ".join(map(str, row)))
            #reveals the number for a specific cell
    def reveal_number(self,row,col):
        self.grid[row][col] = self.hidden_grid[row][col]
        #hides the number for a specific cell
    def hide_number(self,row,col):
        self.grid[row][col] = 'X'