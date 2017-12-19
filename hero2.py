from hero import hero
class hero2(hero):
	steps=2
	def move(self,x,y,mov,player,playerb):
		if(player=="A"):
			if(mov=="FR"):
				if(x>0 and x<=4 and y<4 and y>=0):
					c=0
					for u in playerb:
						if(playerb[u][0]==x-1 and playerb[u][1]!=y):
							c=1
							return[x-self.steps,y,1,[x-1,y]]
					if(c==0):
						return[x-self.steps,y,0]						
				else:
					return False
			if(mov=="FL"):
				if(x>0 and x<=4 and y<=4 and y>0):
					c=0
					for u in playerb:
						if(playerb[u][0]==x-1 and playerb[u][1]!=y):
							c=1
							return[x-self.steps,y,1,[x-1,y]]
					if(c==0):
						return[x-self.steps,y,0]						
				else:
					return False
			elif(mov=="BL"):
				if(x>=0 and x<4 and y>0 and y<=4):
					return[x+self.steps,y,0]
				else:
					return False
			elif(mov=="BR"):
				if(x>=0 and x<4 and y>=0 and y<4):
					return[x+self.steps,y,0]
				else:
					return False
		elif(player=="B"):
			if(mov=="BL"):
				if(x>0 and x<=4 and y>=0 and y<4):
					return[x-self.steps,y,0]
				else:
					return False
			if(mov=="BL"):
				if(x>0 and x<=4 and y>=0 and y<4):
					return[x-self.steps,y,0]
				else:
					return False
			elif(mov=="FR"):
				if(x>=0 and x<4 and y>0 and y<=4):
					return[x+self.steps,y,0]
				else:
					return False
			elif(mov=="FL"):
				if(x>=0 and x<4 and y>=0 and y<4):
					return[x+self.steps,y,0]
				else:
					return False