import random

#TODO add doors, add sounds

def range_intersect(a1,b1,a2,b2):
	a2_mid=a1<=a2 and a2<=b1
	b2_mid=a1<=b2 and b2<=b1
	return a2_mid or b2_mid

def rect_intersect(x1,y1,w1,h1,x2,y2,w2,h2):
	return range_intersect(x1,x1+w1,x2,x2+w2) and  range_intersect(y1,y1+h1,y2,y2+h2)

def contained_in(list1,list2):
	for el in list1:
		if not (el in list2):
			return False
	return True

def list_difference(list1,list2):
	outlist=[]
	for el in list1:
		if not(el in list2):
			outlist.append(el)
	return outlist

class Graph():
	def __init__(self):
		self.nodes=[]
		self.edges=dict()
	def add_node(self,node):
		self.nodes.append(node)
		self.edges[self.nodes.index(node)]=[]
	def add_edge(self,node1,node2):
		if self.nodes.index(node1) not in self.edges[self.nodes.index(node2)]:
			self.edges[self.nodes.index(node1)].append(self.nodes.index(node2))
			self.edges[self.nodes.index(node2)].append(self.nodes.index(node1))
	def adjacent(self,node1,node2):
		if (not node1 in self.nodes) or (not node2 in self.nodes):
			return False
		if self.nodes.index(node2) in self.edges[self.nodes.index(node1)]:
			return True
		return False
	def get_neighbors(self,node):
		neighbor_numbers=self.edges[self.nodes.index(node)]
		neighbors=[]
		for i in neighbor_numbers:
			neighbors.append(self.nodes[i])
		return neighbors
	def get_degree(self,node):
		return len(self.edges[self.nodes.index(node)])
	def spanning_tree(self):
		spanning_tree=Graph()
		for node in self.nodes:
			spanning_tree.add_node(node)
		start_node=self.nodes[0]
		added_nodes=[start_node]
		while len(added_nodes)<len(self.nodes):
			for node in added_nodes:
				neighbors=self.get_neighbors(node)
				new_neighbors=list_difference(neighbors,added_nodes)
				if len(new_neighbors)!=0:
					chosen_neighbor=random.choice(new_neighbors)
					spanning_tree.add_edge(node,chosen_neighbor)
					added_nodes.append(chosen_neighbor)
					break
		return spanning_tree
	def induced_subgraph(self,node_list):
		subgraph=Graph()
		for node in node_list:
			subgraph.add_node(node)
		for node in node_list:
			neighbors=self.get_neighbors(node)
			for neighbor in neighbors:
				if neighbor in node_list:
					if not(subgraph.adjacent(node,neighbor)):
						subgraph.add_edge(node,neighbor)
		return subgraph
	def shortest_path(self,node1,node2):
		if node1==node2:
			return [node1]
		node1_frontier=[(node1,)]
		node2_frontier=[(node2,)]
		explored_node1=[node1]
		explored_node2=[node2]
		searching=True
		while searching:
			something_new_this_round=False
			new_node1_frontier=[]
			for path in node1_frontier:
				last_node=path[-1]
				neighbors=self.get_neighbors(last_node)
				new_neighbors=list_difference(neighbors,explored_node1)
				for new_neighbor in new_neighbors:
					something_new_this_round=True
					explored_node1.append(new_neighbor)
					new_path=path+tuple([new_neighbor])
					new_node1_frontier.append(new_path)
					for other_path in node2_frontier:
						other_end=other_path[-1]
						if other_end==new_neighbor:
							return path+other_path[::-1]
			node1_frontier=new_node1_frontier
			new_node2_frontier=[]
			for path in node2_frontier:
				last_node=path[-1]
				neighbors=self.get_neighbors(last_node)
				new_neighbors=list_difference(neighbors,explored_node2)
				for new_neighbor in new_neighbors:
					something_new_this_round=True
					explored_node2.append(new_neighbor)
					new_path=path+tuple([new_neighbor])
					new_node2_frontier.append(new_path)
					for other_path in node1_frontier:
						other_end=other_path[-1]
						if other_end==new_neighbor:
							return other_path+path[::-1]
			node_2_frontier=new_node2_frontier
			if something_new_this_round==False:
				return None
					
	def check_nodes_connected(self,node1,node2):
		shortest_path=self.shortest_path(node1,node2)
		if shortest_path is None:
			return False
		return True
	def check_graph_connected(self):
		nodes_found=[]
		nodes_found.append(self.nodes[0])
		searching=True
		while searching:
			one_hop=[]
			for node in nodes_found:
				neighbors=self.get_neighbors(node)
				for neighbor in neighbors:
					if (neighbor not in nodes_found) and (neighbor not in one_hop):
						one_hop.append(neighbor)
			if one_hop==[]:
				if len(nodes_found)==len(self.nodes):
					return True
				else:
					return False
			nodes_found=nodes_found+one_hop
	def get_component_with_forbidden(self,start_node,forbidden_list):
		nodes_found=[]
		nodes_found.append(start_node)
		searching=True
		while searching:
			one_hop=[]
			for node in nodes_found:
				neighbors=self.get_neighbors(node)
				for neighbor in neighbors:
					if (neighbor not in nodes_found) and (neighbor not in one_hop) and (neighbor not in forbidden_list):
						one_hop.append(neighbor)
			if one_hop==[]:
				return nodes_found
			nodes_found=nodes_found+one_hop							 
	def get_distance(self,node1,node2):
		shortest_path=self.shortest_path(node1,node2)
		if shortest_path is None:
			return float('inf')
		return len(shortest_path)-1
	def get_longest_path(self):
		longest_length=float('-inf')
		longest_path=None
		for node1 in self.nodes:
			for node2 in self.nodes:
				shortest_path=self.shortest_path(node1,node2)
				if (shortest_path is not None) and len(shortest_path)-1>longest_length:
					longest_length=len(shortest_path)-1
					longest_path=shortest_path
		#print(longest_path)
		return longest_path
	def __str__(self):
		output=''
		for node in self.nodes:
			output+=str(node)+' : '
			for neighbor in self.get_neighbors(node):
				output+=str(neighbor)+' , '
			output=output[:-3]
			output+='\n'
		return output		


def build_grid_graph(m,n):
	outgraph=Graph()
	for x in range(m):
		for y in range(n):
			outgraph.add_node((x,y))
	for x in range(m):
		for y in range(n):
			if y<n-1:
				outgraph.add_edge((x,y),(x,(y+1)%n))
			if y>0:
				outgraph.add_edge((x,y),(x,(y-1)%n))
			if x>0:
				outgraph.add_edge((x,y),((x-1)%m,y))
			if x<m-1:
				outgraph.add_edge((x,y),((x+1)%m,y))
	return outgraph  		

class Maze():
	def __init__(self,screen,grid_x=3,grid_y=3,locked=2):
		grid_graph=build_grid_graph(grid_x,grid_y)
		valid_generation=False
		while not valid_generation:
			self.spanning_tree=grid_graph.spanning_tree()
			self.longest_path=self.spanning_tree.get_longest_path()
			try:
				self.locked_rooms=random.sample(self.longest_path[1:-1],locked)
				valid_generation=True
			except:
				pass
		self.start=self.longest_path[0]
		self.end=self.longest_path[-1]		
		#generate key rooms
		self.key_rooms=[]
		locked_room_indices=list(map(lambda x:self.longest_path.index(x),self.locked_rooms))
		locked_room_indices.sort()
		for locked_room in locked_room_indices:
			allowed_rooms=self.spanning_tree.get_component_with_forbidden(self.start,[self.longest_path[locked_room]])
			self.key_rooms.append(random.choice(allowed_rooms))
		self.locked_rooms=list(map(lambda x:self.longest_path[x],locked_room_indices))
		#build room objects
		self.room_dict=dict()
		for node in self.spanning_tree.nodes:
			if node==self.start:
				self.room_dict[node]=Room('start')
			elif node==self.end:
				self.room_dict[node]=Room('end')
			else:
				self.room_dict[node]=Room()
		for node in self.spanning_tree.nodes:
			for node in self.locked_rooms:
				self.room_dict[node].lock_room()
			for i,node in enumerate(self.key_rooms):
				key_opens=self.locked_rooms[i]
				self.room_dict[node].add_key(key_opens)
		#create main character
		self.screen=screen
		self.char=MainChar()
		self.current_room=self.start
	def move_char(self,x,y):
		char_rect=self.char.surface.get_rect()
		char_width=char_rect.width
		char_height=char_rect.height
		if x>0:
			if self.char.xpos<WIDTH-char_width-x:
				self.char.xpos+=x
			else:
				potential_next_node=(self.current_room[0]+1,self.current_room[1])
				if self.spanning_tree.adjacent(self.current_room,potential_next_node) and not self.room_dict[potential_next_node].locked:
					self.current_room=potential_next_node
					self.char.xpos=0
					self.char.ypos=HEIGHT//2
					 
		if x<0:
			if self.char.xpos>-x:
				self.char.xpos+=x
			else:
				potential_next_node=(self.current_room[0]-1,self.current_room[1])
				if self.spanning_tree.adjacent(self.current_room,potential_next_node) and not self.room_dict[potential_next_node].locked:
                                        self.current_room=potential_next_node
                                        self.char.xpos=WIDTH-char_width
                                        self.char.ypos=HEIGHT//2 
		if y>0:
			if self.char.ypos<HEIGHT-char_height-y:
				self.char.ypos+=y
			else:
				potential_next_node=(self.current_room[0],self.current_room[1]-1)
				if self.spanning_tree.adjacent(self.current_room,potential_next_node) and not self.room_dict[potential_next_node].locked:
                                        self.current_room=potential_next_node
                                        self.char.xpos=WIDTH//2
                                        self.char.ypos=0 
		if y<0:
			if self.char.ypos>-y:
				self.char.ypos+=y
			else:
				potential_next_node=(self.current_room[0],self.current_room[1]+1)
				if self.spanning_tree.adjacent(self.current_room,potential_next_node) and not self.room_dict[potential_next_node].locked:
                                        self.current_room=potential_next_node
                                        self.char.xpos=WIDTH//2
                                        self.char.ypos=HEIGHT-char_height 
		self.key_procedure()
	def render(self):
		self.room_dict[self.current_room].render(self.screen)
		self.char.render(self.screen)
	def key_procedure(self):
		room=self.room_dict[self.current_room]
		if room.key is not None:
			char_rec=self.char.surface.get_rect()
			key_rec=room.key.surface.get_rect()
			touching=rect_intersect(self.char.xpos,self.char.ypos,char_rec.width,char_rec.height,room.key.x,room.key.y,key_rec.width,key_rec.height)
			if touching:
				key_opens=room.key_room
				room.key=None
				self.room_dict[key_opens].unlock_room()
class Room():
	def __init__(self,theme='random'):
		if theme=='random':
			self.image=random.choice(['wood.jpg','stone.jpg','checkered.jpg'])
		elif theme=='start':
			self.image='start.jpg'
		else:
			self.image='end.jpg'
		self.image='backgrounds/'+self.image
		self.locked=False
		self.key=None
		self.surface=pygame.image.load(self.image)
		self.surface=pygame.transform.scale(self.surface,(WIDTH,HEIGHT))

	def lock_room(self):
		self.locked=True
	def unlock_room(self):
		self.locked=False
	def add_key(self,room_key_opens):
		self.key_room=room_key_opens
		self.key=Key(WIDTH//2,HEIGHT//2)
	def render(self,screen):
		screen.blit(self.surface,(0,0))	
		if self.key:
			self.key.render(screen)
class Key():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.image='key.png'
		self.surface=pygame.image.load(self.image)
		self.surface=pygame.transform.scale(self.surface,(WIDTH//7,HEIGHT//7))
	def render(self,screen):
		screen.blit(self.surface,(self.x,self.y))

class MainChar():
	def __init__(self):
		self.image='char.jpeg'
		self.xpos=WIDTH/2
		self.ypos=HEIGHT/2
		self.keys=[]
		self.surface=pygame.image.load(self.image)
		self.surface=pygame.transform.scale(self.surface,(WIDTH//7,HEIGHT//7))
	def render(self,screen):
		screen.blit(self.surface,(self.xpos,self.ypos))
		
if __name__=='__main__':
	WIDTH=600
	HEIGHT=600
	maze_width=3
	maze_height=3
	locks=2
	player_speed=50
	#setup pygame
	import pygame,sys
	from pygame.locals import *
	pygame.init()
	FPS=30
	fpsClock=pygame.time.Clock()
	DISPLAYSURF=pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('Do you know da wae?')
	#setup maze
	maze=Maze(DISPLAYSURF,maze_width,maze_height,locks)
	print(maze.spanning_tree)
	print(maze.start)
	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					maze.move_char(-player_speed,0)
				if event.key == pygame.K_RIGHT:
					maze.move_char(player_speed,0)
				if event.key==pygame.K_UP:
					maze.move_char(0,-player_speed)
				if event.key==pygame.K_DOWN:
					maze.move_char(0,player_speed)

		DISPLAYSURF.fill((0,0,0))
		maze.render()		

		pygame.display.update() 
		fpsClock.tick(FPS)
