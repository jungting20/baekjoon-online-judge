N = int(raw_input())
list = [map(int, raw_input().split()) for i in range(N)]

for i in range(N):
    list[i].reverse()
list.sort()
for i in range(N):
    list[i].reverse()
for i in range(N):
    print list[i][0], list[i][1]