s = raw_input()
ans = 1
for i in xrange(len(s)):
    if s[i]=='A':
       if ans ==1:
           ans=2
       elif ans ==2:
           ans=1
       else:
           continue
    elif s[i]=='B':
        if ans == 3:
            ans = 2
        elif ans == 2:
            ans = 3
        else:
            continue
    else:
        if ans == 1:
            ans = 3
        elif ans == 3:
            ans = 1
        else:
            continue
print ans