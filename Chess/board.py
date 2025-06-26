import pygame as py
import elements as asset
from elements import grid
from config import path, screen, fheight, fwidth, FPS, unit, pos, helper, toggle
from AI_Implementation import minimax, generate_moves, apply_move

def checkAndTurnQueen(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                if grid[i][j].point == 1 and (i == 0 or i == 7):
                    c = grid[i][j].color
                    grid[i][j] = asset.Queen(j, i, c)
                
def isKingExists(grid):
    white = 0
    black = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                if grid[i][j].point == 100:
                    if grid[i][j].color == "white":
                        white += 1
                    else:
                        black += 1
    if white and black:
        return 0
    if white and not black:
        return 1   # white wins
    if not white and black:
        return -1  # black wins

def get_best_move(grid, color, depth):
    best_score = float('inf') if color == "black" else -float('inf')
    best_move = None
    for move in generate_moves(grid, color):
        new_grid = apply_move(grid, move)
        is_opponent_maximizing = (color == "black")  # True if opponent is white (maximizing)
        score = minimax(new_grid, depth - 1, is_opponent_maximizing, -float('inf'), float('inf'))
        if color == "black":
            if score < best_score:
                best_score = score
                best_move = move
        else:
            if score > best_score:
                best_score = score
                best_move = move
    return best_move


py.display.set_caption("Chess Game")
clock = py.time.Clock()

board = py.image.load(path + 'board.png').convert_alpha()
board = py.transform.scale(board, (fwidth, fheight))

# Sound when the piece moves
click_sound = py.mixer.Sound('Pixel_Art_Chess_DevilsWorkshop_V04/' + 'click.mp3')


flag = False
x = 100
y = 100
visual = False
whiteTurn = True
whiteWon = False
blackWon = False
stopwatch = 120
while True:
    screen.fill((250, 250, 250))

    if not whiteTurn:
        best_move = get_best_move(grid, "black", depth=3) 
        if best_move:
            from_col, from_row, to_col, to_row = best_move
            piece = grid[from_row][from_col]
            grid[to_row][to_col] = piece
            piece.x = to_col
            piece.y = to_row
            piece.first = False
            grid[from_row][from_col] = None
            click_sound.play()
            whiteTurn = True
            checkAndTurnQueen(grid)
            state = isKingExists(grid)
            if state == 1:
                whiteWon = True
            elif state == -1:
                blackWon = True

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if flag:
                    if grid[x][y] != None and whiteTurn == helper(grid[x][y].color):
                        if grid[x][y].valid_move(cellY, cellX):
                            grid[cellX][cellY] = grid[x][y]
                            grid[cellX][cellY].x = cellY
                            grid[cellX][cellY].y = cellX
                            grid[cellX][cellY].first = False
                            grid[x][y] = None
                            click_sound.play()
                            whiteTurn = toggle(whiteTurn)
                    flag = False
                    visual = False
                    checkAndTurnQueen(grid)
                    state = isKingExists(grid)
                    if state == 1:
                        whiteWon = True
                    elif state == -1:
                        blackWon = True
                else:
                    flag = True
                    y, x = pos()
                    x2, y2 = pos()
                    if grid[x][y] is not None:
                        visual = True    
                    else:
                        visual = False
                  
    

    if not flag:
        y, x = pos()
        x2, y2 = pos()
    screen.blit(board, (0, 0))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                grid[i][j].print()

    if visual:
        grid[x][y].showLegalMoves()

    if whiteWon:
        font = py.font.Font(None, 74)
        text = font.render("White won", True, (255, 0, 0))
        text_rect = text.get_rect(center=(fwidth // 2, fheight // 2))
        screen.blit(text, text_rect)
        stopwatch -= 1
    
    if blackWon:
        font = py.font.Font(None, 74)
        text = font.render("Black won", True, (255, 0, 0))
        text_rect = text.get_rect(center=(fwidth // 2, fheight // 2))
        screen.blit(text, text_rect)
        stopwatch -= 1

    if stopwatch < 0:
        py.quit()
        exit()


    cellY, cellX = pos()
    X, Y = pos()
    indicator = asset.Indicator(x2, y2)
    selected_CELL = asset.Indicator(X, Y, (2, 5, 255))
    indicator.print()
    selected_CELL.print()
    py.display.update()
    clock.tick(FPS)