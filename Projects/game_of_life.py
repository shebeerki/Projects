import pygame , random , sys

wr, hr = 10, 10
size = 320, 320
rows = size[1]/hr
columns = size[0]/wr
limit = int(sys.argv[1])

red = 255, 0, 0 
white = 255, 255, 255

array = [[0 for i in range(columns)] for j in range(rows)]
neighbour_array = [[0 for i in range(columns)] for j in range(rows)]

class Initial_Window(object):
	'''This class creates a display surface with 
	random rectangular boxes'''

	def __init__(self, size, color ):
		self.size = size  	#initialise size of display
		self.color = color	#initialise color of rectangle
		self.s = 0		#initialise surface variable
		
	def rand(self, i, j):
		'''This function returns random value of 
		first argument multiplied by second argument'''
		
		return j*random.choice(range(i))
 

	def initial_surface(self):
		'''This function creates a display surface 
		and return it through initialised variable self.s '''
		
		self.s = pygame.display.set_mode(self.size)
		pygame.display.update()
		return self.s
		
	def initial_pattern(self):
		'''This function calls the function initial_surface() 
		and randomly draw rectangles of width 'wr',
		height 'hr' and updates display surface '''
		
		self.s = self.initial_surface()	
		self.s.fill(white)
		pygame.display.update()
		for i in range(limit):
			pygame.draw.rect(self.s, self.color,
 			(self.rand(rows, hr), self.rand(columns, wr), wr, hr))
			pygame.display.update()
			pygame.time.delay(3)
		return self.s	
	

class Changing_Window(Initial_Window):
	'''This class inherits traits from class Initial_window'''
  	def __init__(self, rows, columns):
		self.size = size
		self.color = red
		self.rows = rows	#initialise rows in array 
		self.columns = columns	#initialise columns in array
		self.array = array	#initialise array of live and dead 
		self.neighbour_array = neighbour_array #initialise array 
					#representing number of neighbours
       		self.s = super(Changing_Window, self).initial_pattern()
		'''calling function from parent class Initial_window from 
		child class Changing_Window to get the 
		display surface with random rectangles 
		'''

 	def get_rect(self, wr, hr):
		'''This function finds the color present in the 
		rectangle area and returns array representing 
		'1' for color and '0' for white'''
		self.s.unlock()	#easy self.s surface pixel access
		for i in range(self.rows):	#scanning through the height of display
			for j in range(self.columns):#scanning through width 
				if self.s.get_at((j*wr, i*hr)) == (255, 0, 0, 255):
					self.array[i][j] = 1 #setting array element =1
		return self.array
	
	def try_it(self, r, c, k, l, num):
		'''The cells in the boundary areas of display surface
		didn't have all 8 neighbouring cells, so using the loops
		we will get IndexError. To make code run without Errors, 
		this exceeption is used  '''
		try:
			if self.array[r+k][c+l] == 1:
			    	num += 1
     	   		if self.array[r-k][l-c] == 1:
           			num +=1
     		except IndexError:
      			pass
		return num


  	def num_neighbours(self, r, c):
		'''This function finds the number of neighbours of an individual cell
		also range(2) is used because only change in index of neighbouring cell
		with the cell in problem will be 0 or 1 in rowwise and columntwise'''
    		num = 0
     		for k in range(2):	
     			for l in range(2):
      				if (r, c) != (k+r, l+c) or (r, c) != (r-k, l-c):	
					num = self.try_it(r, c, k, l, num)# calling try function
		return num

 	def neighbour_array_make(self):
		'''This function makes an array filled with the number of 
		neighbours around the corresponding cell. Here calling of 
		function num_neighbours takes place
		'''
      		for i in range(self.rows):
       			for j in range(self.columns):
           			self.neighbour_array[i][j] = self.num_neighbours(i,j)
    		return  self.neighbour_array # returns array of number of neighbours 

	def check_live_or_dead(self, i, j):
		'''This will check the status of cell in the next generation 
		depending on the current status like live, dead
		'''
     		if self.array[i][j] == 1:
      			if self.neighbour_array[i][j] < 2 or self.neighbour_array[i][j] >3 :
              			self.array[i][j]=0
          		else:
              			self.array[i][j]=1
   		elif self.array[i][j] == 0 and self.neighbour_array[i][j]==3:
           		self.array[i][j]=1
       		else:
        		pass
		return 0

  	def compute_nextgen(self):
		'''Returns an array indicating next generation  indiacting 
		dead as '0' and live as '1' . This array is used for drawing 
		patterns of rectangles in the next generation
		'''
     		for i in range(self.rows):
        		for j in range(self.columns):
            			self.check_live_or_dead(i, j)#calling check_live_or_dead
      		return self.array

 	def changing_pattern_make(self):
		'''Using self.array the array indicating population, draws pattern of
		rectangles and update it to display surface and returns display surface through self.s
		'''
		self.s.fill(white)
		pygame.display.update()
		for i in range(self.rows):
       			for j in range(self.columns):
                		if self.array[i][j] == 1:
             				w=pygame.draw.rect(self.s, red, (j*wr, i*hr, wr, hr))
					pygame.display.flip()
		pygame.display.flip()
		pygame.time.delay(50)
       		return 0	
	

	def quit_or_not(self):
		'''This function quits the program from executing inifinitely'''
   		for event in pygame.event.get():
        		if event.type == pygame.QUIT: sys.exit()
      		return 0

w = Initial_Window(size, red)		#making object w from class
c = Changing_Window(rows, columns)#making object c from class

while 1:	
	c.quit_or_not()			#check if quited			
	c.get_rect(wr, hr)		#check the color and make array
	c.neighbour_array_make()	#check neighbours, make array of neighbours
	c.compute_nextgen()		#check number of neighbours, make next generation array   
	c.changing_pattern_make()	#from array, make pattern
	pygame.display.update()		#update whole display
	pass











