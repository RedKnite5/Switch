#!/cygdrive/c/Users/RedKnite/Appdata/local/programs/Python/Python38/python.exe

from antlr4 import *
from switchLexer import switchLexer
from switchListener import switchListener
from switchParser import switchParser
import sys
from functools import reduce

from pprint import pprint

def add(*args):
	return reduce(lambda a, b: a + b, args)


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
		}
		ctx = r.getRuleContext()
		map.get(type(ctx), lambda a, b: None)(ctx, child)



class switchPrintListener(switchListener):
	def __init__(self, output, ns):
		self.st = [output]
		self.out = output
		self.ns = ns

	def enterExpr(self, ctx):
		#print("Text: ", ctx.getText())
		pass
	
	def enterPrim_expr(self, ctx):
		table = str.maketrans("zZoO", "0011")
		
		if ctx.INT() is not None:
			num = int(ctx.INT().getText().translate(table), 2)
			self.st[-1] += bytes(str(num), "utf-8")
		elif ctx.FLOAT() is not None:
			integer, decimal = ctx.FLOAT().getText().split("d")
			int_part = int(integer.translate(table), 2)
			
			dec_part = 0
			for d in range(len(decimal)):
				dec_part += float(decimal[d]) / 2**(d + 1)
			
			self.st[-1] += bytes(str(int_part + dec_part), "utf-8")
			
		elif ctx.NAME() is not None:
			if False:
				pass
			else:
				self.st[-1] += bytes(self.ns[ctx.getText()], "utf-8")
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
	
	def enterM_expr(self, ctx):
		ops = {
			"t": "mul",
			"v": "truediv",
			"u": "mod"
		}
		
		self.st[-1] += bytes(
			ops[ctx.children[0].getText()],
			"utf-8"
		) + b"("
	
	def exitM_expr(self, ctx):
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
		self.ns[ctx.NAME().getText()] = self.st[-1].decode("utf-8")
		val = self.st.pop()
		self.st[-1] += val
	
	
			

def run(s):
	return eval(s)

def main():
	output = bytearray("", "utf-8")
	namespace = {"->": "print"}
	
	lexer = switchLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = switchParser(stream)
	tree = parser.expr()
	printer = switchPrintListener(output, namespace)
	walker = MyWalker()
	walker.walk(printer, tree)
	
	print("Output: ", output.decode())
	print("Run: ", run(output.decode()))
	
	
	

if __name__ == '__main__':
	print("Enter text: \n")
	main()