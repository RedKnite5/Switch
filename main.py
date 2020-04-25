#!/mnt/c/Users/RedKnite/Appdata/local/programs/Python/Python38/python.exe

from antlr4 import *
from switchLexer import switchLexer
from switchListener import switchListener
from switchParser import switchParser
from antlr4.error.ErrorListener import ErrorListener

import sys

__all__ = ["comp", "SwitchError"]

class SwitchError(SyntaxError):
	pass

class MyErrorListener(ErrorListener):
	"""Raise SwitchErrors on Antlr errors not just print statements to
	stderr"""

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		raise SwitchError(f"line {line}:{column} {msg}")

	def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
		#raise SwitchError(f"Ambiguity: {startIndex}:{stopIndex}")
		pass

	def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
		#raise SwitchError("AttemptingFullContext: " + str(conflictingAlts))
		pass

	def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
		raise SwitchError("ContextSensitivity")

class MyWalker(ParseTreeWalker):
	"""Support the nextChildf unction"""

	def walk(self, listener, t):
		if isinstance(t, ErrorNode):
			listener.visitErrorNode(t)
			return
		elif isinstance(t, TerminalNode):
			listener.visitTerminal(t)
			return
		self.enterRule(listener, t)
		for child in t.getChildren():
			self.nextChildRule(listener, t, child)
			self.walk(listener, child)
		self.exitRule(listener, t)

	def nextChildRule(self, listener, r, child):
		"""A function that gets called whenever one of the listed classes
		moves to the next child while walking"""

		# The classes that will call the nextChild function
		# nextChild must be implemented for all these classes or
		# AttributeError will occur
		map = {
			switchParser.ArgsContext: listener.nextChildArgs,
			switchParser.CallContext: listener.nextChildCall,
			switchParser.AccessContext: listener.nextChildAccess,
			switchParser.AssignmentContext: listener.nextChildAssignment,
		}
		ctx = r.getRuleContext()
		map.get(type(ctx), lambda a, b: None)(ctx, child)



class switchPrintListener(switchListener):
	def __init__(self, output, ns):
		self.st = [output]
		self.out = output
		self.ns = ns
		self.indent = 0

	def enterSwitch_file(self, ctx):
		"""Add initial setup commands for the Switch language"""

		self.st[-1] += (
			b"from switch_builtins import *\n"
			b"namespace = Namespace()\n"
		)

	def enterWhile_loop(self, ctx):
		"""Indent while loops if they are inside other blocks"""

		self.st[-1] += b" " * self.indent + b"while "

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

	def enterLine(self, ctx):
		"""Indent normal lines as well as while loops"""

		#children = ctx.getChildren()
		#for child in children:
		#	if isinstance(
		#		child,
		#		(switchParser.ExprContext, switchParser.While_loopContext)
		#	):
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
			for d in range(len(decimal)):
				dec_part += float(decimal[d]) / 2 ** (d + 1)

			self.st[-1] += bytes(f"SwitchFrac({int_part + dec_part})", "utf-8")

		elif ctx.NAME() is not None:
			try:
				self.st[-1] += bytes(self.ns[ctx.getText()], "utf-8")
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

		self.call_start = 0

	def nextChildCall(self, ctx, child):
		"""Add an open paren only if this is the second child"""

		if self.call_start == 2:
			self.st[-1] += b"("
		self.call_start += 1

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

	def nextChildArgs(self, ctx, child):
		"""Add commas where appropriate"""

		if (
			# if this is not the last child
			tuple(ctx.getChildren())[0] != child
			# and this is not an ARG_DELIMITER
			and type(child) != tree.Tree.TerminalNodeImpl
		):
			self.st[-1] += b","

	def enterAssignment(self, ctx):
		"""Assignment must be handeled as a whole to use the Namespace walrus
		method"""

		# bytearray for the value to be assigned
		self.st.append(bytearray(b""))

	def nextChildAssignment(self, ctx, child):
		"""Prepare to handle access assignment"""

		if isinstance(child, switchParser.AccessContext):
			# bytearray for the access to be assigned to
			self.st.append(bytearray(b""))
			# var to indicate to the AccessContext that it needs to treat
			# the last access differently
			child._split_last = True

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
		ctx._child_counter = 0

	def nextChildAccess(self, ctx, child):
		"""Add open and closing brackets for indexing"""

		# Do the normal thing if not splitting last access off
		if (
			# _split_last may not exist so the getattr is helpful
			not getattr(ctx, "_split_last", None)
			or ctx._child_counter < len(tuple(ctx.getChildren())) - 2
		):
			if (
				child.getText() != "n" and
				3 < ctx._child_counter < len(tuple(ctx.getChildren())) - 0
			):
				self.st[-1] += b"]"

			if (
				child.getText() not in "n" and
				1 < ctx._child_counter < len(tuple(ctx.getChildren())) - 1
			):
				self.st[-1] += b"["
		else:
			# add additional bytearray for the last part of the access
			if ctx._child_counter < len(tuple(ctx.getChildren())) - 1:
				self.st.append(bytearray(b""))
			else:
				p2 = self.st.pop()
				p1 = self.st.pop()
				self.st.append((p1, p2))

		ctx._child_counter += 1

	def exitAccess(self, ctx):
		"""Stop child counting and clean up"""

		del ctx._child_counter
		try:
			del ctx._split_last
		except AttributeError:
			pass


def comp(input, file=False):
	"""Parse the Switch source code and walk it, then return the python
	code"""

	output = bytearray("", "utf-8")

	namespace = {
		"->": "print_no_nl",
		":": "SwitchMap",
		"...": "SwitchList",
	}

	if file:
		lexer = switchLexer(FileStream(input))
	else:
		lexer = switchLexer(InputStream(input))

	stream = CommonTokenStream(lexer)
	parser = switchParser(stream)

	lexer.removeErrorListeners()
	lexer.addErrorListener(MyErrorListener())

	parser.removeErrorListeners()
	parser.addErrorListener(MyErrorListener())

	tree = parser.switch_file()
	printer = switchPrintListener(output, namespace)
	walker = MyWalker()
	walker.walk(printer, tree)

	return output


def main():
	"""Determine what the program should take input and what output is
	wanted"""

	try:
		assert(sys.argv[1] == "-f")
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


