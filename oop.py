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
	cb=chessboard()
	def move(self,arg,cb):
class hero1(hero):
	steps=2
class hero2(hero):
	steps=2
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
class player(object):
	pass

class game(object):
	global a_pawns,b_pawns
	global lookup
	lookup={}
	def input(self):
		a=player()
		b=player()
		print("No of rows and columns")
		row=int(input())
		col=int(input())
		a_pawns=col+1
		b_pawns=col+1
		pawn_a={}
		pawn_b={}
		x=chessboard(row,col)
		print("Player A Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(4,i,"A",p)
				a_pawns[p]=char
				x.pos(4,i,"A-P"+p[1])
			elif(p[0]=="H"):
				char=hero1(4,i,"A",p)
				a_pawns[p]=char
				x.pos(4,i,"A-P"+p[1])
			elif(p[0]=="T"):
				char=hero2(4,i,"A",p)
				a_pawns[p]
				x.pos(4,i,"A-P"+p[1])
		x.display()
		print("Player B Input")
		for i in range(col):
			p=input()
			if(p[0]=="P"):
				char=pawn(0,i,"B",p)
				b_pawns[p]=char
				x.pos(0,i,"B-P"+p[1])
			elif(p[0]=="H"):
				char=hero1(0,i,"B",p)
				b_pawns[p]=char
				x.pos(0,i,"B-P"+p[1])
			elif(p[0]=="T"):
				char=hero2(0,i,"B",p)
				b_pawns[p]=char
				x.pos(0,i,"B-P"+p[1])
		x.display()
	def start(self):
		while(a_pawns or b_pawns !=0):
			print("A it's your chance")
			p=input()
