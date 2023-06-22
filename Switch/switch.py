#!/usr/bin/env python3

"""Command line interface of Switch"""

import sys
from pathlib import Path

from Switch.Sw import *
from Switch.errors import *

# run from directory with Switch directory in it with:
# python -m Switch.switch

def main():
	"""Determine what the program should take input and what output is
	wanted"""

	try:
		assert sys.argv[1] == "-f"
		output = comp(sys.argv[2], True)
	except AssertionError:
		output = comp(sys.argv[1])
	except IndexError:
		raise SwitchError("Switch requires arguments")

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
			if "-p" in sys.argv:
				exec(output.decode(), {})
			else:
				with open(Path(__file__).parent.absolute() / "out.py", "w+") as file:
					file.write(output.decode())
				import Switch.out
		except Exception as exc:
			raise SwitchError(exc) from exc

if __name__ == "__main__":
	main()
