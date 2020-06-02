#!/mnt/c/Users/RedKnite/Appdata/local/programs/Python/Python38/python.exe

"""The main process of the Switch language"""

import sys
from itertools import takewhile

#from antlr4 import *
from antlr4 import (ParseTreeWalker, InputStream, FileStream,
	CommonTokenStream, ErrorNode, TerminalNode, tree)

from antlr4.error.ErrorListener import ErrorListener

from Switch.switchLexer import switchLexer
from Switch.switchListener import switchListener
from Switch.switchParser import switchParser


__all__ = ["comp", "SwitchError"]


class SwitchError(SyntaxError):
	"""Syntax error in the Switch language"""

	pass


class ExceptionListener(ErrorListener):
	"""Raise SwitchErrors on Antlr errors not just print statements to
	stderr"""

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		raise SwitchError(f"line {line}:{column} {msg}")

	def reportAmbiguity(
		self,
		recognizer,
		dfa,
		startIndex,
		stopIndex,
		exact,
		ambigAlts,
		configs):
		#raise SwitchError(f"Ambiguity: {startIndex}:{stopIndex}")
		pass

	def reportAttemptingFullContext(
		self,
		recognizer,
		dfa,
		startIndex,
		stopIndex,
		conflictingAlts,
		configs):
		#raise SwitchError("AttemptingFullContext: " + str(conflictingAlts))
		pass

	def reportContextSensitivity(
		self,
		recognizer,
		dfa,
		startIndex,
		stopIndex,
		prediction,
		configs):
		raise SwitchError("ContextSensitivity")


class MyWalker(ParseTreeWalker):
	"""Support the next_child function"""

	def walk(self, listener, node):
		if isinstance(node, ErrorNode):
			listener.visitErrorNode(node)
			return
		if isinstance(node, TerminalNode):
			listener.visitTerminal(node)
			return
		self.enterRule(listener, node)
		for child in node.getChildren():
			self.next_child_rule(listener, node, child)
			self.walk(listener, child)
		self.exitRule(listener, node)

	def next_child_rule(self, listener, r, child):
		"""A function that gets called whenever one of the listed classes
		moves to the next child while walking"""

		# The classes that will call the next_child function
		# next_child must be implemented for all these classes or
		# AttributeError will occur
		call_map = {
			switchParser.ArgsContext: listener.next_child_args,
			switchParser.CallContext: listener.next_child_call,
			switchParser.AccessContext: listener.next_child_access,
			switchParser.AssignmentContext: listener.next_child_assignment,
		}
		ctx = r.getRuleContext()
		call_map.get(type(ctx), lambda a, b: None)(ctx, child)


class SwitchPrintListener(switchListener):
	"""Compile Switch code to python code while walking through
	the parse tree"""

	def __init__(self, output, namespace):
		self.st = [output]
		self.out = output
		self.namespace = namespace
		self.indent = 0

	def enterSwitch_file(self, ctx):
		"""Add initial setup commands for the Switch language"""

		self.st[-1] += (
			b"from Switch.switch_builtins import *\n"
			b"namespace = Namespace()\n"
		)

	def enterWhile_loop(self, ctx):
		"""Indent while loops if they are inside other blocks"""

		self.st[-1] +=  b"while "

	def enterWhile_test(self, ctx):
		"""While loop tests must be handled seperatly from other statments
		because they go between the while keyword and the colon"""

		self.st.append(bytearray(b""))

	def exitWhile_test(self, ctx):
		"""Add the contents of the while test, followed by a colon and a
		newline"""

		val = self.st.pop()
		self.st[-1] += val
		self.st[-1] += b":\n"

	def enterWhile_block(self, ctx):
		"""Increase the indentation"""

		self.indent += 1

	def exitWhile_block(self, ctx):
		"""Decrease the indentaion"""

		self.indent -= 1

		self.st[-1] += b"\n"

	def enterFunction(self, ctx):
		ctx.indent = self.indent
		self.indent = 1
		m = tuple(map(lambda a: a.getText(), ctx.getChildren()))
		args = tuple(takewhile(lambda a: a != "B", m[1:]))
		print(args)
		self.st[-1] += (
			b"exec('''\ndef __f("
			+ b"".join(b"__arg%d" % i for i in range(len(args)))
			+ b"):\n namespace.update("
			+ str({key: "__arg%d" % i for i, key in enumerate(args)}).encode("utf-8")
			+ b")\n")

	def exitFunction(self, ctx):
		self.st[-1] += b"''', ns_d := deepcopy({key: (val if not isinstance(val, ModuleType) else val.__dict__) for key, val in globals().items()})) or ns_d['__f']"
		self.indent = ctx.indent

	def enterLine(self, ctx):
		"""Indent normal lines as well as while loops"""

		self.st[-1] += b" " * self.indent

	def exitLine(self, ctx):
		"""Put newline after each line"""

		self.st[-1] += b"\n"

	def enterPrim_expr(self, ctx):
		"""Evaluate INTEGERs, FLOATs, STRINGs, and NAMEs"""

		table = str.maketrans("zZoO", "0011")
		table[ord(" ")] = None
		table[ord("\t")] = None
		table[ord("\n")] = None
		table[ord("\r")] = None

		if ctx.INT() is not None:
			num = int(ctx.INT().getText().translate(table), 2)
			self.st[-1] += bytes(f"SwitchFrac({num})", "utf-8")

		elif ctx.FLOAT() is not None:
			integer, decimal = ctx.FLOAT().getText().translate(table).split("d")
			int_part = int(integer, 2)

			dec_part = 0
			for index, digit in enumerate(decimal):
				dec_part += float(digit) / 2 ** (index + 1)

			self.st[-1] += bytes(f"SwitchFrac({int_part + dec_part})", "utf-8")

		elif ctx.NAME() is not None:
			try:
				self.st[-1] += bytes(self.namespace[ctx.getText()], "utf-8")
			except KeyError:
				self.st[-1] += bytes(
					"namespace["
					+ repr(ctx.getText())
					+ "]",
					"utf-8")

		elif ctx.STRING() is not None:
			nums = ctx.STRING().getText()[1:].split("s")
			nums = [int(x.translate(table), 2) for x in nums]
			chars = [chr(x) for x in nums]
			self.st[-1] += bytes(f"'{''.join(chars)}'", "utf-8")

	def enterCall(self, ctx):
		"""Start keeping track of how many children have passed"""

		ctx.call_start = 0

	def next_child_call(self, ctx, child):
		"""Add an open paren only if this is the second child"""

		if ctx.call_start == 2:
			self.st[-1] += b"("
		ctx.call_start += 1

	def exitCall(self, ctx):
		"""Add a close paren to function call"""

		self.st[-1] += b")"

	def enterMath_op(self, ctx):
		"""Add the function that corosponds the the correct operator"""

		ops = {
			"t": "mul",
			"v": "truediv",
			"u": "mod",
			"p": "add",
			"m": "sub",
			"j": "less_than",
			"g": "greater_than",
			"q": "equal"
		}

		self.st[-1] += bytes(
			ops[ctx.children[0].getText()],
			"utf-8"
		) + b"("

	def exitMath_op(self, ctx):
		"""Close the function call"""

		self.st[-1] += b")"

	def next_child_args(self, ctx, child):
		"""Add commas where appropriate"""

		if (
			# if this is not the last child
			tuple(ctx.getChildren())[0] != child
			# and this is not an ARG_DELIMITER
			and not isinstance(child, tree.Tree.TerminalNodeImpl)
		):
			self.st[-1] += b","

	def enterAssignment(self, ctx):
		"""Assignment must be handeled as a whole to use the Namespace walrus
		method"""

		# bytearray for the value to be assigned
		self.st.append(bytearray(b""))

	def next_child_assignment(self, ctx, child):
		"""Prepare to handle access assignment"""

		if isinstance(child, switchParser.AccessContext):
			# bytearray for the access to be assigned to
			self.st.append(bytearray(b""))
			# var to indicate to the AccessContext that it needs to treat
			# the last access differently
			child.split_last = True

		# is an access expression
		if not ctx.NAME() and isinstance(child, switchParser.ExprContext):
			# pull the bytearray for the value forward and push
			# the bytearray for the access backward
			self.st[-1], self.st[-2] = self.st[-2], self.st[-1]

	def exitAssignment(self, ctx):
		"""Add code to call the Namespace walrus method with arguments"""

		if ctx.NAME():
			val = self.st.pop()
			py_assign = (
				b"namespace.walrus("
				+ bytes(repr(ctx.NAME().getText()), "utf-8")
				+ b", "
				+ val
				+ b")"
			)
			self.st[-1] += py_assign
		else:
			val = self.st.pop()
			obj = self.st.pop()
			self.st[-1] += obj[0] + b".walrus(" + obj[1] + b"," + val + b")"

	def enterAccess(self, ctx):
		"""Start keeping track of how many children have passed"""

		# must be ctx attribute so that nested access works
		# otherwise the counter would be reset to 0
		ctx.child_counter = 0

	def next_child_access(self, ctx, child):
		"""Add open and closing brackets for indexing"""

		# Do the normal thing if not splitting last access off
		if (
			# split_last may not exist so the getattr is helpful
			not getattr(ctx, "split_last", None)
			or ctx.child_counter < len(tuple(ctx.getChildren())) - 2
		):
			if (
				child.getText() != "n" and
				3 < ctx.child_counter < len(tuple(ctx.getChildren())) - 0
			):
				self.st[-1] += b"]"

			if (
				child.getText() not in "n" and
				1 < ctx.child_counter < len(tuple(ctx.getChildren())) - 1
			):
				self.st[-1] += b"["
		else:
			# add additional bytearray for the last part of the access
			if ctx.child_counter < len(tuple(ctx.getChildren())) - 1:
				self.st.append(bytearray(b""))
			else:
				last_access = self.st.pop()
				first_accesses = self.st.pop()
				self.st.append((first_accesses, last_access))

		ctx.child_counter += 1

	def exitAccess(self, ctx):
		"""Stop child counting and clean up"""

		del ctx.child_counter
		try:
			del ctx.split_last
		except AttributeError:
			pass


def comp(source, file=False):
	"""Parse the Switch source code and walk it, then return the python
	code"""

	output = bytearray("", "utf-8")

	namespace = {
		"->": "print_no_nl",
		":": "SwitchMap",
		"...": "SwitchList",
	}

	if file:
		lexer = switchLexer(FileStream(source))
	else:
		lexer = switchLexer(InputStream(source))

	stream = CommonTokenStream(lexer)
	parser = switchParser(stream)

	lexer.removeErrorListeners()
	lexer.addErrorListener(ExceptionListener())

	parser.removeErrorListeners()
	parser.addErrorListener(ExceptionListener())

	parse_tree = parser.switch_file()
	printer = SwitchPrintListener(output, namespace)
	walker = MyWalker()
	walker.walk(printer, parse_tree)

	return output


def main():
	"""Determine what the program should take input and what output is
	wanted"""

	try:
		assert sys.argv[1] == "-f"
		output = comp(sys.argv[2], True)
	except AssertionError:
		output = comp(sys.argv[1])
	except IndexError:
		pass

	minimal = None
	if "-m" in sys.argv:
		minimal = "m"
	elif "-c" in sys.argv:
		minimal = "c"

	if not minimal:
		print("Output:")

	if minimal != "m":
		print(output.decode())

	if not minimal:
		print("\nRun:")

	if minimal != "c":
		try:
			exec(output.decode())
		except Exception:
			print("Switch Excpetion: ")
			raise


if __name__ == '__main__':
	main()
