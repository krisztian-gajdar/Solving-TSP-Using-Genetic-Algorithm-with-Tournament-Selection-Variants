import math

class City:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    # kiiratáshoz
    def __repr__(self):
        return str(self.index)

    # Euclidian distance 2 város közt
    def distanceTo(self, city2):
        x_dist = abs(self.x - city2.x)
        y_dist = abs(self.y - city2.y)
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)