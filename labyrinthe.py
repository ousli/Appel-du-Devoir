from random import choice, randint
from time import sleep


class Labyrinthe:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._WALL = 1
        self._CELL = 0
        self._UNVISITED = 2
        # self._start = start
        # self._end = end
        self._map = [[self._UNVISITED for i in range(
            width)] for i in range(height)]
        self.generate()

    def check_neighbors(self, map_x, map_y):
        neightbors = []
        if map_y > 1:
            top = self._map[map_x][map_y-2]
            if top == self._UNVISITED:
                neightbors.append((map_x, map_y-2))
        if map_x < self._width-2:
            right = self._map[map_x+1][map_y]
            if right == self._UNVISITED:
                neightbors.append((map_x+2, map_y))
        if map_x > 1:
            left = self._map[map_x-1][map_y]
            if left == self._UNVISITED:
                neightbors.append((map_x-2, map_y))
        if map_y < self._height-2:
            bottom = self._map[map_x][map_y+1]
            if bottom == self._UNVISITED:
                neightbors.append((map_x, map_y+2))
        #     ###############
        # if top and top == self._UNVISITED:
        #     neightbors.append((map_x, map_y-1))
        # if right and right == self._UNVISITED:
        #     neightbors.append((map_x+1, map_y))
        # if left and left == self._UNVISITED:
        #     neightbors.append((map_x-1, map_y))
        # if bottom and bottom == self._UNVISITED:
        #     neightbors.append((map_x, map_y+1))
        # for e in neightbors:
        #     if e != self._UNVISITED:
        if neightbors:
            return choice(neightbors)
        else:
            return False

    def wall(self, current, next):
        dx = current[0] - next[0]
        if dx == 1:
            self._map[current[0]-1][current[1]] = self._CELL
            self._map[next[0]+1][next[1]] = self._CELL
        elif dx == -1:
            self._map[current[0+1]][current[1]] = self._CELL
            self._map[next[0-1]][next[1]] = self._CELL
        dy = current[1] - next[1]
        if dy == 1:
            self._map[current[0]][current[1]-1] = self._CELL
            self._map[next[0]][next[1]+1] = self._CELL
        elif dy == -1:
            self._map[current[0]][current[1]+1] = self._CELL
            self._map[next[0]][next[1]-1] = self._CELL

    def generate(self):
        current_cell = (0, randint(1, self._width-1))
        # print(current_cell)
        stack = []
        i = 0
        while i < (self._width * self._height)**2:
            self._map[current_cell[0]][current_cell[1]] = self._CELL
            next_cell = self.check_neighbors(current_cell[0], current_cell[1])
            # print(next_cell)
            # sleep(0.1)
            if next_cell:
                self._map[next_cell[0]][next_cell[1]] = self._CELL
                self.wall(current_cell, next_cell)
                stack.append(current_cell)
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()
            # self.print_map()
            i += 1
            # for i in range(self._height):
            #     for j in range(self._width):
            # 1 vérifie si c'est le départ ou pas
            # Placer une ou plusieurs case qui touche la dernière
            # UN SEUL chemin qui vas jusqu'à l'arrivé
            # Stocker les coordonné de chaque case sous forme de tuple

    def get_map(self):
        return self._map

    def print_map(self):
        for e in self._map:
            for f in e:
                print(f, end='')
            print("")


lab1 = Labyrinthe(20, 20)
print(lab1.print_map())
