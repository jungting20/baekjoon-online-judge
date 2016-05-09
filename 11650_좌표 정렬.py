N = int(raw_input())
list = [map(int, raw_input().split()) for i in range(N)]
list.sort()
for i in range(N):
    print list[i][0], list[i][1]