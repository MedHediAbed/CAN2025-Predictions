
import random
import numpy as np

print("*** Group stage*** : \n ")

Initial_standing = [["Morocco", "Comores", "Mali", "Zambia"], 
                    ["Angola", "Egypt", "South Africa", "Zimbabwe"],
                    ["Uganda", "Tunisia", "Nigeria", "Tanzania"],
                    ["Benin", "Botswana", "RD Congo", "Senegal"],
                    ["Soudan", "Algeria", "Equatorial Guinea", "Burkina Faso"],
                    ["Cameroon", "Gabon", "Côte d'ivoire", "Mozambique"]]

Cotas = [[38, 1.25, 4.9, 1.95], [3.9, 7.57, 5.88, 0.91], [1.85, 6.96, 7.31, 1.84],
         [2.21, 0.94, 4.24, 10.12], [1.07, 8.54, 2.14, 4.02], [6.78, 2.18, 9.97, 2.00]]

def getgrp(team):
    for i in Initial_standing:
        if team in i:
            return Initial_standing.index(i)+1
    raise ValueError(f"Team not found in groups: {team}")
def getcota(team):
            g = getgrp(team)-1
            return Cotas[g][Initial_standing[g].index(team)]

#First Round
final_standing = []
for i in range(6):

    options = Initial_standing[i]
    poids = Cotas[i]  

    probas = np.array(poids) / sum(poids)

    standing = np.random.choice(
        options,
        size=4,          # k éléments
        replace=False,   # SANS remise
        p=probas
    )
    final_standing.append(standing)
    first = standing[0] 
    second = standing[1]

    print(f"Group {i+1}: \nfirst: {first} \nsecond: {second }")
thirds = []
th_cotas = []
for j in range (len(final_standing)):
    thirds.append(final_standing[j][2])
    th_cotas.append(Cotas[j][Initial_standing[j].index(final_standing[j][2])])

options = thirds
poids = th_cotas

probas = np.array(poids) / sum(poids)
best_thrds = list(np.random.choice(
    options,
    size=4,          # k éléments
    replace=False,   # SANS remise
    p=probas
))


print(f"Best thirds:\n{best_thrds[0]} - {best_thrds[1]} - {best_thrds[2]} - {best_thrds[3]}\n")    

'''def comm(list1, list2):
     cmn = []
     for i in list1:
          if i in list2:
               cmn.append(i)
     return cmn
#eliminatories
def thirds_list(a, b, c):
     tli= []
     grps_of_thirds = []
     for i in best_thrds:
          grps_of_thirds.append(getgrp(i))
     list_choices = [[2,5,6], [1,3,4], [3,4,5], [1,2,6]]
     commun = comm(list_choices[0],best_thrds)
     if len(commun)==1 :
          tli[0]=commun
     elif len(commun)==2:
          
getthird = thirds_list() '''


# groupes autorisés par position
allowed_groups = {
    0: {2, 5, 6},
    1: {1, 3, 4},
    2: {3, 4, 5},
    3: {1, 2, 6}
}

def assign_positions(teams):
    """
    teams : list of 4 distinct team names
    return : list of 4 teams ordered according to constraints
    """

    for _ in range(1000):  # sécurité anti-boucle infinie
        result = [None] * 4
        used = set()

        for pos in range(4):
            candidates = [
                t for t in teams
                if t not in used and getgrp(t) in allowed_groups[pos]
            ]

            if not candidates:
                break  # échec → on recommence

            chosen = random.choice(candidates)
            result[pos] = chosen
            used.add(chosen)

        if None not in result:
            return result

    raise ValueError("No valid assignment found")

huits = [[final_standing[0][1], final_standing[2][1]],    
      [final_standing[3][0], assign_positions(best_thrds)[0]],       
      [final_standing[1][0], assign_positions(best_thrds)[1]],       
       [final_standing[5][0], final_standing[4][1]],
       [final_standing[1][1], final_standing[5][1]],
       [final_standing[0][0], assign_positions(best_thrds)[2]],          
       [final_standing[4][0], final_standing[3][1]],
        [final_standing[2][0], assign_positions(best_thrds)[3]]]      


'''for i in best_thrds:
    if getgrp(i) in [2, 6]:
        if huits[1][1]==X:
            huits[1][1]=i
        else:
            huits[7][1]=i
    elif getgrp(i) in [3, 4]:
        if huits[2][1]==X:
            huits[2][1]=i
        else:
            huits[5][1]=i
    elif getgrp(i)==5:
        if huits[1][1]==X:
            huits[1][1]=i
        else:
            huits[5][1]=i
    else:
        if huits[2][1]==X:
            huits[2][1]=i
        else:
            huits[7][1]=i'''

'''# mapping: group -> possible huits indices (priority order)
group_map = {
    2: (1, 7),
    6: (1, 7),
    3: (2, 5),
    4: (2, 5),
    5: (1, 5)
}

for i in best_thrds:
    grp = getgrp(i)

    # default case
    if grp not in group_map:
        targets = (2, 7)
    else:
        targets = group_map[grp]

    # place team in first available slot
    for idx in targets:
        if huits[idx][1] == X:
            huits[idx][1] = i
            break'''

        
print("\n*** 1/8-finals ***:\n")
for i in huits:
    print(i[0] + " Vs " + i[1] + " \n")

#Quarter-finals
print("*** Quarter-finals ***:\n")
quarts = []
for i in huits:

    options = i
    poids = [getcota(i[0]), getcota(i[1])]

    probas = np.array(poids) / sum(poids)
    vainc = np.random.choice(
        options,
        size=1,          # k éléments
        replace=False,   # SANS remise
        p=probas
    )
    quarts.append(vainc[0])

for i in range(0, len(quarts), 2):
    print(f"{quarts[i]} Vs {quarts[i+1]}\n")
#Semi-finals
print("*** Semi-finals ***:\n")
semis=[]
for i in range (0, len(quarts), 2):

    options = [quarts[i], quarts[1+i]]
    poids = [getcota(quarts[i]), getcota(quarts[1+i])]

    probas = np.array(poids) / sum(poids)
    vainc = np.random.choice(
        options,
        size=1,          # k éléments
        replace=False,   # SANS remise
        p=probas
    )
    semis.append(vainc[0])

print(f"{semis[0]} Vs {semis[1]}\n\n{semis[2]} Vs {semis[3]}\n")

#Final:
print("***Final*** 🔥:\n")
fin=[]
for i in range (0, len(semis), 2):

    options = [semis[i], semis[i+1]]
    poids = [getcota(semis[i]), getcota(semis[i+1])]

    probas = np.array(poids) / sum(poids)
    vainc = np.random.choice(
        options,
        size=1,          # k éléments
        replace=False,   # SANS remise
        p=probas
    )
    fin.append(vainc[0])

print(f"{fin[0]} Vs {fin[1]}\n")

#Winner
print("Winner\n")
options = [fin[0], fin[1]]
poids = [getcota(fin[0]), getcota(fin[1])]

probas = np.array(poids) / sum(poids)
win = np.random.choice(
    options,
    size=1,
    replace=False,
    p=probas
)
print(f"🔥 Winner 🔥:{win[0]}")


