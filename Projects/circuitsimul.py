class Logic:
	
	def __init__(self, name, a, b, change = 0):
		self.name = name
		self.a = a
		self.b = b
		self.change = change

class And(Logic):

	def __init__(self, name, a, b):
		Logic.__init__(self, name, a, b)
		
	def aoper(self):
		return self.a and self.b

	def aprints(self):
		print "output of %s gate is %d\n"%(self.name, self.aoper())
		return self.aoper()

class Or(Logic):
	
	def __init__(self, name, a, b):
		Logic.__init__(self, name, a, b)

	def ooper(self):
		return self.a or self.b

	def oprints(self):
		print "output of %s gate is %d\n"%(self.name, self.ooper())
		return self.ooper()

class Not(Logic):

	def __init__(self, name, a):
		Logic.__init__(self, name, a, 0)

	def noper(self):
		return not self.a

	def nprints(self):
		print "output of %s is %d\n"%(self.name, self.noper())
		return self.noper()

class Xor(Logic):
	def __init__(self, name, a, b, change = 0):
		Logic.__init__(self, name, a, b)
		self.change = change
	
	def oper(self):
		n1 = Not("not1", self.b)
		a1 = And("and1", self.a, n1.nprints())
		n2 = Not("not2", self.a)
		a2 = And("and2", n2.nprints(), self.b)
		o  = Or("xor1", a1.aprints(), a2.aprints())
		o.oprints()
		return 0

	def working(self):
		a = self.a
		b = self.b
		self.a, self.b = input("enter the inputs a and b\n")
		if (self.a, self.b) != (a, b):
			self.change = 1
		else:
			self.change = 0
			print "inputs are not changed, so output are the previous ones\n"
		return self.change

	def infinite(self):
		self.oper()
		while 1:
			if self.working():
				self.oper()
		return 0
(a, b) = input("enter the inputs a and b where\
	a, b are either binary 1 or 0\n")
c = Xor('xor1', a, b, 0)
c.infinite()
