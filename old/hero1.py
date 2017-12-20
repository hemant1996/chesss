from hero import hero
class hero1(hero):
	steps=2
	def move(self,x,y,mov,player,playerb):
		if(player=="A"):
			if(mov=="F"):
				if(x>0 and x<=4):
					c=0
					for u in playerb:
						if(playerb[u][0]==x-1 and playerb[u][1]!=y):
							c=1
							return[x-self.steps,y,1,[x-1,y]]
					if(c==0):
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