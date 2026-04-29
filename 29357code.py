from math import dist
def centroid(cl):
    m = []
    for dot in cl:
        a = sum(dist(p1[:2], dot[:2]) for p1 in cl)
        m.append([a, dot])
    return min(m)[-1]


f = open('27_B_29357.txt')
data = []
for line in f:
    x, y, t = [k for k in line.split()]
    data.append([float(x), float(y), t])
clusters = []
while data:
    clusters.append([data.pop(0)])
    for d in clusters[-1]:
        close = [x for x in data if dist(x[:2], d[:2]) < 1.5]
        clusters[-1].extend(close)
        for p in close: data.remove(p)
    print(len(clusters[-1]))

centroids = []
for el in clusters:
    centroids.append(centroid(el))
print(centroids)

if f.name == '27_B_29357.txt':
    maxstars = 0
    maxcl = 0
    minstars = 99999
    mincl = 0
    md = 0
    for el in clusters:
        s = 0
        for dot in el:
            if 'G' in dot[2] and 'V' in dot[2]:
                m = max(dist(dot[:2], p1[:2]) for p1 in el if 'G' in p1[2] and 'V' in p1[2] and dot in el)
                if m > md:
                    md = m
            elif 'K' in dot[2] and 'III' in dot[2]:
                s += 1
        if s > maxstars:
            maxstars = s
            maxcl = clusters.index(el)
        elif s < minstars:
            minstars = s
            mincl = clusters.index(el)
    B1 = dist(centroids[mincl][:2], centroids[maxcl][:2]) * 10000
    B2 = md * 10000
    print(B1, B2)
else:
    mi = 0
    mstars = 9999
    Ax = 0
    Ay = 0
    for el in range(len(clusters)):
        if len(clusters[el]) < mstars:
            mi = el
            mstars = len(clusters[el])
    closest = min(dist(centroids[mi][:2], dot[:2]) for dot in clusters[mi] if 'M' in dot[2] and 'III' in dot[2])
    for dot in clusters[mi]:
        if dist(centroids[mi][:2], dot[:2]) == closest and 'M' in dot[2] and 'III' in dot[2]:
            Ax, Ay = [k * 10000 for k in dot[:2]]
            break
    print(Ax, Ay)


