from chessboard import chessboard
from pawn import pawn
from hero2 import hero2
from hero1 import hero1
class choose(object):
	"""docstring for choose"""
	def __init__(self):
		super(choose, self).__init__()
	def input(self,row,col,inp,board,player):
		if(inp[0]=="P"):
			p=pawn(row,col,player+inp,player)
			board.pos(row,col,p,player)
		elif(inp[0]=="H"):
			p=hero2(row,col,player+inp,player)
			board.pos(row,col,p,player)
		elif(inp[0]=="T"):
			p=hero1(row,col,player+inp,player)
			board.pos(row,col,p,player)
		board.display()
	def move(self,player,chessboard,p):
		if(player=="A"):
			char=chessboard.find_char("A"+p[0:2])
			if(char!=False):
				x=char.position[0]
				y=char.position[1]
				char.move(chessboard,p)
				pos=char.position
				chessboard.pos(pos[0],pos[1],char,"A")
				chessboard.emptyy(x,y)
				chessboard.conseq(char.conseq,"A")
			else:
				print("Not valid")
		elif(player=="B"):
			char=chessboard.find_char("B"+p[0:2])
			if(char!=False):
				x=char.position[0]
				y=char.position[1]
				char.move(chessboard,p)
				pos=char.position
				chessboard.pos(pos[0],pos[1],char,"B")
				chessboard.emptyy(x,y)
				chessboard.conseq(char.conseq,"B")
			else:
				print("Not valid")
		chessboard.display()