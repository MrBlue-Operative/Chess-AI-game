
def generate_moves(grid, color):
    moves = []
    for y in range(8):
        for x in range(8):
            piece = grid[y][x]
            if piece and piece.color == color:
                for to_y in range(8):
                    for to_x in range(8):
                        if piece.valid_move(to_x, to_y):
                            moves.append((x, y, to_x, to_y))
    return moves

def evaluate(grid):
    whitePoints = 0
    blackPoints = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is not None:
                if grid[i][j].color == "black":
                    blackPoints += grid[i][j].point
                else:
                    whitePoints += grid[i][j].point
    return whitePoints - blackPoints

def apply_move(grid, move):
    from_x, from_y, to_x, to_y = move
    new_grid = [[piece.clone() if piece else None for piece in row] for row in grid]
    # Move the piece
    piece = new_grid[from_y][from_x]
    new_grid[from_y][from_x] = None
    new_grid[to_y][to_x] = piece
    piece.x = to_x
    piece.y = to_y
    return new_grid

def minimax(grid, depth, is_maximizing, alpha, beta):
    if depth == 0:
        return evaluate(grid)
    
    if is_maximizing:  # White's turn
        max_eval = -float('inf')
        for move in generate_moves(grid, "white"):
            new_grid = apply_move(grid, move)
            eval = minimax(new_grid, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:  # Black's turn
        min_eval = float('inf')
        for move in generate_moves(grid, "black"):
            new_grid = apply_move(grid, move)
            eval = minimax(new_grid, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval