from copy import copy
from abc import abstractmethod
from reference import ref


class Set:
	@abstractmethod
	def __init__(self, container=None):
		pass

	@abstractmethod
	def add(self, elem):
		pass

	@abstractmethod
	def pop(self):
		pass

	@abstractmethod
	def clear(self):
		pass

	@abstractmethod
	def remove(self, item):
		pass

	def empty(self):
		if not self:
			return True
		else:
			return False

	def update(self, other):
		for elem in other:
			self.add(elem)

	def union(self, other):
		new_set = copy(self)
		new_set.update(other)
		return new_set

	def discard_update(self, other):
		for elem in other:
			if elem in self:
				self.remove(elem)

	def discard(self, other):
		new_set = copy(self)
		new_set.discard_update(other)
		return new_set

	def intersection(self, other):
		new_set = copy(self)
		new_set.intersection_update(other)
		return new_set

	def intersection_update(self, other):
		cp = copy(self)
		for elem in cp:
			if elem not in other:
				self.remove(elem)

	def difference_update(self, other):
		self.__init__(self.discard(other) | other.discard(self))

	def difference(self, other):
		new_set = copy(self)
		new_set.difference_update(other)
		return new_set

	def __copy__(self):
		return self.__class__(self.container)

	def __contains__(self, item):
		if item in self.container:
			return True
		else:
			return False

	def __len__(self):
		return len(self.container)

	def __and__(self, other):
		return self.intersection(other)

	def __or__(self, other):
		return self.union(other)

	def __iter__(self):
		return self.container.__iter__()

	def __str__(self):
		string = str(self.container)
		return "{" + string[1:-1] + "}"

class SetViaList(Set):
	def __init__(self, container=None):
		Set.__init__(self, container)
		if not container:
			self.container = []
		elif hasattr(container, "container"):
			self.container = list(container.container)
		else:
			self.container = list(container)

	def add(self, elem):
		if elem in self.container:
			pass
		else:
			self.container.append(elem)

	def pop(self):
		return self.container.pop()

	def clear(self):
		self.container = []

	def remove(self, item):
		return self.container.remove(item)


class SetViaSet(Set):
	def __init__(self, container=None):
		Set.__init__(self, container)
		if not container:
			self.container = set()
		elif hasattr(container, "container"):
			self.container = set(container.container)
		else:
			self.container = set(container)

	def add(self, elem):
		if elem in self.container:
			pass

		else:
			self.container.add(elem)

	def pop(self):
		return self.container.pop()

	def clear(self):
		self.container = set()

	def remove(self, item):
		return self.container.remove(item)


class SetViaTuple(Set):
	def __init__(self, container=None):
		Set.__init__(self, container)
		if not container:
			self.container = tuple()
		elif hasattr(container, "container"):
			self.container = tuple(container.container)
		else:
			self.container = tuple(container)

	def _container_get(self):
		return self._container.get_obj()

	def _container_set(self, item):
		if not "_set" in self.__dict__:
			self._container = ref(item)
		else:
			self._container.set_obj(item)

	def _container_del(self):
		if not "_container" in self.__dict__:
			return None
		else:
			self.__dict__.pop("_container")

	container = property(_container_get, _container_set, _container_del)

	def add(self, elem):
		if elem in self.container:
			pass
		else:
			self.container = self.container + (elem,)

	def pop(self):
		elem = self.container[-1]
		self.container = self.container[:-1]
		return elem

	def clear(self):
		self.container = tuple()

	def remove(self, item):
		index = self.container.index(item)
		self.container = self.container[:index]+self.container[index+1:]


if __name__ == "__main__":
	x = SetViaList()
	x.add(12)
	x.add(13)
	y = SetViaSet(x)
	y.add(14)
	print("x :%s, y: %s" % (x, y))
	y = x
	y.add(1)
	print("x :%s, y: %s" % (x, y))
	print(y.pop())
	print(x)
	x = SetViaTuple({1, 2, 3, 4})
	x.add(10)
	print(x)
	x.pop()
	print(x)
	x.clear()
	print(x)
	x.update(SetViaList((1, 3, 10, 30)))
	x.remove(3)
	print(x)
	print(len(x))
