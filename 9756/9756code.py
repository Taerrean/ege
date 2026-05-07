def arrange_meetings(mass):
    mass.sort(key=lambda x: x[1])
    t = 0
    every_end = []
    while mass:
        every_end.append(mass[0]) if max(mass)[0] >= mass[0][1] else every_end.append(mass[-1])
        t = every_end[-1][1]
        mass = [meet for meet in mass if meet[0] >= t and meet not in every_end]
    return [len(every_end), t]
f = open('26_9756.txt')
n = int(f.readline())
data = []
for line in f:
    n, k = [int(k) for k in line.split()]
    data.append([n, k])
print(arrange_meetings(data))
