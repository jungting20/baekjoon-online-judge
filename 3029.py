# -*-coding: utf-8 -*-
# current time 현재시각
chour, cmin, csec = [int(x) for x in raw_input().split(':')]
# estimate time 나트륨을 던질 시간
ehour, emin, esec = [int(x) for x in raw_input().split(':')]
# waiting ime 기다려야 하는 시간
whour, wmin, wsec = 0, 0, 0
 
# 초, 분, 시 순으로 계산
wsec += esec - csec
if wsec < 0:
    wsec += 60
    wmin -= 1
 
wmin += emin - cmin
if wmin < 0:
    wmin += 60
    whour -= 1

whour += ehour - chour
if whour < 0:
    whour += 24
 
# 정인이는 적어도 1초를 기다리며, 많아야 24시간을 기다린다.
if whour == 0 and wmin == 0 and wsec == 0:
    print ("24:00:00")
 
else:
    print "%02d:%02d:%02d" % (whour, wmin, wsec)