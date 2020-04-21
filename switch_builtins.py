
from functools import reduce
from fractions import Fraction

__all__ = [
	"SwitchFrac",
	"Namespace",
	"SwitchList",
	"SwitchMap",
	"print_no_nl",
	"add",
	"sub",
	"mul",
	"truediv",
	"mod",
	"less_than",
	"greater_than",
	"equal",
]


def return_same_class(cls):
	def wrap(func):
		return lambda self, *args, **kwargs: self.__class__(func(self, *args, **kwargs))

	methods = (
		"__add__", "__radd__",
		"__sub__", "__rsub__",
		"__mul__", "__rmul__",
		"__truediv__", "__rtruediv__",
		"__mod__", "__rmod__",
		"limit_denominator"
	)

	for method in methods:
		wrapped = wrap(getattr(cls, method))
		setattr(cls, method, wrapped)

	return cls

def limit_float_denominators(method):
	def func(self, other):
		if isinstance(other, float):
			return getattr(self, method)(self.__class__(other).limit_denominator())

		return getattr(super(SwitchFracBase, self), method)(other)
	return func

def overload_math_dunder_methods(func):
	def decorator(cls):
		methods = (
			"__add__", "__radd__",
			"__sub__", "__rsub__",
			"__mul__", "__rmul__",
			"__truediv__", "__rtruediv__",
			"__mod__", "__rmod__"
		)

		for method in methods:
			f = func(method)
			setattr(cls, method, f)

		return cls
	return decorator

@return_same_class
@overload_math_dunder_methods(limit_float_denominators)
class SwitchFracBase(Fraction):
	def __str__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator / self.denominator)

	def is_integer(self):
		return self.denominator == 1


class SwitchFrac(SwitchFracBase):
	def __mul__(self, other):
		try:
			return super().__mul__(other)
		except TypeError:
			if self.denominator == 1:
				return self.numerator * other
			else:
				raise

	def __rmul__(self, other):
		try:
			return super().__rmul__(other)
		except TypeError:
			if self.denominator == 1:
				return other * self.numerator
			else:
				raise

class Namespace(dict):
	def walrus(self, key, value):
		self[key] = value
		return value

class SwitchList(dict):
	def __init__(self, *args):
		super().__init__()
		self.length = len(args)
		self.update({
			"add": lambda a: self.append(a),
			"pop": lambda: self.pop(self.length - 1),
			"len": self.length,
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


def print_no_nl(*args, **kwargs):
	kw = {"end": ""}
	kw.update(kwargs)
	print(*args, **kw)

def add(*args):
	return reduce(lambda a, b: a + b, args)

def sub(*args):
	return reduce(lambda a, b: a - b, args)

def mul(*args):
	return reduce(lambda a, b: a * b, args)

def truediv(*args):
	return reduce(lambda a, b: a / b, args)

def mod(*args):
	return reduce(lambda a, b: a % b, args)

def less_than(*args):
	total = []
	for i in range(len(args) - 1):
		total.append(args[i] < args[i + 1])
	return all(total)

def greater_than(*args):
	total = []
	for i in range(len(args) - 1):
		total.append(args[i] > args[i + 1])
	return all(total)

def equal(*args):
	total = []
	for i in range(len(args) - 1):
		total.append(args[i] == args[i + 1])
	return all(total)

