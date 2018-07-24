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

def check(p):
    return p[0]**2 + p[1]**2 <= 1

print(check(ranpoint()))

print(list(map(check,points(50))))

N = 500000
k = 0
for x in map(check,points(N)):
    if x: k+=1
print(k)

print(k/N*4)

