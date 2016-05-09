import math
a, b, v = map(float, raw_input().split())
print int(math.ceil((v-b)/(a-b)))