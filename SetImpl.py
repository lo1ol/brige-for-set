from copy import copy
from abc import abstractmethod
from reference import ref


class Set:
	"""
	Abstract method Set which contain some virtual methods for other other implementation of set
	and main methods, which uses overriding virtual methods
	"""
	@abstractmethod
	def __init__(self, container=None):
		"""
		virtual constructor
		:param container: optional parameter for initial container
		"""
		pass

	@abstractmethod
	def add(self, elem):
		"""
		virtual method implements operation add to set
		:return: None
		"""
		pass

	@abstractmethod
	def pop(self):
		"""
		virtual method implements pop random element from set
		:return: popped element
		"""
		pass

	@abstractmethod
	def clear(self):
		"""
		virtual method implements clearing set
		:return: None
		"""
		pass

	@abstractmethod
	def remove(self, item):
		"""
		virtual method for removing item from set, if no item -- exception
		:param item: item for removing
		:return: None
		"""
		pass

	def empty(self):
		"""
		check emptiness of set
		:return: True if set is empty, otherwise -- False
		"""
		if not self:
			return True
		else:
			return False

	def update(self, other):
		"""
		Add other set to set
		:param other: other set
		:return: None
		"""
		for elem in other:
			self.add(elem)

	def union(self, other):
		"""
		Copy current set and return new set updated with other
		:param other: other set
		:return: New updated set
		"""
		new_set = copy(self)
		new_set.update(other)
		return new_set

	def discard_update(self, other):
		"""
		Remove elements, which contains other set in current set
		:param other: other set
		:return:
		"""
		for elem in other:
			if elem in self:
				self.remove(elem)

	def discard(self, other):
		"""
		Copy current set and return new set discarded with other
		:param other: other set
		:return: New discarded set
		"""
		new_set = copy(self)
		new_set.discard_update(other)
		return new_set

	def intersection(self, other):
		"""
		Make intersection with other set in current set
		:param other: other set
		:return: None
		"""
		new_set = copy(self)
		new_set.intersection_update(other)
		return new_set

	def intersection_update(self, other):
		"""
		Copy current set and return new set intersected with other
		:param other: other set
		:return: New Intersected set
		"""
		cp = copy(self)
		for elem in cp:
			if elem not in other:
				self.remove(elem)

	def difference_update(self, other):
		"""
		Remove elements, which not contain other set from current set
		:param other: other set
		:return:None
		"""
		self.__init__(self.discard(other) | other.discard(self))

	def difference(self, other):
		"""
		Copy current set and return new set differenced with other
		:param other: other set
		:return: New Intersected set
		"""
		new_set = copy(self)
		new_set.difference_update(other)
		return new_set

	def __copy__(self):
		"""
		Make a copy of current set
		:return: copy of current set
		"""
		return self.__class__(self.container)

	def __contains__(self, item):
		"""
		Overriding operation in
		:param item: item for checking on containing
		:return: True if item in set, otherwise -- False
		"""
		if item in self.container:
			return True
		else:
			return False

	def __len__(self):
		"""
		Method for getting len of set
		:return: len of set
		"""
		return len(self.container)

	def __and__(self, other):
		"""
		Overriding of operation & (intersection)
		:param other: other set
		:return: new set
		"""
		return self.intersection(other)

	def __or__(self, other):
		"""
		Overriding of operation | (union)
		:param other: other set
		:return: new set
		"""
		return self.union(other)

	def __iter__(self):
		"""
		Get iterator for set
		:return: iterator for set
		"""
		return self.container.__iter__()

	def __str__(self):
		"""
		convert set to string
		:return: str
		"""
		string = str(self.container)
		return "{" + string[1:-1] + "}"


class SetViaList(Set):
	"""
	Implementation of set via list
	"""
	def __init__(self, container=None):
		"""
		virtual constructor
		:param container: optional parameter for initial container
		"""
		Set.__init__(self, container)
		if not container:
			self.container = []
		elif hasattr(container, "container"):
			self.container = list(container.container)
		else:
			self.container = list(set(container))

	def add(self, elem):
		"""
		virtual method implements operation add to set
		:return: None
		"""
		if elem in self.container:
			pass
		else:
			self.container.append(elem)

	def pop(self):
		"""
		virtual method implements pop random element from set
		:return: popped element
		"""
		return self.container.pop()

	def clear(self):
		"""
		virtual method implements clearing set
		:return: None
		"""
		self.container = []

	def remove(self, item):
		"""
		virtual method for removing item from set, if no item -- exception
		:param item: item for removing
		:return: None
		"""
		return self.container.remove(item)


class SetViaSet(Set):
	"""
	Implementation of set via list
	"""
	def __init__(self, container=None):
		"""
		virtual constructor
		:param container: optional parameter for initial container
		"""
		Set.__init__(self, container)
		if not container:
			self.container = set()
		elif hasattr(container, "container"):
			self.container = set(container.container)
		else:
			self.container = set(container)

	def add(self, elem):
		"""
		virtual method implements operation add to set
		:return: None
		"""
		if elem in self.container:
			pass

		else:
			self.container.add(elem)

	def pop(self):
		"""
		virtual method implements pop random element from set
		:return: popped element
		"""
		return self.container.pop()

	def clear(self):
		"""
		virtual method implements clearing set
		:return: None
		"""
		self.container = set()

	def remove(self, item):
		"""
		virtual method for removing item from set, if no item -- exception
		:param item: item for removing
		:return: None
		"""
		return self.container.remove(item)


class SetViaTuple(Set):
	"""
	Implementation of set via list
	"""
	def __init__(self, container=None):
		"""
		virtual constructor
		:param container: optional parameter for initial container
		"""
		Set.__init__(self, container)
		if not container:
			self.container = tuple()
		elif hasattr(container, "container"):
			self.container = tuple(container.container)
		else:
			self.container = tuple(set(container))

	def _container_get(self):
		"""
		Getter for container attribute
		:return:
		"""
		return self._container.get_obj()

	def _container_set(self, item):
		"""
		setter for container attribute
		:param item:
		:return:
		"""
		if not "_set" in self.__dict__:
			self._container = ref(item)
		else:
			self._container.set_obj(item)

	def _container_del(self):
		"""
		deleter for container attribute
		:return:
		"""
		if not "_container" in self.__dict__:
			return
		else:
			self.__dict__.pop("_container")

	container = property(_container_get, _container_set, _container_del)  # Property for make tuple changable object in python

	def add(self, elem):
		"""
		virtual method implements operation add to set
		:return: None
		"""
		if elem in self.container:
			pass
		else:
			self.container = self.container + (elem,)

	def pop(self):
		"""
		virtual method implements pop random element from set
		:return: popped element
		"""
		elem = self.container[-1]
		self.container = self.container[:-1]
		return elem

	def clear(self):
		"""
		virtual method implements clearing set
		:return: None
		"""
		self.container = tuple()

	def remove(self, item):
		"""
		virtual method for removing item from set, if no item -- exception
		:param item: item for removing
		:return: None
		"""
		index = self.container.index(item)
		self.container = self.container[:index]+self.container[index+1:]


if __name__ == "__main__":
	x = SetViaList()
	x.add(12)
	x.add(13)
	y = SetViaSet(x)
	y.add(14)
	print("x :%s, y: %s" % (x, y))
	y.add(12)
	y = x
	y.add(1)
	print("x :%s, y: %s" % (x, y))
	print(y.pop())
	print(x)
	x = SetViaTuple({1, 2, 3, 4, 4})
	x.add(10)
	print(x)
	x.pop()
	print(x)
	x.clear()
	print(x)
	x.update(SetViaSet((1, 3, 10, 30)))
	x.remove(3)
	print(x)
	print(len(x))
