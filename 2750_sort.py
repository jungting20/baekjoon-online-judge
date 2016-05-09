import time

start_time = time.time()

n = int(raw_input())
list = []
for i in range(n):
    list.append(int(raw_input()))

list.sort()

for i in range(n):
    print list[i]
end_time = time.time()

print end_time - start_time