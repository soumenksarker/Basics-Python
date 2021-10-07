number = 23
run = True
while run:
    
    num = int(input('plz enter a number '))
    if num == number:
        print ('U guessed it')
        run = False
    elif num < number :
        print ('sorry your guess is lower')
    else:
        print ('sorry your guess is higher, try another') 
else:
    print ('the while loop is over')
print ('done')
