import random
class Grid:
    def __init__(self,size):
        self.size = size
        self.grid = [['X'] * size for _ in range(size)]
        self.hidden_grid = self.make_hidden_grid()
        
    def make_hidden_grid(self):
        hidden_grid = [[None] * self.size for _ in range(self.size)]
        index = 0
        temp_list = [0] * (self.size**2)
        for i in range(0, len(temp_list), 2):
            temp = random.randint(0,9)
            temp_list[i], temp_list[i+1] = temp, temp
        random.shuffle(temp_list)
        for row in range(self.size):
            for col in range(self.size):
                hidden_grid[row][col] = temp_list[index]
                index += 1
        return hidden_grid

    def display(self):
        print("   " + " ".join(chr(65 + i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            print(f"{idx}  " + " ".join(map(str, row)))
            
    def display_hidden(self):
        print("   " + " ".join(chr(65 + i) for i in range(self.size)))
        for idx, row in enumerate(self.hidden_grid):
            print(f"{idx}  " + " ".join(map(str, row)))

    def reveal_number(self, row, col):
        self.grid[row][col] = self.hidden_grid[row][col]

    def hide_number(self, row, col):
        self.grid[row][col] = 'X'