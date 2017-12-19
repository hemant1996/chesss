from hero import hero
class pawn(hero):
	steps=1
	def move(self,x,y,mov,player,playerb):
		if(player=="A"):
			if(mov=="F"):
				if(x>0 and x<=4):
					return[x-self.steps,y,0]
				else:
					return False
			elif(mov=="B"):
				if(x>=0 and x<4):
					return[x+self.steps,y,0]
				else:
					return False				
			elif(mov=="L"):
				if(y>0 and y<=4):
					return[x,y-self.steps,0]
				else:
					return False			
			elif(mov=="R"):
				if(y>=0 and y<4):
					return[x,y+self.steps,0]
				else:
					return False
		elif(player=="B"):
			if(mov=="B"):
				if(x>0 and x<=4):
					return[x-self.steps,y,0]
				else:
					return False
			elif(mov=="F"):
				if(x>=0 and x<4):
					return[x+self.steps,y,0]
				else:
					return False				
			elif(mov=="R"):
				if(y>0 and y<=4):
					return[x,y-self.steps,0]
				else:
					return False			
			elif(mov=="L"):
				if(y>=0 and y<4):
					return[x,y+self.steps,0]
				else:
					return False