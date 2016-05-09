# l, r = map(int, raw_input().split())
# ans = 10
# for i in xrange(l, r+1):
#     cnt = 0
#     a = str(i)
#     for j in xrange(len(a)):
#         if a[j] == '8':
#            cnt += 1
#     if ans > cnt:
#         ans = cnt
# print ans
L, R = [x for x in raw_input().split()]
#1 <= L <= R <= 2,000,000,000

eight = 0
if (len(L) == len (R)):
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                eight += 1
        else:
            break

print (eight)