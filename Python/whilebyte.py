number = 23
running = True
while running:
    guess = int(input('enter any number'))
    if number == guess:
         print('your imagination is right')
         print ('but you have not got any prize')
         runnig = False
    elif guess<number:
         print ('your thinking is low')
         print ('try another')
    else:
         print ('your thinking is high')
else:
    print('the while loop is over')
print('done')
input('press enter to exit')      
