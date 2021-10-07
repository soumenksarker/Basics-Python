x = 50
def funct(x):
    print ('x is', x)
    x = 2
    print ('x here is local',x)
funct(x)
print('x is still unchanged',x)
