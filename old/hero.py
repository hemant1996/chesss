class hero(object):
	global x,y
	global row,col
	alive= None
	owner= None
	name=None
	def __init__(self, x,y,owner,name,row,col):
		super(hero, self).__init__()
		self.x=x
		self.y=y
		self.alive= True
		self.owner=owner
		self.name=name