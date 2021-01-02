# Globals for the directions
# Change the values as you see fit
EAST = [1, 0]
NORTH = [0, 1]
WEST = [-1, 0]
SOUTH = [0, -1]


class Robot:
    def __init__(self, direction=None, x=0, y=0):
        if direction is None:
            direction = NORTH
        self.directions = [EAST, NORTH, WEST, SOUTH]
        self.direction = direction
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def move(self, movement):

        index_points = self.directions.index(self.direction)

        for move in movement:
            if move == 'R':
                index_points -= 1
                if index_points == -1:
                    index_points = 3
                self.direction = self.directions[index_points]
            elif move == 'L':
                index_points += 1
                if index_points == 4:
                    index_points = 0
                self.direction = self.directions[index_points]
            elif move == 'A':
                self.x += self.direction[0]
                self.y += self.direction[1]
                self.coordinates = (self.x, self.y)
