import SetImpl
from reference import ref
from copy import copy


class Set:
	_max_for_tuple = 10
	_max_for_list = 100

	def __init__(self, container=()):
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
		return self._set.get_obj()

	def _set_set(self, item):
		if not "_set" in self.__dict__:
			self._set = ref(item)
		else:
			self._set.set_obj(item)

	def _set_del(self):
		if "_set" in self.__dict__:
			self.__dict__.pop("_set")

	set = property(_set_get, _set_set, _set_del)

	def _transform(self):
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
		self.set.add(elem)
		self._transform()

	def pop(self):
		res = self.set.pop()
		self._transform()
		return res

	def clear(self):
		self.set.clear()
		self._transform()

	def remove(self, item):
		self.set.remove(item)
		self._transform()

	def empty(self):
		return self.set.empty()

	def update(self, other):
		self.set.update(other.set)
		self._transform()

	def union(self, other):
		return Set(self.set.union(other.set))

	def discard_update(self, other):
		self.set.discard_update(other.set)
		self._transform()

	def discard(self, other):
		return Set(self.set.discard(other.set))

	def intersection(self, other):
		return Set(self.set.intersection(other.set))

	def intersection_update(self, other):
		self.set.intersection_update(other.set)
		self._transform()

	def difference_update(self, other):
		self.set.difference_update(other.set)
		self._transform()

	def difference(self, other):
		return Set(self.set.difference(other.set))

	def __copy__(self):
		return Set(self.set.__copy__())

	def __contains__(self, item):
		return self.set.__contains__(item)

	def __len__(self):
		return self.set.__len__()

	def __and__(self, other):
		return Set(self.set.__and__(other.set))

	def __or__(self, other):
		return Set(self.set.__or__(other.set))

	def __iter__(self):
		return self.set.__iter__()

	def __str__(self):
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