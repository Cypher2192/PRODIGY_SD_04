import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Sudoku Solver")
app.geometry("400x500")

grid = [[tk.Entry(app, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        grid[i][j].grid(row=i, column=j, padx=5, pady=5)
        grid[i][j].bind("<KeyRelease>", lambda e, row=i, col=j: validate_input(row, col))

def validate_input(row, col):
    value = grid[row][col].get()
    if not (value.isdigit() and 1 <= int(value) <= 9):
        grid[row][col].delete(0, tk.END)

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = grid[i][j].get()
            row.append(int(value) if value.isdigit() else 0)
        board.append(row)
    return board

def fill_board(board):
    for i in range(9):
        for j in range(9):
            grid[i][j].delete(0, tk.END)
            grid[i][j].insert(0, str(board[i][j]))

def solve():
    board = get_board()
    if solve_sudoku(board):
        fill_board(board)
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            grid[i][j].delete(0, tk.END)

tk.Button(app, text="Solve", command=solve, width=15).grid(row=10, column=0, columnspan=5, pady=20)
tk.Button(app, text="Clear", command=clear_grid, width=15).grid(row=10, column=4, columnspan=5, pady=20)

app.mainloop()
