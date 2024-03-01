import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.master.bind("<Key>", self.key_pressed)
        
        self.board_size = 4
        self.tiles = [[0] * self.board_size for _ in range(self.board_size)]
        
        self.score = 0
        self.high_score = 0
        
        self.create_widgets()
        self.new_game()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="lightgray")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.high_score_label = tk.Label(self.master, text="High Score: 0")
        self.high_score_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
    def new_game(self):
        self.score = 0
        self.update_score_display()
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.tiles[row][col] = 0
        
        self.add_random_tile()
        self.add_random_tile()
        self.draw_board()
        
    def draw_board(self):
        self.canvas.delete("tile")
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                value = self.tiles[row][col]
                if value > 0:
                    x0, y0 = col * 100, row * 100
                    x1, y1 = x0 + 100, y0 + 100
                    color = "#%02x%02x%02x" % (255 - value*10, 255 - value*10, 255)
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags="tile")
                    self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(value), tags="tile")
                    
    def add_random_tile(self):
        empty_tiles = [(row, col) for row in range(self.board_size) for col in range(self.board_size) if self.tiles[row][col] == 0]
        if empty_tiles:
            row, col = random.choice(empty_tiles)
            self.tiles[row][col] = 2 if random.random() < 0.9 else 4
            
    def key_pressed(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.move_tiles(event.keysym)
            self.add_random_tile()
            self.draw_board()
            self.update_score_display()
    
    def move_tiles(self, direction):
        if direction == "Up":
            for col in range(self.board_size):
                self.move_col_up(col)
        elif direction == "Down":
            for col in range(self.board_size):
                self.move_col_down(col)
        elif direction == "Left":
            for row in range(self.board_size):
                self.move_row_left(row)
        elif direction == "Right":
            for row in range(self.board_size):
                self.move_row_right(row)
    
    def move_col_up(self, col):
        for row in range(1, self.board_size):
            if self.tiles[row][col] != 0:
                for i in range(row, 0, -1):
                    if self.tiles[i-1][col] == 0:
                        self.tiles[i-1][col] = self.tiles[i][col]
                        self.tiles[i][col] = 0
                    elif self.tiles[i-1][col] == self.tiles[i][col]:
                        self.tiles[i-1][col] *= 2
                        self.tiles[i][col] = 0
                        self.score += self.tiles[i-1][col]
                        break
    
    def move_col_down(self, col):
        for row in range(self.board_size-2, -1, -1):
            if self.tiles[row][col] != 0:
                for i in range(row, self.board_size-1):
                    if self.tiles[i+1][col] == 0:
                        self.tiles[i+1][col] = self.tiles[i][col]
                        self.tiles[i][col] = 0
                    elif self.tiles[i+1][col] == self.tiles[i][col]:
                        self.tiles[i+1][col] *= 2
                        self.tiles[i][col] = 0
                        self.score += self.tiles[i+1][col]
                        break
    
    def move_row_left(self, row):
        for col in range(1, self.board_size):
            if self.tiles[row][col] != 0:
                for i in range(col, 0, -1):
                    if self.tiles[row][i-1] == 0:
                        self.tiles[row][i-1] = self.tiles[row][i]
                        self.tiles[row][i] = 0
                    elif self.tiles[row][i-1] == self.tiles[row][i]:
                        self.tiles[row][i-1] *= 2
                        self.tiles[row][i] = 0
                        self.score += self.tiles[row][i-1]
                        break
    
    def move_row_right(self, row):
        for col in range(self.board_size-2, -1, -1):
            if self.tiles[row][col] != 0:
                for i in range(col, self.board_size-1):
                    if self.tiles[row][i+1] == 0:
                        self.tiles[row][i+1] = self.tiles[row][i]
                        self.tiles[row][i] = 0
                    elif self.tiles[row][i+1] == self.tiles[row][i]:
                        self.tiles[row][i+1] *= 2
                        self.tiles[row][i] = 0
                        self.score += self.tiles[row][i+1]
                        break
    
    def update_score_display(self):
        self.score_label.config(text="Score: {}".format(self.score))
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text="High Score: {}".format(self.high_score))

root = tk.Tk()
game = Game2048(root)
root.mainloop()