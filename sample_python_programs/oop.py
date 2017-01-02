class Employee:
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		print (self.__class__.__name__, "created")
	
	def displayCount(self):
		print ("Total Employees %d" % Employee.empCount)
		
	def displayEmployee(self):
		print ("Name:", self.name, ", Salary:", self.salary)
	
	def __del__(self):
		class_name = self.__class__.__name__
		print (class_name, "destroyed")

def cls_test():      
    emp1 = Employee("Ziggler", 125000)
    emp2 = Employee("Bret", 12302010)
    
    emp1.displayEmployee()
    emp2.displayEmployee()
    
    emp2.displayCount();
    
if __name__ == '__main__':
    cls_test()