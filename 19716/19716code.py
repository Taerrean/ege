from re import *
from time import *
n = time()
f = open('24.21_19716.txt').readline()
reg1 = r'1{2,}|2{2,}|0{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}'
d = set((x.group() for x in finditer(reg1, f)))
for el in d: f = f.replace(el, 'Z' * len(el))
reg2 = r'Z\d+Z'
m = findall(reg2, f)
ans = max(len(x) for x in m)
for x in m:
    print(x) if len(x) == ans else None
print(ans)
k = time()
print(round(k-n, 5))