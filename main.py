import sys
from hero2 import hero2
from hero1 import hero1
from pawn import pawn
class coordinate(object):
	global x,y
class empty(object):
	"""docstring for empty"""
	name="  -  "

class game(object):
	global x,row,col,a,b
	global player_a,player_b
	global empty
	empty=empty()
	def input(self):
		self.player_a={}
		self.player_b={}
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
				self.player_a[p]=[col-1,i]
			elif(p[0]=="H"):
				char=hero1(col-1,i,"A"," A-"+p,self.row,self.col)
				self.x[col-1][i]=char
				self.player_a[p]=[col-1,i]
			elif(p[0]=="T"):
				char=hero2(col-1,i,"A"," A-"+p,self.row,self.col)
				self.x[col-1][i]=char
				self.player_a[p]=[col-1,i]
		self.display()
		print("Player B Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				self.player_b[p]=[0,i]
			elif(p[0]=="H"):
				char=hero1(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				self.player_b[p]=[0,i]
			elif(p[0]=="T"):
				char=hero2(0,i,"B"," B-"+p,self.row,self.col)
				self.x[0][i]=char
				self.player_b[p]=[0,i]
		self.display()
	def start(self):
		while(self.a>0 or self.b >0):
			print("Enter your move Player A")
			p=input()
			if(p[0]=="P"):
				pos=self.player_a[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"A",self.player_b)
				print(i)
				if(i!=False):
					if(i[2]==1):
						self.x[i[4][0]][i[4][1]]=empty
						del player_b[i[4][0]][i[4][1]]						
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_a[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			elif(p[0]=="H"):
				pos=self.player_a[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"A",self.player_b)
				print(i)
				if(i!=False):
					if(i[2]==1):
						self.x[i[4][0]][i[4][1]]=empty
						del player_b[i[4][0]][i[4][1]]
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_a[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			elif(p[0]=="T"):
				pos=self.player_a[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"A",self.player_b)
				if(i!=False):
					if(i[2]==1):
						self.x[i[4][0]][i[4][1]]=empty
						del player_b[i[4][0]][i[4][1]]
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_a[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			self.display()
			print("Enter your move Player B")
			p=input()
			if(p[0]=="P"):
				pos=self.player_b[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"B",self.player_a)
				if(i!=False):
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_b[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			elif(p[0]=="H"):
				pos=self.player_b[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"B",self.player_a)
				if(i!=False):
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_b[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			elif(p[0]=="T"):
				pos=self.player_b[p[0:2]]
				x=pos[0]
				y=pos[1]
				i=self.x[x][y].move(x,y,p[3],"B",self.player_a)
				if(i!=False):
					self.x[i[0]][i[1]]=self.x[x][y]
					self.x[x][y]=empty
					self.player_b[p[0:2]]=[i[0],i[1]]
				else:
					print("wrong move")
			self.display()

	def display(self):
		for i in range(self.row):
			for t in range(self.col):
				sys.stdout.write(" "+self.x[i][t].name)
			print("\n")