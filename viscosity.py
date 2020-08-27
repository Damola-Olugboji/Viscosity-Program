import math

num = int(input("How many species in this gas mixture? "))
x = [0] * num
M = [0] * num
mu = [0] * num
for i in range(0, num):
    x[i] = float(input("Enter the Molar Fraction: "))
    M[i] = float(input("Enter the Molecular Weight: "))
    mu[i] = float(input("Enter the mu value: "))


def calculate(x, M, mu):
    w, h = num, num
    phi = [[0 for x in range(w)] for y in range(h)]
    xphi = [[0 for x in range(w)] for y in range(h)]
    denominator = [0] * num
    numerator = [0] * num
    viscosity = [0] * num
    for i in range(0, num):
        for c in range(0, num):
            phi[i][c] = get_phi(mu[i], mu[c], M[i], M[c])

    for a in range(0, num):
        for b in range(0, num):
            xphi[a][b] = x[b] * phi[a][b]

    for i in range(0, num):
        denominator[i] = sum(xphi[i])

    for i in range(0, num):
        numerator[i] = x[i] * mu[i]

    for i in range(0, num):
        viscosity[i] = numerator[i] / denominator[i]
    print("\n")
    print("Viscosity [g/cm s]: " + str(round(sum(viscosity), 13)))


def get_phi(mui, muj, mi, mj):
    if mui == muj:
        return 1
    phi = (
        (1 / math.sqrt(8))
        * ((1 + (mi / mj)) ** (-0.5))
        * (1 + ((mui / muj) ** 0.5) * ((mj / mi) ** 0.25)) ** 2
    )
    return phi


calculate(x, M, mu)

"""
x = [0.5226, 0.3048, 0.0659, 0.0900]
M = [2.01588, 28.01, 28.0134, 36.46]
mu = [0.027469092, 0.060326492, 0.059615963, 434.55]


0.0001464707550, 0.0002028770331, 0.0001746432201
"""
