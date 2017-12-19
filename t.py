class my(object):
	x=1
	def __init__(self, arg):
		super(my, self).__init__()
		self.x = arg
class main(object):
	x=[]
	
	def do(self):
		for i in range(5):
			self.x.append(my(i))