a = raw_input()
ans=''
for i in range(len(a)):
    if 90>=ord(a[i])>=65:
        ans+=a[i]
print ans

