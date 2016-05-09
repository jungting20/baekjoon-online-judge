def GCD(A, B):
    if B == 0:
        return A

    return GCD(B, A % B)

A, B = map(int, raw_input().split())

if A > B:
    A, B = B, A

comDivisor = GCD(A, B)

print('1' * comDivisor)