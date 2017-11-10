class A(object): 
	def __method(self): 
		print ("I'm a method in A" )
	def method(self): 
		self.__method() 

a = A() 
a.method()



class B(A): 
	def __method(self): 
		print ("I'm a method in B" )

b = B() 
b.method()