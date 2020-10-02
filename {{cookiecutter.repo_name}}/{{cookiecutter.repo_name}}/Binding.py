class Button(object):

	def __init__(self):
		self.callback = None

	def bind(self, callback = None):
		self.callback = callback

	def __call__(self, *args, **kwargs):


class App(object):

	def run(self):
		while(True):


