# -*- coding: utf-8 -*-

# self number 구하기
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어 d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가
# 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 이하인 모든 셀프 넘버들의 합을 구하라.

N = 31
ori_number =[]
gen_number =[]

for number in range(1, N+1):
    ori_number.append(number)

# print (ori_number)
for number in range(0, N):
    temp_sum = 0 # 부분합 계산을 위함
    i = ori_number[number] # i 는 자릿수 계산을 위함
    temp_sum = temp_sum + i # 현재 수인 n(i)는 무조건 더함
    # print("first temp_sum",temp_sum)

    temp = 0 # temp 는 오리지널 숫자를 나누는 중간 값을 보관하기 위함

    while i > 9 : # 10보다 작으면 마지막 자리수만 (i)를 더하고 종료할 것임
        temp = i # 나누어진 값을 계산하기 위한 용
        i = (int)(i/10) # 첫번째 자리수 빼고 나머지 값을 저장함
        # print("next i",i)
        while temp > 9:
            temp = (int)(temp%10) # 10보다 작을때 까지 나눠서 첫번째 자리수를 구함
        # print("temp_sum + temp :",temp_sum,temp)
        temp_sum = temp_sum + temp
    # print("last digit ",i)

    temp_sum = temp_sum + i # 10보다 작으면 마지막 자리수만 (i)를 더하고 종료할 것임
    gen_number.append(temp_sum)
# print(ori_number)
# print(gen_number)
gen_number.sort()
sum = 0
ori_number_pivot = 0
gen_number_pivot = 0
# 오리지널 넘버와 제너레이트 된 숫자를 피벗으로 비교하여 self sumber인지 아닌지 판단할 거임
# 파이썬 자체에 간결한 코드로도 쉽게 해결가능 아래 예시는 좋은 코드는 아님
while ori_number_pivot < N:
    # print(ori_number[ori_number_pivot],gen_number[gen_number_pivot])
    if ori_number[ori_number_pivot]< gen_number[gen_number_pivot]:
        # print ("self number",ori_number[ori_number_pivot])
        sum = sum + ori_number[ori_number_pivot]
        # print (sum)
        ori_number_pivot = ori_number_pivot + 1
    elif ori_number[ori_number_pivot]>gen_number[gen_number_pivot]:
        gen_number_pivot = gen_number_pivot + 1
    else:
        ori_number_pivot = ori_number_pivot + 1
        gen_number_pivot = gen_number_pivot + 1
print(sum)


