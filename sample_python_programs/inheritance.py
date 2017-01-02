class Base:
	baseAtr = 10
	def __init__(self):
		print ("Base class constructor")
	
	def __del__(self):
		print ("Base class destructor")
		
	def setValue(self, value):
		Base.baseAtr = value
	
	def printValue(self):
		print ("Base attribute value: ", Base.baseAtr)
	

class Derived(Base):
	def __init__(self):
		print ("Derived class constructor")
	
	def __del__(self):
		print ("Derived class destructor")

	def derivedMethod(self):
		print ("Derived class method")

def oop_test():
    dObj = Derived ()
    dObj.derivedMethod ()
    dObj.printValue ()
    dObj.setValue (20)
    dObj.printValue ()

if __name__ == '__main__':
    oop_test()	