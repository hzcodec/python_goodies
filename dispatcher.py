SELECT1 = 0
SELECT2 = 1
SELECT3 = 2
SELECT4 = 3

class MCP():
	def __init__(self):
		self.dispatcher = {SELECT1: self.selection_1, \
		                   SELECT2: self.selection_2, \
		                   SELECT3: self.selection_2, \
                                   SELECT4: self.selection_4}


	def check(self):
		print(self.dispatcher)
		print('-----------------')
		print(len(self.dispatcher))
		print('-----------------')

	def config(self, reg, pin, mode):
		if reg > (len(self.dispatcher) - 1):
			print('Error: Register [{}] not valid'.format(reg))
		else:
			self.dispatcher[reg](pin, mode)

	def selection_1(self, pin, mode):
		print('Selection 1: pin={}, mode={}'.format(pin, mode))

	def selection_2(self, pin, mode):
		print('Selection 2: pin={}, mode={}'.format(pin, mode))

	def selection_3(self, pin, level):
		print('Selection 3: pin={}, level={}'.format(pin, level))

	def selection_4(self, pin, level):
		print('Selection 4: pin={}, level={}'.format(pin, level))


myDispach = MCP()

myDispach.config(SELECT1, 99, 1)
myDispach.config(SELECT2, 77, 2)
myDispach.config(3, 44, 2)
