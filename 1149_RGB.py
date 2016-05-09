N = int(raw_input())
smallest = []
smallest.extend([int(x) for x in raw_input().split()])

for case in range(N-1):
    R, G, B = [int(x) for x in raw_input().split()]
    smallestR = min(R+smallest[1], R+smallest[2])
    smallestG = min(G+smallest[0], G+smallest[2])
    smallestB = min(B+smallest[0], B+smallest[1])
    smallest = [smallestR, smallestG, smallestB]
 
print (min(smallest[0], smallest[1], smallest[2]))