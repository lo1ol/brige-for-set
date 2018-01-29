class ref():
	"""
	Implementation of references in python
	"""
	def __init__(self, obj):
		"""
		Set object in reference
		:param obj:
		"""
		self.obj = [obj]

	def set_obj(self, obj):
		"""
		change current object in reference
		:param obj: New object
		:return: None
		"""
		self.obj[0] = obj

	def get_obj(self):
		"""
		get current object from reference
		:return: current object
		"""
		return self.obj[0]