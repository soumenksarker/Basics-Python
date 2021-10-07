def print_max(x, y):
   '''Print the maximum of numbers.

    The two value must be in integers.'''
    #convert the value in integers if possible
   x = int(x)
   y = int(y)
   if x > y:
     print('x is the greater', x)
   else:
     print ('y is the greater', y)
print_max(3,5)
print(print_max.__doc__)

