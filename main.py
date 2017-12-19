class hero(object):
	"""docstring for hero"""
	position=[]
	def __init__(self, arg1,arg2):
		super(hero, self).__init__()
		position= arg
		self.arg2=
		
class game(object):
	"""docstring for game"""
	global a_pawns,b_pawns
	a_pawns=5
	b_pawns=5
	global lookup
	lookup={}
	def input(self):
		global x
		x = [["-" for i in range(5)] for j in range(5)]
		print("Player A Input")
		for i in range(5):
			p=input()
			lookup["A-"+p]=[4,i]
			x[4][i]="A-"+p
		print("Player B Input")
		for i in range(4,-1,-1):
			p=input()
			lookup["B-"+p]=[0,i]
			x[0][i]="B-"+p
		print(x)
	def start(self):
		while(a_pawns or b_pawns !=0):
			print("A it's your chance")
			move=input()
			values=lookup["A-"+move[0:2]]
			if(move[3]=="F" and values[0]-1>=0):
				x[values[0]-1][values[1]]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="B" and values[0]+1<=5):
				x[values[0]+1][values[1]]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="L" and values[1]-1>=0):
				x[values[0]][values[1]-1]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="R" and values[1]+1<=5):
				x[values[0]][values[1]+1]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			print(x)
			print("B it's your chance")
			move=input()
			values=lookup["A-"+move[0:2]]
			if(move[3]=="F" and values[0]-1>=0):
				x[values[0]-1][values[1]]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="B" and values[0]+1<=5):
				x[values[0]+1][values[1]]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="L" and values[1]-1>=0):
				x[values[0]][values[1]-1]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			if(move[3]=="R" and values[1]+1<=5):
				x[values[0]][values[1]+1]="A-"+move[0:2]
				x[values[0]][values[1]]="-"
			else:
				print("Invalid move")
			move=input()
			values=lookup["B-"+move[0:2]]
			print(values)