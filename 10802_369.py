clap = raw_input().split()
cnt = 0
for i in range(int(clap[0]), int(clap[1])+1):
    if i % 3 == 0:
        cnt += 1

    else:
        num = str(i)
        for j in range(len(num)):
            if (int(num[j]) % 3 == 0) and (int(num[j]) != 0):
                cnt += 1
                break
            else:
                continue
        continue

print cnt % 20150523
