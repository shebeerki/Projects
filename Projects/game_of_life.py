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
       
	def __init__(self, size, color ):
		self.size = size  
		self.color = color
		self.s = 0
		
	def rand(self, i, j):
		return j*random.choice(range(i))
 

	def initial_surface(self):
		self.s = pygame.display.set_mode(self.size)
		pygame.display.update()
		return self.s
		
	def initial_pattern(self):
		self.s = self.initial_surface()	
		self.s.fill(white)
		pygame.display.update()
		for i in range(limit):
			pygame.draw.rect(self.s, self.color,
 							(self.rand(rows, wr), self.rand(columns, hr), wr, hr))
			pygame.display.update()
			pygame.time.delay(3)
		return self.s	
	

class Changing_Window(Initial_Window):

  	def __init__(self, size, color, rows, columns):
		self.size = size
		self.color = color
		self.rows = rows
		self.columns = columns
		self.array = array
		self.neighbour_array = neighbour_array
       		self.s = super(Changing_Window, self).initial_pattern()
	
 	def get_rect(self, wr, hr):
		self.s.unlock()
		for i in range(self.rows):
			for j in range(self.columns):
				if self.s.get_at((j*wr, i*hr)) == (255, 0, 0, 255):
					self.array[i][j] = 1
		return self.array
	
	def try_it(self, r, c, k, l, num):
		try:
			if self.array[r+k][c+l] == 1:
			    	num += 1
     	   		if self.array[r-k][l-c] == 1:
           			num +=1
     		except IndexError:
      			pass
		return num


  	def num_neighbours(self, r, c):
    		num = 0
     		for k in range(2):
     			for l in range(2):
      				if (r, c) != (k+r, l+c) or (r, c) != (r-k, l-c):	
					num = self.try_it(r, c, k, l, num)
		return num

 	def neighbour_array_make(self):
      		for i in range(self.rows):
       			for j in range(self.columns):
           			self.neighbour_array[i][j] = self.num_neighbours(i,j)
    		return  self.neighbour_array

	def check_live_or_dead(self, i, j):
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
     		for i in range(self.rows):
        		for j in range(self.columns):
            			self.check_live_or_dead(i, j)
      		return self.array

 	def changing_pattern_make(self):
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
   		for event in pygame.event.get():
        		if event.type == pygame.QUIT: sys.exit()
      		return 0



w = Initial_Window(size, red)
c = Changing_Window(size, red, rows, columns)

while 1:
	c.quit_or_not()
	c.get_rect(wr, hr)
	c.neighbour_array_make()
	c.compute_nextgen()
	c.changing_pattern_make()
	pygame.display.update()
	pass











