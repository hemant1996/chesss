import abc
class character(object):
	global name,alive,position,conseq,player
	"""docstring for ClassName"""
	def __init__(self, x,y,name,player):
		super(character, self).__init__()
		self.name = name
		self.alive = True
		self.position=[x,y]
		self.player=player
	@abc.abstractmethod
	def move(self,chessboard):
		pass	