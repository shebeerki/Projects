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
		w1 = Wire('wire1', self.b, "not1")
		w2 = Wire("wire2", self.a, "and1")
		n1 = Not("not1", w1.woper())
		w3 = Wire("wire3", n1.nprints(), "and1")
		a1 = And("and1", w1.woper(), n1.noper())
		w4 = Wire("wire4", self.b, "and2")
		w5 = Wire('wire5', self.a, "not2")
		n2 = Not("not2", self.a)
		w6 = Wire("wire6", n2.nprints(), "and2")
		a2 = And("and2", n2.noper(), w2.woper())
		w7 = Wire("wire7", a1.aprints(), "or")
		w8 = Wire("wire8", a2.aprints(), "or")
		o  = Or("xor1", a1.aoper(), a2.aoper())
		o.oprints()
		return 0

	def working(self):
		if (self.a, self.b) != (a, b):
			self.change = 1
		else:
			self.change = 0
			print "inputs are not changed, so output are the previous ones\n"
		return self.change


class Wire(Logic):
	
		def __init__(self, name, a_now, gate = None):
			self.name = name
			self.a_now = a_now
			self.gate = gate
			print "%s passes    %d ==>   %s\n"%(self.name, self.a_now, self.gate)

		def woper(self):
			return self.a_now


(a, b) = input("enter the inputs a and b where\
	a, b are either binary 1 or 0\n")
c = Xor('xor1', a, b, 0)
c.oper()
while 1:
	a = c.a
	b = c.b
	c.a, c.b = input("enter the inputs a and b\n")
	if c.working(a, b):
		c.oper()
	pass
