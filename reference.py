class ref():
	def __init__(self, obj):
		self.obj = [obj]

	def set_obj(self, obj):
		self.obj[0] = obj

	def get_obj(self):
		return self.obj[0]