f = lambda n, m: m < 1 or n * f(n-1, m-1)//m
print( f( *map( int, raw_input().split() ) ) )