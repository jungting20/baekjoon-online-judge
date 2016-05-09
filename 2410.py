maxnum = 2000
mod = 1000000000
x = int(raw_input())


dp = []
for i in xrange(1000011):
    dp.append(0)

a = []
for i in xrange(0, 21):
    a.append(2**i)

for i in xrange(0, 21):
    if a[i] <= x:
        dp[a[i]] += 1

    for j in xrange(a[i], x+1):
        dp[j] += dp[j-a[i]]
        dp[j] %= mod

print dp[x]