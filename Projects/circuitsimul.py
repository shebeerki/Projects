class Wire :
    
    	def __init__ (self, gate, name, printvalue = 0,  latch = 0) :
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

   	def connect (self, inputs) :
        	for input in self.arr_inputs(inputs) : self.inputs.append(input)
		return 0

   	def setvalue(self, value) :
        	if self.value == value : 
			return 
        	self.value = value          
       	 	if self.latch: 
			self.gate.oper()
		if self.printvalue:
        		print "Connector %s-%s set to %s" % (self.gate.name,self.name,self.value)
        	for con in self.inputs : 
			con.setvalue(value)
		return 0		

class Gate :
    
    def __init__ (self, name) :
        self.name = name
         
class Gate1(Gate):

	def __init__(self,name):
		Gate.__init__(self, name)
		self.A = Wire(self, 'A', latch = 1)
		self.B = Wire(self, 'B')

class Not (Gate1) :        
    
	def __init__ (self, name) :
        	Gate1.__init__ (self, name)
	
	def oper (self) : 
    		self.B.setvalue(not self.A.value)

class Gate2 (Gate) :  
    	
	def __init__ (self, name) :
        	Gate.__init__ (self, name)
        	self.A = Wire(self,'A', latch = 1)
        	self.B = Wire(self,'B', latch = 1)
  		self.C = Wire(self,'C')

	def oper(self):
		return 0

class And (Gate2) :     
    
    	def __init__ (self, name) :
        	Gate2.__init__ (self, name)
    
    	def oper (self) : 
    		self.C.setvalue(self.A.value and self.B.value)
		return 0

class Or (Gate2) :        
    
    	def __init__ (self, name) :
        	Gate2.__init__ (self, name)
    
    	def oper (self) : 
    		self.C.setvalue(self.A.value or self.B.value)
		return 0

class Xor (Gate2) :
    	
	def __init__ (self, name) :
        	Gate2.__init__ (self, name)
        	self.A1 = And("A1")
        	self.A2 = And("A2")
        	self.N1 = Not("N1")
        	self.N2 = Not("N2")
        	self.O1 = Or ("O1")
        	self.A.connect    ([ self.A1.A, self.N2.A])
        	self.B.connect    ([ self.N1.A, self.A2.A])
        	self.N1.B.connect ([ self.A1.B ])
        	self.N2.B.connect ([ self.A2.B ])
        	self.A1.C.connect ([ self.O1.A ])
        	self.A2.C.connect ([ self.O1.B ])
        	self.O1.C.connect ([ self.C ])


x1 = Xor("xor")
x1.C.printvalue = 1
x1.A.printvalue = 1
x1.A.setvalue(1)
x1.B.printvalue = 1
x1.B.setvalue(1)
