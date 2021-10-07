#recommended always using parenthesis
#to indicate start and end of tuple
#even though parenthesis is optional
#explicit is better than implicit
zoo = ('python', 'elephant', 'penguin')
print  ('number of the elements', len(zoo))
new_zoo = 'monkey', 'camel',zoo
print ('number of animals are in new zoo', len(new_zoo))
print ('all animals in new zoo', new_zoo)
print ('animal brought from old zoo are',new_zoo[2])
print ('last animal brought form old zoo is ', new_zoo[2][2])
print ('number of animal in new zoo is',len(new_zoo))-1+len(new_zoo[2])

#here u just use the last line for finding the length of new_zoo
