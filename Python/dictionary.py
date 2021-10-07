#ab is short for address book
ab = { 'swaroop' : 'swaroop@gmail.com',
       'supto'   : 'soumensarker.ice.iu.bd@gmail.com',
       'masud'   : 'masud@gmail.com',
       'spammer' : 'spammer@hotmail.com'
       }
print ('the mail address of supto is', ab['supto'])
del ab['spammer']
#print ('item 2 is', ab[1])
print ('\nthere are {} contacts in the address\n'.format(len(ab)))
for name, address in ab.items():
 print ('Contact {} at {}'. format(name, address))
#adding key value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
 print ('Guido address is ', ab['Guido'])
