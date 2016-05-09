# -*- coding: utf-8 -*-

number = 10
greeting = '안녕하세요'
place= '문자열 포맷의 세계'
welcome = '환영합니다'

base= '{}번 손님, {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome)
print number, '번 손님', greeting, '.', place, '에 오신 것을 ', welcome, '!'
print base
print new_way