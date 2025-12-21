
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
best_thrds = np.random.choice(
    options,
    size=4,          # k éléments
    replace=False,   # SANS remise
    p=probas
)


print(f"Best thirds:\n{best_thrds[0]} - {best_thrds[1]} - {best_thrds[2]} - {best_thrds[3]}\n")    

#eliminatories
X = "mazlt"
huits = [[final_standing[0][1], final_standing[2][1]],
      [final_standing[3][0], X],
      [final_standing[1][0],X],
       [final_standing[5][0], final_standing[4][1]],
       [final_standing[1][1], final_standing[5][1]],
       [final_standing[0][0], X],
       [final_standing[4][0], final_standing[3][1]],
        [final_standing[2][0], X]]

def getgrp(team):
    for i in Initial_standing:
        if team in i:
            return Initial_standing.index(i)+1

def getcota(team):
            g = getgrp(team)-1
            return Cotas[g][Initial_standing[g].index(team)]

for i in best_thrds:
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
            huits[7][1]=i
        
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

