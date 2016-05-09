def collatz(num):
    global count
    if num == 1:
        return
    elif num % 2 == 0:
        num /= 2
        collatz(num)
    else:
        num = num*3 + 1
        collatz(num)
    count += 1

maxNum=0
thatNum=0
for i in range(3599, 3610):
    count = 0
    collatz(i)
    if maxNum<count:
        maxNum = count
        thatNum = i
    print i, thatNum, count