from empty import empty
import sys
class chessboard(object):
	global row,column,pos_hash,empty
	pos_hash={}
	empty=empty()	
	def __init__(self, arg,arg1):
		super(chessboard, self).__init__()
		self.row = arg
		self.column= arg1
		self.x = [[empty for i in range(self.row)] for j in range(self.column)]
		self.display()
	def pos(self,row,col,char,player):
		self.x[row][col]=char
		print(self.x[row][col].position,char.name)
		pos_hash[char.name]=[row,col]
	def display(self):
		for i in range(self.row):
			for t in range(self.column):
				sys.stdout.write(" "+self.x[i][t].name)
			print("\n")
	def valid(self,pos):
		if(pos[0]<=self.row-1 and pos[0]>=0 and pos[1]<=self.column-1 and pos[1]>=0):
			return True
		else:
			return False
	def find_char(self,char):
		if char in pos_hash:
			pos=pos_hash[char]
			if(self.x[pos[0]][pos[1]].name==" - "):
				del pos_hash[char]
				return False
			else:
				return self.x[pos[0]][pos[1]]
		else:
			print("It is dead ! Get over it")
			return False
	def conseq(self,conseq,player):
		for i in conseq:
			x=self.x
			print("value of iter",x)
			if(x[i[0]][i[1]].player!=player and x[i[0]][i[1]].player!=None):
				x[i[0]][i[1]].alive=False
				x[i[0]][i[1]]=empty
	def emptyy(self,row,col):
		self.x[row][col]=empty
