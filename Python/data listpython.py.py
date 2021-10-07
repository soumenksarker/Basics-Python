shoplist = ['banana','carrot','mango', 'apple']
print ('the length of items of my list', len(shoplist))
print('this items are')#end = ' ') here is use for give a space after item of any list
for item in shoplist:
 print (item) #end = ' ')
print ('i also have to buy some rice')
shoplist.append('rice')
print ('now myshoplist is ', shoplist)
print ('i wanna sort my list')
shoplist.sort()
print ('as we can see here my shorted list is', shoplist)
 
print ('the  first item i buy', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print ('i bought the old item', olditem);
print ('now my shoplist is ', shoplist)
 
 

