import turtle

# --- Setup screen ---
win = turtle.Screen()
win.title("Tic Tac Toe 🧩")
win.setup(width=400, height=400)

# --- Draw grid ---
pen = turtle.Turtle()
pen.pensize(5)
pen.hideturtle()

# Vertical lines
pen.penup()
pen.goto(-60, 180)
pen.pendown()
pen.goto(-60, -180)

pen.penup()
pen.goto(60, 180)
pen.pendown()
pen.goto(60, -180)

# Horizontal lines
pen.penup()
pen.goto(-180, 60)
pen.pendown()
pen.goto(180, 60)

pen.penup()
pen.goto(-180, -60)
pen.pendown()
pen.goto(180, -60)

# --- Game state ---
board = [["" for _ in range(3)] for _ in range(3)]
turn = "X"
game_over = False

# --- Helper functions ---
def draw_x(x, y):
    pen.color("blue")
    pen.penup()
    pen.goto(x - 40, y - 40)
    pen.pendown()
    pen.goto(x + 40, y + 40)
    pen.penup()
    pen.goto(x - 40, y + 40)
    pen.pendown()
    pen.goto(x + 40, y - 40)

def draw_o(x, y):
    pen.color("red")
    pen.penup()
    pen.goto(x, y - 40)
    pen.pendown()
    pen.circle(40)

def get_cell(x, y):
    col = (x + 180) // 120
    row = (180 - y) // 120
    if 0 <= row < 3 and 0 <= col < 3:
        return int(row), int(col)
    return None, None

def check_winner():
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return board[r][0]
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def cell_center(row, col):
    return -120 + col * 120, 120 - row * 120

def click(x, y):
    global turn, game_over
    if game_over:
        return
    row, col = get_cell(x, y)
    if row is not None and board[row][col] == "":
        cx, cy = cell_center(row, col)
        if turn == "X":
            draw_x(cx, cy)
            board[row][col] = "X"
            turn = "O"
        else:
            draw_o(cx, cy)
            board[row][col] = "O"
            turn = "X"
        winner = check_winner()
        if winner:
            turtle.penup()
            turtle.goto(0, -200)
            turtle.color("green")
            turtle.write(f"{winner} wins!", align="center", font=("Courier", 24, "bold"))
            game_over = True
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            turtle.penup()
            turtle.goto(0, -200)
            turtle.color("orange")
            turtle.write("It's a draw!", align="center", font=("Courier", 24, "bold"))
            game_over = True

win.onclick(click)
turtle.done()