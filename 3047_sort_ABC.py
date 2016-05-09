n, m, l = map(int, raw_input().split())
abc = raw_input()

list = []
list.append(n)
list.append(m)
list.append(l)

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

ans_list = [1,1,1]

for i in range(3):
    if abc[i] == 'A':
        ans_list[i] = list[0]
    elif abc[i] == 'B':
        ans_list[i] = list[1]
    else:
        ans_list[i] = list[2]

print ans_list[0], ans_list[1], ans_list[2]
