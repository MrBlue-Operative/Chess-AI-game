import pygame as py
from config import path, screen, unit, normalize, opposite

class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 1
    
    def clone(self):
        cloned_pawn = Pawn(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_pawn.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))

    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False
        if self.color == "white":
            n = 1
        else:
            n = -1

        if self.first:
            if ((self.y - y == n or self.y - y == n + n) and self.x == x) and isFree(x, y, self.color):
                return True
        
        if abs(self.x - x) == 1 and self.y - y == n and not isFree(x, y, opposite(self.color)):
            return True
            
        if (self.y - y == n and self.x == x) and isFree(x, y, self.color):
            if not isFree(x, y, opposite(self.color)):
                return False
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()

class Rook:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 5
    
    def clone(self):
        cloned_pawn = Rook(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_rook.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))
    
    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False
        
        if (self.x == x or self.y == y) and isFree(x, y, self.color):
            dx = normalize(x - self.x)
            dy = normalize(y - self.y)
            stepX = self.x
            stepY = self.y
            count = 0
            while not (stepX == x and stepY == y):
                stepX += dx
                stepY += dy

                if count == 1:
                    return False
                
                if not isFree(stepX, stepY, opposite(self.color)):
                    count += 1
                
                
                if not isFree(stepX, stepY, self.color):
                    return False
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()

class Knight:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 3
    
    def clone(self):
        cloned_pawn = Knight(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_knight.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))

    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False
        
        if ((abs(self.x - x) == 2 and abs(self.y - y) == 1) or (abs(self.x - x) == 1 and abs(self.y - y) == 2)) and isFree(x, y, self.color):
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()

class Bishop:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 3
    
    def clone(self):
        cloned_pawn = Bishop(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_bishop.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))
    
    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False
        
        if (abs(self.x - x) == abs(self.y - y)) and isFree(x, y, self.color):
            dx = normalize(x - self.x)
            dy = normalize(y - self.y)
            stepX = self.x
            stepY = self.y
            count = 0
            while not (stepX == x and stepY == y):
                stepX += dx
                stepY += dy

                if count == 1:
                    return False
                
                if not isFree(stepX, stepY, opposite(self.color)):
                    count += 1
                
                if not isFree(stepX, stepY, self.color):
                    return False
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()

class Queen:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 9
    
    def clone(self):
        cloned_pawn = Queen(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_queen.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))

    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False
    
        if (abs(self.x - x) == abs(self.y - y) or self.x == x or self.y == y) and isFree(x, y, self.color):
            dx = normalize(x - self.x)
            dy = normalize(y - self.y)
            stepX = self.x
            stepY = self.y
            count = 0
            while not (stepX == x and stepY == y):
                stepX += dx
                stepY += dy

                if count == 1:
                    return False
                
                if not isFree(stepX, stepY, opposite(self.color)):
                    count += 1
                
                if not isFree(stepX, stepY, self.color):
                    return False
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()

class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.first = True
        # Value of the Material
        self.point = 100
    
    def clone(self):
        cloned_pawn = King(self.x, self.y, self.color)
        cloned_pawn.first = self.first
        return cloned_pawn
        
    def print(self):
        pawn = py.image.load(path + self.color + '_king.png').convert_alpha()
        pawn = py.transform.scale(pawn, (unit.x/2, unit.y/2))
        screen.blit(pawn, (self.x * unit.x + 28, self.y * unit.y + 30))
    
    def valid_move(self, x, y):
        if self.x == x and self.y == y:
            return False

        if (abs(self.x - x) <= 1 and abs(self.y - y) <= 1) and isFree(x, y, self.color):
            return True
        else:
            return False
    
    def showLegalMoves(self):
        for x in range(8):
            for y in range(8):
                if self.valid_move(x, y) and isFree(x, y, self.color):
                    py.draw.circle(screen, (0, 12, 23), (x*unit.x + 52, y * unit.y + 48), 7)
                    py.display.flip()


# Other Helping objects Like indicator for visualization

def toggle(value):
    return not value

class Indicator:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        
    def print(self):
        py.draw.rect(screen, self.color, (self.x*unit.x + 8, self.y*unit.y + 8, unit.x, unit.y), 3)
        py.display.flip()

grid = [
    [Rook(0,0, "black"), Knight(1,0, "black"), Bishop(2,0, "black"), Queen(3,0, "black"), 
     King(4,0, "black"), Bishop(5,0, "black"), Knight(6,0, "black"), Rook(7,0, "black")],
    [Pawn(0,1, "black"), Pawn(1,1, "black"), Pawn(2,1, "black"), Pawn(3,1, "black"),
     Pawn(4,1, "black"), Pawn(5,1, "black"), Pawn(6,1, "black"), Pawn(7,1, "black")],
    [None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(0,6, "white"), Pawn(1,6, "white"), Pawn(2,6, "white"), Pawn(3,6, "white"),
     Pawn(4,6, "white"), Pawn(5,6, "white"), Pawn(6,6, "white"), Pawn(7,6, "white")],
    [Rook(0,7, "white"), Knight(1,7, "white"), Bishop(2,7, "white"), Queen(3,7, "white"),
     King(4,7, "white"), Bishop(5,7, "white"), Knight(6,7, "white"), Rook(7,7, "white")]
]

def isFree(x, y, color):
    if grid[y][x] == None or grid[y][x].color != color:
        return True
    return False