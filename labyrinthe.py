class Labyrinthe:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # self._start = start
        # self._end = end
        self._map = [[0 for i in range(width)] for i in range(height)]

    def check_neighbors(self):
        neightbors = []
        top = self

    def generate(self):

        # for i in range(self._height):
        #     for j in range(self._width):
        # 1 vérifie si c'est le départ ou pas
        # Placer une ou plusieurs case qui touche la dernière
        # UN SEUL chemin qui vas jusqu'à l'arrivé
        # Stocker les coordonné de chaque case sous forme de tuple

    def get_map(self):
        return self._map


lab1 = Labyrinthe(10, 10)
print(lab1.get_map())
