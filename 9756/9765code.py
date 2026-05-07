def arrange_meetings(mass):
    t = 0
    every_end = []
    while mass:
        every_end.append(mass[0]) if not all(x < min(mass, key= lambda x: x[1])[1] for x, y in mass) else every_end.append(max(mass, key= lambda x: x[1]))
        t = every_end[-1][1]
        a = [meet for meet in mass if meet[0] >= t and meet not in every_end]
        mass = a
    return [len(every_end), t]
f = open('26_9756.txt')
n = int(f.readline())
data = []
for line in f:
    n, k = [int(k) for k in line.split()]
    data.append([n, k])
data.sort(key =lambda x: x[1])
print(arrange_meetings(data))
