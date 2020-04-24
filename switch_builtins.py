
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
	"""Wrap the methods in 'methods' so that they will return an instance of
	the class that they were called from, not any base classes"""

	def wrap(func):
		"""Wrap func so that it returns the type of the first argument"""

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

def limit_float_denominators(method, cls):
	"""Wrap method so that the denominators of floats are limited when used
	in operations"""

	def func(self, other):
		"""If other is a float convert it the the type of self and call
		limit_denominator on it, before calling method on it. Otherwise proced
		as normal"""

		if isinstance(other, float):
			return getattr(self, method)(self.__class__(other).limit_denominator())

		return getattr(super(cls, self), method)(other)
	return func

def overload_math_dunder_methods(func):
	"""Create a decorator that wraps methods of a class in func"""

	def decorator(cls):
		"""Wrap the methods in 'methods' in func"""

		methods = (
			"__add__", "__radd__",
			"__sub__", "__rsub__",
			"__mul__", "__rmul__",
			"__truediv__", "__rtruediv__",
			"__mod__", "__rmod__"
		)

		for method in methods:
			f = func(method, cls)
			setattr(cls, method, f)

		return cls
	return decorator

@return_same_class
@overload_math_dunder_methods(limit_float_denominators)
class SwitchFracBase(Fraction):
	"""The base number class for Switch"""

	def __str__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator / self.denominator)

	def __repr__(self):
		if self.denominator == 1:
			return str(self.numerator)
		else:
			return str(self.numerator / self.denominator)

	# I forget what raised an error when this wasn't there
	# I should figure it out so I know if it is safe to deleter
	# Don't delete before then. Its not hurting anything :)
	def is_integer(self):
		return self.denominator == 1


class SwitchFrac(SwitchFracBase):
	"""Number class for Switch"""

	def __mul__(self, other):
		"""Multiplication by strings and other sequences should work if self
		is a whole number"""

		try:
			return super().__mul__(other)
		except TypeError:
			if self.denominator == 1:
				return self.numerator * other
			else:
				raise

	def __rmul__(self, other):
		"""Multiplication by strings and other sequences should work if self
		is a whole number"""

		try:
			return super().__rmul__(other)
		except TypeError:
			if self.denominator == 1:
				return other * self.numerator
			else:
				raise

class Namespace(dict):
	"""Namespace for Switch"""

	def walrus(self, key, value):
		"""Set key to value and return value"""

		self[key] = value
		return value

class SwitchList(dict):
	"""A list for Switch"""

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
			s += repr(self[i]) + ","
		return s[:-1] + "]"

class SwitchMap(dict):
	"""A dictionary for Switch"""

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
			s += f"{repr(key)}:{repr(val)},"
		return s[:-1] + "}"


def print_no_nl(*args, **kwargs):
	"""Wrap the print function so that the default end argument is
	the empty string"""

	kw = {"end": ""}
	kw.update(kwargs)
	print(*args, **kw)

def add(*args):
	"""Add all the arguments"""

	return reduce(lambda a, b: a + b, args)

def sub(*args):
	"""Subtract all arguments after the first from the first one"""

	return reduce(lambda a, b: a - b, args)

def mul(*args):
	"""Multiply all the arguments together"""

	return reduce(lambda a, b: a * b, args)

def truediv(*args):
	"""Divide the first argument by all subsequent ones"""

	return reduce(lambda a, b: a / b, args)

def mod(*args):
	"""Return the first argument mod the rest in order"""

	return reduce(lambda a, b: a % b, args)

def less_than(*args):
	"""Return True if all arguments are in ascending order"""

	for i in range(len(args) - 1):
		if not args[i] < args[i + 1]:
			return False
	return True

def greater_than(*args):
	"""Return True if all arguments are in decending order"""

	for i in range(len(args) - 1):
		if not args[i] > args[i + 1]:
			return False
	return True

def equal(*args):
	"""Return True if all arguments are equal"""

	for i in args[1:]:
		if not args[0] == i:
			return False
	return True

