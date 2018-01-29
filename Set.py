import SetImpl
from reference import ref
from copy import copy


class Set:
	"""
	Implementation of bridge between SetViaTuple, ListViaList, SetViaSet
	if number of elements 0<=n<=10, current container has type SetViaTuple
	if number of elements 10<n<=100, current container has type SetViaList
	if number of elements 100<n, current container has type SetViaSt
	"""
	_max_for_tuple = 10
	_max_for_list = 100

	def __init__(self, container=()):
		"""
		Constructor of Set bridge
		:param container: initialize set
		"""
		if len(container) > self._max_for_list:
			self.set = SetImpl.SetViaSet(container)
			self._current = "set"
		elif len(container) > self._max_for_tuple:
			self.set = SetImpl.SetViaList(container)
			self._current = "list"
		else:
			self.set = SetImpl.SetViaTuple(container)
			self._current = "tuple"

	def _set_get(self):
		"""
		getter for attribute set
		:return:
		"""
		return self._set.get_obj()

	def _set_set(self, item):
		"""
		setter for attribute set
		:return:
		"""
		if not "_set" in self.__dict__:
			self._set = ref(item)
		else:
			self._set.set_obj(item)

	def _set_del(self):
		"""
		deleter for attribute set
		:return:
		"""
		if "_set" in self.__dict__:
			self.__dict__.pop("_set")

	set = property(_set_get, _set_set, _set_del)  # Property set uses for make unchangeable items in python changeable.
	# Furthermore it makes changes visible after transform in other set (which has same reference on object)

	def _transform(self):
		"""
		This method called after each changes of size in set,
		If changes of type are necessary, they are made
		:return:
		"""
		if self._current != "set" and len(self.set) > self._max_for_list:
			self.set = SetImpl.SetViaSet(self.set)
			self._current = "set"
			print("set")
		elif self._current != "list" and self._max_for_tuple < len(self.set) <= self._max_for_list:
			self.set = SetImpl.SetViaList(self.set)
			self._current = "list"
			print("list")
		elif self._current != "tuple" and len(self.set) <= self._max_for_tuple:
			self.set = SetImpl.SetViaTuple(self.set)
			self._current = "tuple"
			print("tuple")

	def add(self, elem):
		"""
		make add to set, after that make transform
		:param elem: new elem
		:return: None
		"""
		self.set.add(elem)
		self._transform()

	def pop(self):
		"""
		Make pop to set, after that make transform
		:return: random element from set
		"""
		res = self.set.pop()
		self._transform()
		return res

	def clear(self):
		"""
		Erase set
		:return: None
		"""
		self.set.clear()
		self._transform()

	def remove(self, item):
		"""
		Remove item from set, if no item -- exception
		After removing make transform
		:param item: item for removing
		:return: None
		"""
		self.set.remove(item)
		self._transform()

	def empty(self):
		"""
		check emptiness of set
		:return: True if set is empty, otherwise -- False
		"""
		return self.set.empty()

	def update(self, other):
		"""
		Add other set to set
		After that make transform
		:param other: other set
		:return: None
		"""
		self.set.update(other.set)
		self._transform()

	def union(self, other):
		"""
		Copy current set and return new set updated with other
		:param other: other set
		:return: New updated set
		"""
		return Set(self.set.union(other.set))

	def discard_update(self, other):
		"""
		Remove elements, which contains other set in current set
		After that make transform
		:param other: other set
		:return:
		"""
		self.set.discard_update(other.set)
		self._transform()

	def discard(self, other):
		"""
		Copy current set and return new set discarded with other
		:param other: other set
		:return: New discarded set
		"""
		return Set(self.set.discard(other.set))

	def intersection(self, other):
		"""
		Make intersection with other set in current set
		:param other: other set
		:return: None
		"""
		return Set(self.set.intersection(other.set))

	def intersection_update(self, other):
		"""
		Copy current set and return new set intersected with other
		After that make transform
		:param other: other set
		:return: New Intersected set
		"""
		self.set.intersection_update(other.set)
		self._transform()

	def difference_update(self, other):
		"""
		Remove elements, which not contain other set from current set
		After that make transform
		:param other: other set
		:return:None
		"""
		self.set.difference_update(other.set)
		self._transform()

	def difference(self, other):
		"""
		Copy current set and return new set differenced with other
		:param other: other set
		:return: New Intersected set
		"""
		return Set(self.set.difference(other.set))

	def __copy__(self):
		"""
		Make a copy of current set
		:return: copy of current set
		"""
		return Set(self.set.__copy__())

	def __contains__(self, item):
		"""
		Overriding operation in
		:param item: item for checking on containing
		:return: True if item in set, otherwise -- False
		"""
		return self.set.__contains__(item)

	def __len__(self):
		"""
		Method for getting len of set
		:return: len of set
		"""
		return self.set.__len__()

	def __and__(self, other):
		"""
		Overriding of operation & (intersection)
		:param other: other set
		:return: new set
		"""
		return Set(self.set.__and__(other.set))

	def __or__(self, other):
		"""
		Overriding of operation | (union)
		:param other: other set
		:return: new set
		"""
		return Set(self.set.__or__(other.set))

	def __iter__(self):
		"""
		Get iterator for set
		:return: iterator for set
		"""
		return self.set.__iter__()

	def __str__(self):
		"""
		convert set to string
		:return: str
		"""
		return self.set.__str__()


if __name__ == "__main__":
	inst = Set()
	for i in range(101):
		inst.add(i)
	print(inst)
	print('---')
	inst.pop()
	print("---")
	inst.add(1)
	print("---")
	inst.add("101")
	print("---")
	inst.clear()


	for i in range(101):
		inst.add(i)
	print("Reference test")
	inst2 = inst
	inst2.pop()
	inst2.add(110)
	print(inst2)
	print(inst)


	print("Copy test")
	inst2 = copy(inst)
	inst2.add(101)
	print(inst2)
	print(inst)
	inst2.clear()
	for i in range(50, 150):
		inst2.add(i)
	print("---")
	print(inst2)
	print(inst)


	print("Or test")
	print(inst|inst2)
	print("---")


	print("And test")
	print(inst & inst2)
	print("---")


	print("Discard test")
	print(inst.discard(inst2))
	print("---")


	print("Difference test")
	print((inst.difference(inst2)))
	print("---")


	print("Empty test")
	print(inst.empty())