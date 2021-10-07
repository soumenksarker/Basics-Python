class Robot:
    '''Represents a Robot with a name'''
    # a class variable counting the number of robot
    population = 0
    
    def __init__(self, name):
       '''initilize the data'''
       self.name = name
       print ("(initializing{})".format(self.name))
       #when the robot is created the person is added to the population
       Robot.population += 1
       
    def die(self):
       '''i am dying'''
       print ("(initializing person {} destroid)". format(self.name))
       #when the person destroyed
       #it mynus the robot population
       Robot.population -= 1

       if Robot.population == 0:
        print ('the {} robot is last one'. format(self.name))
       else: 
        print ('there are {:d} robots still working'. format(Robot.population))

    def say_hi(self):
       '''Greating by the Robot,
       well ,they can do that'''
       print ("Greatings my masters call me {}.".format(self.name))
    @classmethod
    def how_many(cls):
     '''The current population'''
    
     print ("we have {:d} robots".format(cls.population))
    
droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print ('\nRobot can do some work\n')

print ('\n Robot finished there work, so lets destroy them\n')
droid1.die()
droid2.die()
Robot.how_many()
