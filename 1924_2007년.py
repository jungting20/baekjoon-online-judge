x, y = map(int, raw_input().split())
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = y-1
b = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for i in range(x):
    ans += a[i]
print b[ans % 7]
# if ans % 7 == 0:
#     print "MON"
# elif ans % 7 == 1:
#     print "TUE"
# elif ans % 7 == 2:
#     print "WED"
# elif ans % 7 == 3:
#     print "THU"
# elif ans % 7 == 4:
#     print "FRI"
# elif ans % 7 == 5:
#     print "SAT"
# else:
#     print "SUN"