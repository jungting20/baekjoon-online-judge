# -*- coding:utf-8 -*-
string = raw_input()
palindrome = True
odd = -1
# 알파벳 개수를 셀 리스트
alphabet = [0 for x in range(26)]

for x in range(len(string)):
    alphabet[ord(string[x])-65] += 1

if len(string) % 2 == 0:
    for x in range(26):
        if (alphabet[x] % 2 == 1):
            palindrome = False

else:
    check = 0
    for x in range(26):
        if (alphabet[x] % 2 == 1):
            check += 1
            odd = x
    if check > 1:
        palindrome = False
if palindrome:
    palinstr = ""   # 팰린드롬의 앞부분
    for x in range(26):
        while (alphabet[x] >= 2):   # 알파벳이 쓰였으면 출력할 팰린드롬의 앞부분에 추가
            # alphabet[x] = 1일 수 있음! 이 경우 나중에 추가해준다.
            palinstr = palinstr + chr(x + 65)
            alphabet[x] -= 2    # 앞부분을 두번 반복해서 정답을 출력해주니 2번 빼주기
    if odd == -1:    # odd의 기본값. 입력길이가 짝수일때
        answer = palinstr + palinstr[::-1]
    else:
        answer = palinstr + chr(odd+65) + palinstr[::-1]
        # string[::-1]은 string을 뒤에서부터 읽어준다
    print (answer)

#팰린드롬이 아닐시
else:
    print("I'm Sorry Hansoo")