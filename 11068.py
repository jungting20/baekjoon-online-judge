def base_converter(num, base):
    lst = list()
    while num > 0:
        lst = [num % base] + lst
        num /= base
    return lst

def is_palindrome(arr):
    for i in xrange(len(arr)/2):
        if arr[i] != arr[-(i+1)]:
            return False
    return True

T = int(raw_input())
for _ in xrange(T):
    num = int(raw_input())
    flag = False
    base=64
    while base > 1 and not flag:
        flag |= is_palindrome(base_converter(num, base))
        base -= 1
    if flag:
        print 1
    else:
        print 0
