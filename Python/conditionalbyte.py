number = 23
guess = int(input('enter any number'))
if(guess ==number):
     print('your answer is correct')
     print ('but u have not get any prize')
elif(guess<number):
         print ('sorry your guess is lower')
         print ('try another')
else:
         print ('sorry your guess is higher')
         print('try another')
input('plz press enter to exit')
