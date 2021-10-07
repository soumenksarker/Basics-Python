x = 50
def func():
       global x
       print ('x is', x)
       x = 2
       print ('now change value is x to',x)
func()
print('the function value is x=', x)
