def cake(N):
    if 360 % N == 0:
        a = 'y'
    else:
        a = 'n'
        
    if N > 360:
        b = 'n'
    else:
        b = 'y'
        
    if N > 26:
        c = 'n'
    else:
        c = 'y'
        
    return f'{a} {b} {c}'
        
        


N = int(input())
print(cake(N))




