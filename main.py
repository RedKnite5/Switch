#!/cygdrive/c/Users/RedKnite/Appdata/local/programs/Python/Python38/python.exe

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
	def __init__(self):
		super(MyErrorListener, self).__init__()

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		raise SwitchError("line " + str(line) + ":" + str(column) + " " + msg)


class MyWalker(ParseTreeWalker):
	def walk(self, listener, t):
		if isinstance(t, ErrorNode):
			listener.visitErrorNode(t)
			return
		elif isinstance(t, TerminalNode):
			listener.visitTerminal(t)
			return
		self.enterRule(listener, t)
		for child in t.getChildren():
			self.walk(listener, child)
			self.nextChildRule(listener, t, child)
		self.exitRule(listener, t)

	def nextChildRule(self, listener, r, child):
		map = {
			switchParser.ArgsContext: listener.nextChildArgs,
			switchParser.CallContext: listener.nextChildCall,
			switchParser.AccessContext: listener.nextChildAccess,
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
		self.st[-1] += (
			b"from switch_builtins import *\n"
			b"namespace = Namespace()\n"
		)

	def enterWhile_loop(self, ctx):
		self.st[-1] += b"while "
	
	def enterWhile_test(self, ctx):
		self.st.append(bytearray(b""))
	
	def exitWhile_test(self, ctx):
		val = self.st.pop()
		self.st[-1] += val
		self.st[-1] += b":\n"
	
	def enterWhile_block(self, ctx):
		self.indent += 1
	
	def exitWhile_block(self, ctx):
		self.indent -= 1

	def enterLine(self, ctx):
		children = ctx.getChildren()
		for child in children:
			if isinstance(child, switchParser.ExprContext):
				self.st[-1] += b" " * self.indent

	def exitLine(self, ctx):
		self.st[-1] += b"\n"
		
	def enterExpr(self, ctx):
		#print("Text: ", ctx.getText())
		pass

	def enterPrim_expr(self, ctx):
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
		self.call_start = 0

	def nextChildCall(self, ctx, child):
		if self.call_start == 1:
			self.st[-1] += b"("
		self.call_start += 1

	def exitCall(self, ctx):
		self.st[-1] += b")"

	def enterMult(self, ctx):
		ops = {
			"t": "mul",
			"v": "truediv",
			"u": "mod"
		}
		
		self.st[-1] += bytes(
			ops[ctx.children[0].getText()],
			"utf-8"
		) + b"("

	def exitMult(self, ctx):
		self.st[-1] += b")"

	def enterAdd_sub_expr(self, ctx):
		ops = {
			"p": "add",
			"m": "sub"
		}
		
		self.st[-1] += bytes(
			ops[ctx.children[0].getText()],
			"utf-8"
		) + b"("

	def exitAdd_sub_expr(self, ctx):
		self.st[-1] += b")"

	def enterComp(self, ctx):
		ops = {
			"j": "less_than",
			"g": "greater_than",
			"q": "equal"
		}
		
		self.st[-1] += bytes(
			ops[ctx.children[0].getText()],
			"utf-8"
		) + b"("

	def exitComp(self, ctx):
		self.st[-1] += b")"
	
	def nextChildArgs(self, ctx, child):
		if (
			tuple(ctx.getChildren())[-1] != child
			and type(child) != tree.Tree.TerminalNodeImpl
		):
			self.st[-1] += b","

	def enterAssignment(self, ctx):
		if ctx.NAME():
			self.st.append(bytearray(b""))

	def exitAssignment(self, ctx):
		val = self.st.pop()
		py_assign = (
			b"namespace.walrus("
			+ bytes(repr(ctx.NAME().getText()), "utf-8")
			+ b", "
			+ val
			+ b")"
		)
		self.st[-1] += py_assign

	def enterAccess(self, ctx):
		ctx._child_counter = 0
	
	def nextChildAccess(self, ctx, child):
		if (
			child.getText() != "n" and 
			1 < ctx._child_counter < len(tuple(ctx.getChildren()))
		):
			self.st[-1] += b"]"

		if (
			child.getText() != "n" and 
			0 < ctx._child_counter < len(tuple(ctx.getChildren())) - 1
		):
			self.st[-1] += b"["
		
		ctx._child_counter += 1
	
	def exitAccess(self, ctx):
		del ctx._child_counter


def comp(input, file=False):
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


if __name__ == '__main__':
	try:
		assert(sys.argv[1] == "-f")
		output = comp(sys.argv[2], True)
	except AssertionError:
		output = comp(sys.argv[1])
	except IndexError:
		pass

	print("Output:\n", output.decode(), sep="")

	print("\nRun: ")
	try:
		exec(output.decode())
	except Exception:
		print("Switch Excpetion: ")
		raise

