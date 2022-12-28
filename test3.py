from random import randint, choice


MUR = 1
CASE = 0
PAS_VISITE = 2
HEIGHT = 20
WIDTH = 20
laby = [[PAS_VISITE for j in range(WIDTH)] for i in range(WIDTH)]


def compter_cellules(prochain_mur):
    nb_cases = 0
    if laby[prochain_mur[0]-1][prochain_mur[1]] == CASE:
        nb_cases += 1
    if laby[prochain_mur[0]+1][prochain_mur[1]] == CASE:
        nb_cases += 1
    if laby[prochain_mur[0]][prochain_mur[1]-1] == CASE:
        nb_cases += 1
    if laby[prochain_mur[0]][prochain_mur[1]+1] == CASE:
        nb_cases += 1

    return nb_cases


# Randomize starting point and set it a cell
case_depart = (randint(1, HEIGHT-2), randint(1, WIDTH-2))
# case_depart[0] = randint(1, HEIGHT-2)
# case_depart[1] = randint(1, WIDTH-2)

# Mark it as cell and add surrounding liste_mur to the list
laby[case_depart[0]][case_depart[1]] = CASE
liste_mur = []
liste_mur.append([case_depart[0] - 1, case_depart[1]])
liste_mur.append([case_depart[0], case_depart[1] - 1])
liste_mur.append([case_depart[0], case_depart[1] + 1])
liste_mur.append([case_depart[0] + 1, case_depart[1]])

laby[case_depart[0]-1][case_depart[1]] = MUR
laby[case_depart[0]][case_depart[1] - 1] = MUR
laby[case_depart[0]][case_depart[1] + 1] = MUR
laby[case_depart[0] + 1][case_depart[1]] = MUR


while liste_mur:
    prochain_mur = choice(liste_mur)
    # Check if it is a left wall
    if prochain_mur[1] != 0:
        if laby[prochain_mur[0]][prochain_mur[1]-1] == PAS_VISITE and laby[prochain_mur[0]][prochain_mur[1]+1] == CASE:
            # Find the number of surrounding cells
            nb_cases = compter_cellules(prochain_mur)

            if nb_cases < 2:
                # Denote the new path
                laby[prochain_mur[0]][prochain_mur[1]] = CASE

                # Mark the new liste_mur
                # Upper cell
                if prochain_mur[0] != 0:
                    if laby[prochain_mur[0]-1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]-1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]-1, prochain_mur[1]])

                # Bottom cell
                if prochain_mur[0] != HEIGHT-1:
                    if laby[prochain_mur[0]+1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]+1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]+1, prochain_mur[1]])

                # Leftmost cell
                if prochain_mur[1] != 0:
                    if laby[prochain_mur[0]][prochain_mur[1]-1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]-1] = MUR
                    if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]-1])

            # Delete wall
            for wall in liste_mur:
                if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                    liste_mur.remove(wall)

            continue

    # Check if it is an upper wall
    if prochain_mur[0] != 0:
        if laby[prochain_mur[0]-1][prochain_mur[1]] == PAS_VISITE and laby[prochain_mur[0]+1][prochain_mur[1]] == CASE:

            nb_cases = compter_cellules(prochain_mur)
            if nb_cases < 2:
                # Denote the new path
                laby[prochain_mur[0]][prochain_mur[1]] = CASE

                # Mark the new liste_mur
                # Upper cell
                if prochain_mur[0] != 0:
                    if laby[prochain_mur[0]-1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]-1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]-1, prochain_mur[1]])

                # Leftmost cell
                if prochain_mur[1] != 0:
                    if laby[prochain_mur[0]][prochain_mur[1]-1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]-1] = MUR
                    if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]-1])

                # Rightmost cell
                if prochain_mur[1] != WIDTH-1:
                    if laby[prochain_mur[0]][prochain_mur[1]+1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]+1] = MUR
                    if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]+1])

            # Delete wall
            for e in liste_mur:
                if e[0] == prochain_mur[0] and e[1] == prochain_mur[1]:
                    liste_mur.remove(e)

            continue

    # Check the bottom wall
    if prochain_mur[0] != HEIGHT-1:
        if laby[prochain_mur[0]+1][prochain_mur[1]] == PAS_VISITE and laby[prochain_mur[0]-1][prochain_mur[1]] == CASE:

            nb_cases = compter_cellules(prochain_mur)
            if nb_cases < 2:
                # Denote the new path
                laby[prochain_mur[0]][prochain_mur[1]] = CASE

                # Mark the new liste_mur
                if prochain_mur[0] != HEIGHT-1:
                    if laby[prochain_mur[0]+1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]+1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]+1, prochain_mur[1]])
                if prochain_mur[1] != 0:
                    if laby[prochain_mur[0]][prochain_mur[1]-1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]-1] = MUR
                    if [prochain_mur[0], prochain_mur[1]-1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]-1])
                if prochain_mur[1] != WIDTH-1:
                    if laby[prochain_mur[0]][prochain_mur[1]+1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]+1] = MUR
                    if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]+1])

            # Delete wall
            for wall in liste_mur:
                if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                    liste_mur.remove(wall)

            continue

    # Check the right wall
    if prochain_mur[1] != WIDTH-1:
        if laby[prochain_mur[0]][prochain_mur[1]+1] == PAS_VISITE and laby[prochain_mur[0]][prochain_mur[1]-1] == CASE:

            nb_cases = compter_cellules(prochain_mur)
            if nb_cases < 2:
                # Denote the new path
                laby[prochain_mur[0]][prochain_mur[1]] = CASE

                # Mark the new liste_mur
                if prochain_mur[1] != WIDTH-1:
                    if laby[prochain_mur[0]][prochain_mur[1]+1] != CASE:
                        laby[prochain_mur[0]][prochain_mur[1]+1] = MUR
                    if [prochain_mur[0], prochain_mur[1]+1] not in liste_mur:
                        liste_mur.append([prochain_mur[0], prochain_mur[1]+1])
                if prochain_mur[0] != HEIGHT-1:
                    if laby[prochain_mur[0]+1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]+1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]+1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]+1, prochain_mur[1]])
                if prochain_mur[0] != 0:
                    if laby[prochain_mur[0]-1][prochain_mur[1]] != CASE:
                        laby[prochain_mur[0]-1][prochain_mur[1]] = MUR
                    if [prochain_mur[0]-1, prochain_mur[1]] not in liste_mur:
                        liste_mur.append([prochain_mur[0]-1, prochain_mur[1]])

            # Delete wall
            for wall in liste_mur:
                if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
                    liste_mur.remove(wall)

            continue

    # Delete the wall from the list anyway
    for wall in liste_mur:
        if wall[0] == prochain_mur[0] and wall[1] == prochain_mur[1]:
            liste_mur.remove(wall)


# Mark the remaining unvisited cells as liste_mur
for i in range(0, HEIGHT):
    for j in range(0, WIDTH):
        if laby[i][j] == PAS_VISITE:
            laby[i][j] = MUR

# Set entrance and exit
for i in range(0, WIDTH):
    if laby[1][i] == CASE:
        laby[0][i] = CASE
        break

for i in range(WIDTH-1, 0, -1):
    if laby[HEIGHT-2][i] == CASE:
        laby[HEIGHT-1][i] = CASE
        break

print(laby)
