from chessboard import chessboard
from choose import choose
class game(object):
	global row,col,chessboard,choose
	def b(self):
		print("Rows and Columns")
		self.row=input()
		self.col=input()
		self.chessboard=chessboard(self.row,self.col)
	def input(self):
		board=self.chessboard
		row=self.row
		col=self.col
		self.choose=choose()
		print("Player A Input")
		for x in range(col):
			p=input()
			self.choose.input(row-1,x,p,board,"A")
		print("Player B Input")
		for x in range(col):
			p=input()
			self.choose.input(0,x,p,board,"B")
	def start(self):
		while(True):
			print("Player A,Your Move")
			p=input()
			self.choose.move("A",self.chessboard,p)
			print("Player B,Your Move")
			p=input()
			self.choose.move("B",self.chessboard,p)