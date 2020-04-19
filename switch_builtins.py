
from functools import reduce

class Namespace(dict):
	def walrus(self, key, value):
		self[key] = value
		return value

class SwitchList(dict):
	def __init__(self, *args):
		super().__init__()
		self.update(dict(enumerate(args)))

class SwitchMap(dict):
	def __init__(self, *args):
		super().__init__()

		it = iter(args)
		for x in it:
			try:
				self.update({x: next(it)})
			except StopIteration:
				raise ValueError("Must have an even number of items")

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
		total.append(args[i] > args[i + 1])

