from random import choice, randint


class Labyrinthe:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._mur = 1
        self._case = 0
        self._pas_visite = 2
        self._entree = 3
        self._sortie = 4
        self._laby = [[self._pas_visite for i in range(
            width)] for i in range(height)]
        self.generate()

    def compter_cellules(self, prochain_mur):
        nb_cases = 0
        if self._laby[prochain_mur[0]-1][prochain_mur[1]] == self._case:
            nb_cases += 1
        if self._laby[prochain_mur[0]+1][prochain_mur[1]] == self._case:
            nb_cases += 1
        if self._laby[prochain_mur[0]][prochain_mur[1]-1] == self._case:
            nb_cases += 1
        if self._laby[prochain_mur[0]][prochain_mur[1]+1] == self._case:
            nb_cases += 1

        return nb_cases

    def generate(self):

        case_depart = (randint(1, self._height-2), randint(1, self._width-2))

        self._laby[case_depart[0]][case_depart[1]] = self._case
        liste_mur = []
        liste_mur.append([case_depart[0] - 1, case_depart[1]])
        liste_mur.append([case_depart[0], case_depart[1] - 1])
        liste_mur.append([case_depart[0], case_depart[1] + 1])
        liste_mur.append([case_depart[0] + 1, case_depart[1]])

        self._laby[case_depart[0]-1][case_depart[1]] = self._mur
        self._laby[case_depart[0]][case_depart[1] - 1] = self._mur
        self._laby[case_depart[0]][case_depart[1] + 1] = self._mur
        self._laby[case_depart[0] + 1][case_depart[1]] = self._mur
        while liste_mur:
            prochain_mur = choice(liste_mur)
            if prochain_mur[1] != 0:
                if self._laby[prochain_mur[0]][prochain_mur[1]-1] == self._pas_visite and self._laby[prochain_mur[0]][prochain_mur[1]+1] == self._case:
                    nb_cases = self.compter_cellules(prochain_mur)

                    if nb_cases < 2:
                        self._laby[prochain_mur[0]
                                   ][prochain_mur[1]] = self._case

                        if prochain_mur[0] != 0:
                            if self._laby[prochain_mur[0]-1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] -
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]-1, prochain_mur[1]])

                        if prochain_mur[0] != self._height-1:
                            if self._laby[prochain_mur[0]+1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] +
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]+1, prochain_mur[1]])

                        if prochain_mur[1] != 0:
                            if self._laby[prochain_mur[0]][prochain_mur[1]-1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]-1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]-1])

                    for wall in liste_mur:
                        if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                            liste_mur.remove(wall)

                    continue

            if prochain_mur[0] != 0:
                if self._laby[prochain_mur[0]-1][prochain_mur[1]] == self._pas_visite and self._laby[prochain_mur[0]+1][prochain_mur[1]] == self._case:

                    nb_cases = self.compter_cellules(prochain_mur)
                    if nb_cases < 2:
                        self._laby[prochain_mur[0]
                                   ][prochain_mur[1]] = self._case

                        if prochain_mur[0] != 0:
                            if self._laby[prochain_mur[0]-1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] -
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]-1, prochain_mur[1]])

                        if prochain_mur[1] != 0:
                            if self._laby[prochain_mur[0]][prochain_mur[1]-1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]-1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]-1])

                        if prochain_mur[1] != self._width-1:
                            if self._laby[prochain_mur[0]][prochain_mur[1]+1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]+1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]+1])

                    for e in liste_mur:
                        if e[0] == prochain_mur[0] and e[1] == prochain_mur[1]:
                            liste_mur.remove(e)

                    continue

            if prochain_mur[0] != self._height-1:
                if self._laby[prochain_mur[0]+1][prochain_mur[1]] == self._pas_visite and self._laby[prochain_mur[0]-1][prochain_mur[1]] == self._case:

                    nb_cases = self.compter_cellules(prochain_mur)
                    if nb_cases < 2:
                        self._laby[prochain_mur[0]
                                   ][prochain_mur[1]] = self._case

                        if prochain_mur[0] != self._height-1:
                            if self._laby[prochain_mur[0]+1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] +
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]+1, prochain_mur[1]])
                        if prochain_mur[1] != 0:
                            if self._laby[prochain_mur[0]][prochain_mur[1]-1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]-1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]-1])
                        if prochain_mur[1] != self._width-1:
                            if self._laby[prochain_mur[0]][prochain_mur[1]+1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]+1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]+1])

                    for wall in liste_mur:
                        if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                            liste_mur.remove(wall)

                    continue

            if prochain_mur[1] != self._width-1:
                if self._laby[prochain_mur[0]][prochain_mur[1]+1] == self._pas_visite and self._laby[prochain_mur[0]][prochain_mur[1]-1] == self._case:

                    nb_cases = self.compter_cellules(prochain_mur)
                    if nb_cases < 2:
                        self._laby[prochain_mur[0]
                                   ][prochain_mur[1]] = self._case

                        if prochain_mur[1] != self._width-1:
                            if self._laby[prochain_mur[0]][prochain_mur[1]+1] != self._case:
                                self._laby[prochain_mur[0]
                                           ][prochain_mur[1]+1] = self._mur
                            if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0], prochain_mur[1]+1])
                        if prochain_mur[0] != self._height-1:
                            if self._laby[prochain_mur[0]+1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] +
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]+1, prochain_mur[1]])
                        if prochain_mur[0] != 0:
                            if self._laby[prochain_mur[0]-1][prochain_mur[1]] != self._case:
                                self._laby[prochain_mur[0] -
                                           1][prochain_mur[1]] = self._mur
                            if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                                liste_mur.append(
                                    [prochain_mur[0]-1, prochain_mur[1]])

                    for wall in liste_mur:
                        if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                            liste_mur.remove(wall)

                    continue

            for wall in liste_mur:
                if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                    liste_mur.remove(wall)

        for i in range(0, self._height):
            for j in range(0, self._width):
                if self._laby[i][j] == self._pas_visite:
                    self._laby[i][j] = self._mur

        for i in range(0, self._width):
            if self._laby[1][i] == self._case:
                self._laby[0][i] = self._entree
                break

        for i in range(self._width-1, 0, -1):
            if self._laby[self._height-2][i] == self._case:
                self._laby[self._height-1][i] = self._sortie
                break

    def get_map(self):
        return self._laby
