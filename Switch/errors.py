"""Error Types"""


class SwitchError(SyntaxError):
	"""Syntax error in the Switch language"""

class SwitchKeyError(SwitchError, KeyError):
	"""Key error in Switch"""
