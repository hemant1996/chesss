from character import character
class hero1(character):
	"""docstring for pawn"""
	def move(self,chessboard,p):
		self.conseq=[]
		if(self.alive):
			if(p[3]=="FR"):
				new_pos=[self.position[0]-2,self.position[1]+2]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.conseq.append([self.position[0]-1,self.position[1]+1])
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="FL"):
				new_pos=[self.position[0]-2,self.position[1]-2]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.conseq.append([self.position[0]-1,self.position[1]-1])
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="BR"):
				new_pos=[self.position[0]+2,self.position[1]+2]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.conseq.append([self.position[0]-1,self.position[1]+1])
					self.position=new_pos
				else:
					print("invalid position")
			elif(p[3]=="BL"):
				new_pos=[self.position[0]+2,self.position[1]-2]
				if(chessboard.valid(new_pos)):
					self.conseq.append(self.position)
					self.conseq.append([self.position[0]+1,self.position[1]-1])
					self.position=new_pos
				else:
					print("invalid position")
		else:
			print("Dead Player")