# --coding:utf-8

class Man:
  def __init__(self,name):
    self.name =name
    print("Initialized!")

  def hello(self):
    print("Hello "+self.name + "!")

  def goodbye(self):
    print("Good-bye "+self.name +"!")

print("start")
m =Man("Davide")
print("set David")
m.hello()
m.goodbye()
