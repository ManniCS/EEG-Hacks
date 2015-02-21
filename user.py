# figure out how to redraw stuff on the canvas / pause an animation

import threading
import math
import time
import numpy as np
from tkinter import *

class Maze():
	def __init__(self, width, height, circle_width = 50):
		#intialize geometric constants and thread property
		self.height = height
		self.width = width
		self.circle_width = circle_width
		self.maze = np.zeros([height, width])
		# self.action_icon_display_thread = False

		#create the window
		window = Tk()
		window.geometry(str(width) + 'x' + str(height))
		self.window = window

		#create the canvas
		canvas = Canvas(window, width=width, height=height)
		canvas.pack()
		self.canvas = canvas

		#create five very simple maze lines
		canvas.create_line(0, height*1/6, width - 2*circle_width, height*1/6)
		canvas.create_line(width, height*2/6, 2*circle_width, height*2/6)
		canvas.create_line(0, height*3/6, width - 2*circle_width, height*3/6)
		canvas.create_line(width, height*4/6, 2*circle_width, height*4/6)
		canvas.create_line(0, height*5/6, width - 2*circle_width, height*5/6)

		#update maze representations
		self.addWall(0, height*1/6,  width - 2*circle_width, height*1/6)
		self.addWall(width, height*2/6, 2*circle_width, height*2/6)
		self.addWall(0, height*3/6, width - 2*circle_width, height*3/6)
		self.addWall(width, height*4/6, 2*circle_width, height*4/6)
		self.addWall(0, height*5/6, width - 2*circle_width, height*5/6)

		print(self.maze)

		#create a starting circle
		print(height)
		print(width // 2 - circle_width) 
		print(width // 2 + circle_width) 
		print(height - 2 * circle_width)

		origin = ((width - circle_width) // 2, height - circle_width - 20)
		c = canvas.create_oval(origin[0], origin[1],
							   origin[0] + circle_width, origin[1] + circle_width,
							   fill="red")

		# height, width // 2 - circle_width,  # // is explicit floor division in python
		# 	 		  height, width // 2 + circle_width,           # canvas.create_oval requires integer values
		# 		      height - 2 * circle_width, width // 2 - circle_width,
		# 		      height - 2 * circle_width, width // 2 + circle_width)
		self.c = c

	def process_move(self, x, y):
		self.move_circle(x,y) #move circle

		# if (m.action_icon_display_thread): #process action icon animation
		# 		m.action_icon_display_thead.join()

		# m.action_icon_display_thread = self.ActionIconDisplayThread(x, y, self.canvas)
		# m.action_icon_display_thread.start()

		# self.update_action_icon(x, y)

	def addWall(self, start_x, start_y, end_x, end_y):
		#adds a wall to the internal representation of the maze
		start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y) # convert to ints, if receive float values
		
		if start_x > end_x:
			start_x, end_x = self.swap(start_x, end_x)
		if end_y < start_y:
			end_y, start_y = self.swap(end_y, start_y)

		row_span = end_y - start_y
		col_span = end_x - start_x
		col_per_row = col_span if row_span == 0 else (col_span + 1 / row_span) #round up int div
		curr_x = start_x

		for i in range(start_y, end_y):
			for j in range(0, col_per_row):
				curr_x += 0 if curr_x > end_x else 1
				self.maze[i][curr_x] = 1

	def move_circle(self, x, y):
		#move the circle by the specified amounts
		if self.canvas.
		self.canvas.move(self.c, x, y)

	def update_action_icon(self, x, y):
		#function to be used by thread which updates the icon visualizing latest action

		padding = 10 #padding of icon against side of canvas

		#arrow icon geometric attributes
		arrow_length = 20
		arrow_head_height = 10
		arrow_head_length = 10
		arrow_head_hypotenuse = math.sqrt(arrow_head_height**2 + arrow_head_length**2) #silly parameter requered by tkinter.create_line for arrow drawing
		line_weight = 10
		line_color = "red"

		if (x > 0 and y == 0):
			#setup left arrow
			start_x = self.canvas.winfo_width()
			start_y = arrow_length / 2.0
			end_x = self.canvas.winfo_width() - arrow_length
			end_y = arrow_length / 2.0
		if (x < 0 and y == 0):
			#setup right arrow
			start_x = self.canvas.winfo_width() - arrow_length
			start_y = arrow_length / 2.0
			end_x = self.canvas.winfo_width()
			end_y = arrow_length / 2.0
		if (x == 0 and y > 0):
			#setup up arrow
			start_x = self.canvas.winfo_width() - arrow_length / 2.0
			start_y = arrow_length
			end_x = self.canvas.winfo_width() - arrow_length / 2.0
			end_y = 0
		if (x == 0 and y < 0):
			#setup down arrow
			start_x = self.canvas.winfo_width() - arrow_length / 2.0
			start_y = 0
			end_x = self.canvas.winfo_width() - arrow_length / 2.0
			end_y = arrow_length
		if (x > 0 and y > 0):
			#setup NE arrow
			start_x = self.canvas.winfo_width() - arrow_length
			start_y = arrow_length
			end_x = self.canvas.winfo_width()
			end_y = 0
		if (x > 0 and y < 0):
			#setup SE arrow
			start_x = self.canvas.winfo_width() - arrow_length
			start_y = 0
			end_x = self.canvas.winfo_width()
			end_y = arrow_length
		if (x < 0 and y > 0):
			#setup NW arrow
			start_x = self.canvas.winfo_width()
			start_y = arrow_length
			end_x = self.canvas.winfo_width() - arrow_length
			end_y = 0
		if (x < 0 and y < 0):
			#setup SW arrow
			start_x = self.canvas.winfo_width()
			start_y = 0
			end_x = self.canvas.winfo_width() - arrow_length
			end_y = arrow_length

		#add padding
		start_x -= padding
		end_x -= padding
		start_y += padding
		end_y += padding

		#paint arrow
		arrow = self.canvas.create_line(start_x, start_y, end_x, end_y, arrow = "last", arrowshape = (arrow_head_length, arrow_head_hypotenuse, arrow_head_height), width = line_weight, fill = line_color)

		#keep arrow around for half a second
		time.sleep(0.5)

		#fade object - at the moment, from red to white
		# for i in range(5,255,10):
		# 	rgb = 255, i, i
		# 	self.canvas.itemconfig(arrow, fill=str('#%02x%02x%02x' % rgb))
		# 	time.sleep(0.01)

		#remove from canvas
		self.canvas.delete(arrow)

	def swap(self, a, b):
		#swaps the values of two numbers
		return (b, a)

	# class ActionIconDisplayThread(threading.Thread):
	# 	def __init__(self, x, y, canvas):
	# 		threading.Thread.__init__(self)
	# 		self.x = x
	# 		self.y = y
	# 		self.canvas = canvas
	# 		self.arrow = False
	# 		#padding of icon against side of canvas
	# 		self.padding = 10 
	# 		#arrow icon geometric attributes
	# 		self.arrow_length = 20
	# 		self.arrow_head_height = 10
	# 		self.arrow_head_length = 10
	# 		self.arrow_head_hypotenuse = math.sqrt(self.arrow_head_height**2 + self.arrow_head_length**2) #silly parameter requered by tkinter.create_line for arrow drawing
	# 		self.line_weight = 10
	# 		self.line_color = "red"

	# 	def run(self):
	# 		# try: 
	# 			#function to be used by thread which updates the icon visualizing latest action
	# 			if (self.x > 0 and self.y == 0):
	# 				#setup left arrow
	# 				start_x = self.canvas.winfo_width()
	# 				start_y = self.arrow_length / 2.0
	# 				end_x = self.canvas.winfo_width() - self.arrow_length
	# 				end_y = self.arrow_length / 2.0
	# 			if (self.x < 0 and self.y == 0):
	# 				#setup right arrow
	# 				start_x = self.canvas.winfo_width() - self.arrow_length
	# 				start_y = self.arrow_length / 2.0
	# 				end_x = self.canvas.winfo_width()
	# 				end_y = self.arrow_length / 2.0
	# 			if (self.x == 0 and self.y > 0):
	# 				#setup up arrow
	# 				start_x = self.canvas.winfo_width() - self.arrow_length / 2.0
	# 				start_y = self.arrow_length
	# 				end_x = self.canvas.winfo_width() - self.arrow_length / 2.0
	# 				end_y = 0
	# 			if (self.x == 0 and self.y < 0):
	# 				#setup down arrow
	# 				start_x = self.canvas.winfo_width() - self.arrow_length / 2.0
	# 				start_y = 0
	# 				end_x = self.canvas.winfo_width() - self.arrow_length / 2.0
	# 				end_y = self.arrow_length
	# 			if (self.x > 0 and self.y > 0):
	# 				#setup NE arrow
	# 				start_x = self.canvas.winfo_width() - self.arrow_length
	# 				start_y = self.arrow_length
	# 				end_x = self.canvas.winfo_width()
	# 				end_y = 0
	# 			if (self.x > 0 and self.y < 0):
	# 				#setup SE arrow
	# 				start_x = self.canvas.winfo_width() - self.arrow_length
	# 				start_y = 0
	# 				end_x = self.canvas.winfo_width()
	# 				end_y = self.arrow_length
	# 			if (self.x < 0 and self.y > 0):
	# 				#setup NW arrow
	# 				start_x = self.canvas.winfo_width()
	# 				start_y = self.arrow_length
	# 				end_x = self.canvas.winfo_width() - self.arrow_length
	# 				end_y = 0
	# 			if (self.x < 0 and self.y < 0):
	# 				#setup SW arrow
	# 				start_x = self.canvas.winfo_width()
	# 				start_y = 0
	# 				end_x = self.canvas.winfo_width() - self.arrow_length
	# 				end_y = self.arrow_length

	# 			#add padding
	# 			start_x -= self.padding
	# 			end_x -= self.padding
	# 			start_y += self.padding
	# 			end_y += self.padding

	# 			#paint arrow
	# 			self.arrow = self.canvas.create_line(start_x, start_y, end_x, end_y, arrowshape = (self.arrow_head_length, self.arrow_head_hypotenuse, self.arrow_head_height), width = self.line_weight, fill = line_color)

	# 			#keep arrow around for half a second
	# 			time.sleep(0.5)

	# 			#fade object - at the moment, from red to white
	# 			for i in range(5,255,10):
	# 				rgb = 255, i, i
	# 				self.canvas.itemconfig(self.arrow, fill=str('#%02x%02x%02x' % rgb))
	# 				time.sleep(0.02)

	# 			#remove from canvas
	# 			self.canvas.delete(self.arrow)
	# 			# self.arrow = False

	# 	    # except SystemExit: 
	# 	    # 	pass               //this does not work with python's new threading package. Possible way to make this work by making the thread a process?
	# 	    # finally:
	# 	    # 	if(arrow):
	# 		   #  	self.canvas.delete(arrow)


if __name__ == '__main__':
	m = Maze(200, 400, 30)

	s = input('--> ');

	while(s != "exit"):
		if("r" in s):
			m.process_move(20, 0)
		elif("l" in s):
			m.process_move(-20,0)
		elif("u" in s):
			m.process_move(0,-20)
		elif("d" in s):
			m.process_move(0,20)
		else:
			pass

		s = input('--> ');