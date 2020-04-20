
from functools import reduce

class Namespace(dict):
	def walrus(self, key, value):
		self[key] = value
		return value

class SwitchList(dict):
	def __init__(self, *args):
		super().__init__()
		self.length = len(args)
		self.update({
			"append": lambda a: self.append(a),
			"pop": lambda: self.pop(self.length - 1),
			"length": self.length,
		})
		self.update(dict(enumerate(args)))

	def append(self, val):
		self.update({self.length: val})
		self.length += 1

	def __str__(self):
		s = "["
		for i in range(self.length):
			s += str(self[i]) + ","
		return s[:-1] + "]"

class SwitchMap(dict):
	def __init__(self, *args):
		super().__init__()

		it = iter(args)
		for x in it:
			try:
				self.update({x: next(it)})
			except StopIteration:
				raise ValueError("Must have an even number of items")

	def __str__(self):
		s = "{"
		for key, val in self.items():
			s += f"{key}:{val},"
		return s[:-1] + "}"


class Number(int, float):
	pass

def print_no_nl(*args, **kwargs):
	print(*args, end="", **kwargs)

def add(*args):
	return reduce(lambda a, b: a + b, args)

def sub(*args):
	return reduce(lambda a, b: a - b, args)

def mul(*args):
	return reduce(lambda a, b: a * b, args)

def truediv(*args):
	r = reduce(lambda a, b: a / b, args)
	if r.is_integer():
		return int(r)
	return r

def mod(*args):
	return reduce(lambda a, b: a % b, args)

def less_than(*args):
	total = []
	for i in range(len(args)):
		if i == len(args) - 1:
			return all(total)
		total.append(args[i] < args[i + 1])

def greater_than(*args):
	total = []
	for i in range(len(args)):
		if i == len(args) - 1:
			return all(total)
		total.append(args[i] > args[i + 1])

def equal(*args):
	total = []
	for i in range(len(args)):
		if i == len(args) - 1:
			return all(total)
		total.append(args[i] == args[i + 1])

