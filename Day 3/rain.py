from tkinter import *
import time

WINDOW_WIDTH=1000 #pixels
WINDOW_HEIGHT=300
RAINDROP_WIDTH=10

class Sky():
	def __init__(self):
		#gui window setup
		self.root=Tk()
		self.canvas=Canvas(self.root,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
		self.canvas.pack()
		#lists to store raindrop information
		self.raindrops=[]
		self.raindrop_heights=[]
		#initialize scheduled rainfall
		self.time=0
		self.schedule=[]
	def add_raindrops_to_top(self,position_list): #positions between 0 and WINDOW_WIDTH
		for position in position_list:
			self.raindrops.append(self.canvas.create_rectangle(position,0,position+RAINDROP_WIDTH,RAINDROP_WIDTH,fill='blue'))
			self.raindrop_heights.append(0)
	def fall(self,distance=7):
		remaining_raindrops=[]
		remaining_raindrop_heights=[]
		for i,raindrop in enumerate(self.raindrops):
			self.canvas.move(raindrop,0,distance)
			self.raindrop_heights[i]+=distance
			if self.raindrop_heights[i]<WINDOW_HEIGHT: #raindrop i still on screen
				remaining_raindrops.append(raindrop)
				remaining_raindrop_heights.append(self.raindrop_heights[i])
			else:
				self.canvas.delete(raindrop)
		self.canvas.update()
		self.raindrops=remaining_raindrops
		self.raindrop_heights=remaining_raindrop_heights
		self.time+=1
	def set_raindrop_schedule(self,schedule): #raindrop schedule should be a list of lists, of raindrop positions to add at time 0,1,2...
		self.schedule=schedule
	def start_rain(self):
		while True:
			if self.time<len(self.schedule):
				self.add_raindrops_to_top(self.schedule[self.time])
			time.sleep(.1)
			self.fall()
			
if __name__=='__main__':
	sky=Sky()
	sky.set_raindrop_schedule([[0,7,100,140,150]])
	sky.start_rain()

	mainloop() #required to get the tkinter gui going
