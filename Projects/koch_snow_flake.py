import pygame.draw 
import math 
import pygame.display
import sys

size = 640, 640
red = 255, 0, 0
black = 0, 0, 0

a = 200, 360

le = input("length of side of equilateral triangle\n")
s = pygame.display.set_mode(size)
pygame.display.update()


def fractal(le, state):
	e = lines(le, state, 0, a)
	i = lines(le, state, 120, e)
	h = lines(le, state, 240, i)
	
def lines(le, state, angle, p):
	if state == 0:
		e = point(le, angle, p)
		print e
		pygame.draw.line(s, red, p, e)
		pygame.display.update()
		return e
	else:
		h = lines(le / 3, state - 1, angle, p)
		i = lines(le / 3, state - 1, angle - 60, h)
		j = lines(le / 3, state - 1, angle + 60, i)
		k = lines(le / 3, state - 1, angle, j)
		return k
		

def point(le, angle, a):
	angle = angle * 3.14 / 180
	w = math.cos(angle) * le
	h = math.sin(angle) * le
	print w, h
	return a[0] + w, a[1] - h

def escape():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	return 0


while 1:
	for i in range(5):
		fractal(le, i)
		pygame.time.delay(300)
		s.fill(black)
		escape()
	pass
