def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        n = oldm%oldn
    return n
print (gcd(32,16))

        
