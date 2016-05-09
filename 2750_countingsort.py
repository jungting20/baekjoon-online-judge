import time

start_time = time.time()

n = int(raw_input())
list = []
for i in range(n):
    list.append(int(raw_input()))

def counting_sort(A):
    if min(A) < 0:
        raise
    i, n, k = 0, len(A), max(A)+1
    C=[0]*k
    for j in range(n):
        C[A[j]]=C[A[j]]+1
    for j in range(k):
        while C[j] > 0:
            (A[i], C[j], i) = (j, C[j]-1, i+1)

counting_sort(list)

for i in range(n):
    print list[i]

end_time = time.time()
print end_time - start_time