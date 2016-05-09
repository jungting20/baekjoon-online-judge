list_a= map(int, raw_input().split())
list_b= map(int, raw_input().split())
cnt_a=0
cnt_b=0
for i in range(10):
    if list_a[i] > list_b[i]:
        cnt_a+=1
    elif list_a[i] < list_b[i]:
        cnt_b+=1
    else:
        continue
if cnt_a > cnt_b:
    print 'A'
elif cnt_a < cnt_b:
    print  'B'
else:
    print 'D'