n = int(raw_input())
maxnum = 2000
mod = 100999
dp = []
for i in range(2002):
    dp.append(0)

dp[0] = 1
for i in range(1, maxnum+1):
    for j in range(maxnum, i-1, -1):
        dp[j] = (dp[j]+dp[j-i]) % mod

while n > 0:
    n -= 1
    x = int(raw_input())
    print dp[x]