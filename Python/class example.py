class person:
     def __init__(self,name,age):
      self.name = name
      self.age  = age
     def say_hi(self):
      print ('hello how are u, my name is',self.name,' and my age is', self.age)

person(input('enter a name'), int(input('enter your age'))).say_hi()

