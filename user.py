from tkinter import *

class Maze():
	def __init__(self, width, height, circle_width = 50):
		#intialize geometric constants 
		self.height = height
		self.width = width
		self.circle_width = circle_width

		#create the window
		window = Tk()
		window.geometry(str(height) + 'x' + str(width))
		self.window = window

		#create the canvas
		canvas = Canvas(window, width=width, height=height)
		canvas.pack()
		self.canvas = canvas

		#create two very simple maze lines
		canvas.create_line(0, height*1/3, width*2/3, height*1/3)
		canvas.create_line(width, height*2/3, width*1/3, height*2/3)

		#create a starting circle
		print(height)
		print(width // 2 - circle_width) 
		print(width // 2 + circle_width) 
		print(height - 2 * circle_width)

		origin = ((width - circle_width) // 2, height - circle_width - 10)
		c = canvas.create_oval(origin[0], origin[1],
							   origin[0] + circle_width, origin[1] + circle_width,
							   fill="red")

		# height, width // 2 - circle_width,  # // is explicit floor division in python
		# 	 		  height, width // 2 + circle_width,           # canvas.create_oval requires integer values
		# 		      height - 2 * circle_width, width // 2 - circle_width,
		# 		      height - 2 * circle_width, width // 2 + circle_width)
		self.c = c

	def move_circle(self, x, y):
		#move the circle by the specified amounts
		self.canvas.move(self.c, x, y)

if __name__ == '__main__':
	m = Maze(400, 400, 50)

	s = input('--> ');

	while(s != "exit"):
		if("l" in s):
			m.move_circle(10,0)
		elif("h" in s):
			m.move_circle(-10,0)
		elif("j" in s):
			m.move_circle(0,-10)
		elif("k" in s):
			m.move_circle(0,10)
		else:
			pass

		s = input('--> ');