from character import character
class pawn(character):
	"""docstring for pawn"""
	def move(self,chessboard,p):
		self.conseq=[]
		if(self.alive):
			if(p[3]=="F"):
				new_pos=[self.position[0]-1,self.position[1]]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="B"):
				new_pos=[self.position[0]+1,self.position[1]]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="L"):
				new_pos=[self.position[0],self.position[1]-1]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="R"):
				new_pos=[self.position[0],self.position[1]+1]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.position=new_pos
				else:
					print("invalid position")
		else:
			print("Dead Player")