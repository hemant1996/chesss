class chessboard(object):
	def __init__(self, arg,arg1):
		super(chessboard, self).__init__()
		self.row = arg
		self.column= arg1
		self.x = [["-" for i in range(self.row)] for j in range(self.column)]
		print self.x
	def pos(self, row,col,char):
		self.x[row][col]=char
	def display(self):
		print(self.x)
class hero(object):
	position=[0,0]
	alive= None
	owner= None
	name=None
	def __init__(self, arg,arg1,own,name):
		super(hero, self).__init__()
		self.position[0] = arg
		self.position[1] = arg1
		self.alive= True
		self.owner=own
		self.name=name
class pawn(hero):
	steps=1
	def move(self,arg,cb):
		if(self.arg=="F" and self.position[0]+steps>=0):
			self.cb.pos(position[0]+steps,position[1],self.name)
			self.cb.pos(position[0],position[1],"-")
			self.position[0]=self.position[0]+1
			self.position[1]=self.position[1]
		if(self.arg=="B" and self.position[0]-steps<=5):
			self.cb.pos(position[0]-steps,position[1],self.name)
			self.cb.pos(position[0],position[1],"-")
			self.position[0]=self.position[0]-steps
			self.position[1]=self.position[1]

class hero1(hero):
	steps=2
	def move(self,arg,cb):
		if(self.arg=="F" and self.position[0]+steps>=0):
			self.cb.pos(position[0]+steps,position[1],self.name)
			self.cb.pos(position[0],position[1],"-")
			self.position[0]=self.position[0]+steps
			self.position[1]=self.position[1]
		if(self.arg=="B" and self.position[0]-steps<=5):
			self.cb.pos(position[0]-steps,position[1],self.name)
			self.cb.pos(position[0],position[1],"-")
			self.position[0]=self.position[0]-steps
			self.position[1]=self.position[1]
class hero2(hero):
	steps=2
class game(object):
	global a_pawns,b_pawns
	global pawn_a
	global pawn_b

	def input(self):
		print("No of rows and columns")
		self.pawn_a={}
		self.pawn_b={}
		row=int(input())
		col=int(input())
		self.a_pawns=col+1
		self.b_pawns=col+1
		x=chessboard(row,col)
		print("Player A Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(col-1,i,"A",p)
				self.pawn_a[p]=char
				x.pos(col-1,i,"A-P"+p[1])
			elif(p[0]=="H"):
				char=hero1(col-1,i,"A",p)
				self.pawn_a[p]=char
				x.pos(col-1,i,"A-P"+p[1])
			elif(p[0]=="T"):
				char=hero2(col-1,i,"A",p)
				self.pawn_a[p]=char
				x.pos(col-1,i,"A-P"+p[1])
		x.display()
		print("Player B Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(0,i,"B",p)
				self.pawn_b[p]=char
				x.pos(0,i,"B-P"+p[1])
			elif(p[0]=="H"):
				char=hero1(0,i,"B",p)
				self.pawn_b[p]=char
				x.pos(0,i,"B-P"+p[1])
			elif(p[0]=="T"):
				char=hero2(0,i,"B",p)
				self.pawn_b[p]=char
				x.pos(0,i,"B-P"+p[1])
		x.display()
	def start(self):
		while(self.a_pawns!=0 or self.b_pawns !=0):
			print("A it's your chance")
			p=input()
			pawn[p[0:2]].move(p[3:5],x,"A-"+p[0:2])