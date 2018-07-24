import random as rnd

def ranpoint():
    return [rnd.random(),rnd.random()]
print(ranpoint())

def points(n):
    m = []
    for i in range(0,n):
        m.append(ranpoint())
    return m

print(points(50))
