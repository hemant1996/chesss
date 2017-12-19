import sys
class coordinate(object):
	global x,y
class empty(object):
	"""docstring for empty"""
	name="  -  "
		
		
class hero(object):
	global x,y
	global row,col
	alive= None
	owner= None
	name=None
	def __init__(self, x,y,owner,name,row,col):
		super(hero, self).__init__()
		self.x=x
		self.y=y
		self.alive= True
		self.owner=owner
		self.name=name
class pawn(hero):
	steps=1
	def move(self,x,y,mov,player):
		if(player=="A"):
			if(mov=="F"):
				if(x>0 and x<=5):
					return[x-1,y]
				else:
					return False
			elif(mov=="B"):
				if(x<=0 and x>5):
					return[x+1,y]
				else:
					return False				
			elif(mov=="L"):
				if(y>0 and y<=5):
					return[x,y-1]
				else:
					return False			
			elif(mov=="R"):
				if(y>=0 and y<5):
					return[x,y+1]
				else:
					return False
class hero1(hero):
	steps=2
class hero3(hero):
	steps=2
class game(object):
	global x,row,col,a,b
	global player_a,player_b
	player_a={}
	player_b={}
	global empty
	empty=empty()
	def input(self):
		print("No of rows and columns")
		self.row=int(input())
		self.col=int(input())
		self.a=self.col
		self.b=self.col
		self.x = [[empty for i in range(self.row)] for j in range(self.col)]
		self.display()
		print("Player A Input")
		col=self.col
		for i in range(self.col):
			p=input()
			if(p[0]=="P"):
				char=pawn(col-1,i,"A"," A-"+p,self.row,self.col)
				self.x[col-1][i]=char
				player_a[p]=[col-1,i]
			elif(p[0]=="H"):
				char=hero1(col-1,i,"A"," A-"+p,self.row,self.col)
				self.x[col-1][i]=char
				player_a[p]=[col-1,i]
			elif(p[0]=="T"):
				char=hero2(col-1,i,"A"," A-"+p,self.row,self.col)
				self.x[col-1][i]=char
				player_a[p]=[col-1,i]
		self.display()
		print("Player B Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				player_b[p]=[0,i]
			elif(p[0]=="H"):
				char=hero1(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				player_b[p]=[0,i]
			elif(p[0]=="T"):
				char=hero2(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				player_b[p]=[0,i]
		self.display()
	def start(self):
		while(self.a>0 or self.b >0):
			print("Enter your move Player A")
			p=input()
			if(p[0]=="P"):
				pos=player_a[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"A")
				if(i!=False):
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
				else:
					print("wrong move")
			self.display()

	def display(self):
		for i in range(self.row):
			for t in range(self.col):
				sys.stdout.write(" "+self.x[i][t].name)
			print("\n")