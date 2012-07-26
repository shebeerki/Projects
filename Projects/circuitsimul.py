class Wire:
    
    	def __init__ (self, gate, name, printvalue = 0,  latch = 0):
        	self.value = None
        	self.gate = gate
		self.printvalue = printvalue
        	self.name  = name
        	self.latch = latch
        	self.inputs = []

    	def arr_inputs(self, inputs):
    		if type(inputs) != type([]):
			inputs = [inputs]
   		return inputs

   	def connect(self, inputs):
        	for input in self.arr_inputs(inputs): 
			self.inputs.append(input)
		return 0

   	def setvalue(self, value):
        	if self.value == value: 
			return 
        	self.value = value          
       	 	if self.latch: 
			self.gate.oper()
		if self.printvalue:
        		print "Connector %s-%s set to %s" % (self.gate.name,self.name,bool(self.value))
        	for con in self.inputs: 
			con.setvalue(value)
		return 0		

class Gate:
    
    def __init__ (self, name):
        self.name = name
         
class Gate1(Gate):

	def __init__(self,name):
		Gate.__init__(self, name)
		self.A = Wire(self, 'A', latch = 1)
		self.B = Wire(self, 'B')

class Not(Gate1):        
    
	def __init__(self, name):
        	Gate1.__init__(self, name)
	
	def oper(self): 
		if self.A.value != None:
    			self.B.setvalue(not self.A.value)

class Gate2(Gate):  
    	
	def __init__(self, name):
        	Gate.__init__(self, name)
        	self.A = Wire(self,'A', latch = 1)
        	self.B = Wire(self,'B', latch = 1)
  		self.C = Wire(self,'C')

	def oper(self):
		return 0

class And(Gate2):     
    
    	def __init__(self, name):
        	Gate2.__init__(self, name)
    
    	def oper(self) : 
		if self.A.value != None and self.B.value != None:
    			self.C.setvalue(self.A.value and self.B.value)
		return 0

class Or(Gate2):        
    
    	def __init__(self, name):
        	Gate2.__init__ (self, name)
    
    	def oper(self) : 
		if self.A.value != None and self.B.value != None:
    			self.C.setvalue(self.A.value or self.B.value)
		return 0

class Xor (Gate2):
    	
	def __init__(self, name):
        	Gate2.__init__(self, name)

	def oper(self):
		if self.A.value != None and self.B.value != None:
			self.C.setvalue((self.A.value and not self.B.value) or (not self.A.value and self.B.value))
		return 0

#implementing full adder
x1 = Xor("xor1")
x2 = Xor("xor2")
a1 = And("and1")
a2 = And("and2")
o1 = Or("or1")

	
x1.A.connect([a2.A, x1.A])
x1.B.connect([x1.B, a2.B])
x2.B.connect([x2.B, a1.A])
x1.C.connect([x2.A, a1.B])
a1.C.connect([o1.A])
a2.C.connect([o1.B])
x2.C.printvalue = 1
o1.C.printvalue = 1
cin = 0
while 1:
	a, b = input("enter the inputs a, b \n")
	x1.A.setvalue(a)
	x1.B.setvalue(b)
	x2.B.setvalue(cin)
	cin = o1.C.value
'''the sum and carry out of the full adder is printed
if and only if it will be different from previous sum and 
carry out'''
