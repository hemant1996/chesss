class pawn(hero):
	steps=1
	def move(self,x,y,mov,player):
		if(player=="A"):
			if(mov=="F"):
				if(x>0 and x<=5):
					return[x-1,y]
				else:
					return False
			elif(mov=="B"):
				if(x<=0 and x>5):
					return[x+1,y]
				else:
					return False				
			elif(mov=="L"):
				if(y>0 and y<=5):
					return[x,y-1]
				else:
					return False			
			elif(mov=="R"):
				if(y>=0 and y<5):
					return[x,y+1]
				else:
					return False