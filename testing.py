
import sys
import unittest
from io import StringIO

from main import comp, SwitchError


old_stdout = sys.stdout
old_stderr = sys.stderr

def run(tester, source_code, output):
	code = comp(source_code)
	exec(code)
	tester.assertEqual(sys.stdout.getvalue(), output)



class TestPrimitivePrinting(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_print_one(self):
		code = comp("c->nOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "1")

	def test_print_four(self):
		code = comp("c->nOZZl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "4")

	def test_print_thirteen(self):
		code = comp("c->nOOZOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "13")

	def test_lowercase_numbers(self):
		code = comp("c->noozol")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "13")

	def test_mixedcase_numbers(self):
		code = comp("c->noOZozl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "26")

	def test_numbers_with_spaces(self):
		code = comp("c->no  OZ \n o	z\tl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "26")

	def test_print_A(self):
		code = comp("c->nSOZZZZZOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "A")

	def test_print_A_lowercase_numbers(self):
		code = comp("c->nSozzzzzol")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "A")

	def test_print_A_mixedcase_numbers(self):
		code = comp("c->nSoZZzzzOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "A")

	def test_print_A_lowercase_s_fails(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ token recognition error at: (.*)",
			comp,
			"c->nsoZZzzzOl")

	def test_print_Hello(self):
		code = comp("c->nSOZZOZZZsOOZZOZOsOOZOOZZsOOZOOZZsOOZOOOOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "Hello")

	def test_print_Hello_uppercase_s_fails(self):

		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ no viable alternative at input (.*)",
			comp,
			"c->nSOZZOZZZSOOZZOZOSOOZOOZZSOOZOOZZSOOZOOOOl")

	def test_print_Hello_spaces(self):
		code = comp("c->nSOZZOZZZ sOOZZOZO sOOZOOZZ sOOZOOZZ sOOZOOOOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "Hello")

	def test_print_float_1d0(self):
		code = comp("c->nOdZl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "1")

	def test_print_float_0d25(self):
		code = comp("c->nZdZOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "0.25")

	def test_print_float_0d75(self):
		code = comp("c->nZdOOl")
		exec(code)
		self.assertEqual(sys.stdout.getvalue(), "0.75")


class TestLines(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_line(self):
		run(self, "c->nOlLc->nOl", "11")

	def test_line_no_EOF(self):
		run(self, "c->nOlLc->nOlL", "11")

	def test_line_nl_are_no_substiture(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ no viable alternative at input (.*)",
			comp,
			"c->nOl \n c->nOlL")

	def test_empty_lines(self):
		run(self, "c->nOl L L c->nOl", "11")

	def test_empty_file(self):
		run(self, "", "")

	def test_3_empty_lines(self):
		run(self, "LLL", "")

	def test_literal_newlines_(self):
		run(self, """LL
		L""", "")


class TestAssignment(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_assignment_star_equals_1(self):
		run(self, "e*nOLc->n*l", "1")

	def test_assignment_star_equals_A(self):
		run(self, "e*nSOZZZZZOLc->n*l", "A")

	def test_assignment_star_equals_AB(self):
		run(self, "e*nSOZZZZZOsOZZZZOZLc->n*l", "AB")

	def test_assignment_star_equals_13(self):
		run(self, "e*nOOZOLc->n*l", "13")

	def test_assignment_percent_equals_1(self):
		run(self, "e%nOLc->n%l", "1")

	def test_assignment_backslash_equals_1(self):
		run(self, "e\\nOLc->n\\l", "1")

	def test_assignment_double_quote_equals_1(self):
		run(self, "e\"nOLc->n\"l", "1")

	def test_assignment_single_quote_equals_1(self):
		run(self, "e\'nOLc->n\'l", "1")

	def test_assignment_mess_equals_1(self):
		run(self, "e{}{{)(&%^&||\\\"\"nOLc->n{}{{)(&%^&||\\\"\"l", "1")

	def test_assignment_star_equals_0d25(self):
		run(self, "e*nZdZOLc->n*l", "0.25")

	def test_words_dont_work_as_var_names(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ token recognition error at: (.*)",
			comp,
			"exnOLc->nxl")

	def test_numbers_dont_work_as_var_names(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ token recognition error at: (.*)",
			comp,
			"e6nOLc->n6l")

	def test_variables_can_change(self):
		run(self, "e*nZLc->n*lLe*nOLc->n*l", "01")

	def test_variables_can_change_in_loop(self):
		run(self, "e?nZL W j?nOZOZ Wb c->n?l L e?np?nO L w", "0123456789")


class TestMath(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_print_addition(self):
		run(self, "c->npOnOZl", "3")

	def test_assign_addition(self):
		run(self, "e.npOnOZLc->n.l", "3")

	def test_print_addition_of_strings(self):
		run(self,
		"c->n p SOZZZZZO n SOZZZZOZl",
		"AB")

	def test_chain_addition(self):
		run(self, "c->n pOn OZZ n O n Zl", "6")

	def test_addition_of_floats(self):
		run(self, "c->n p OdO n ZdZO l", "1.75")

	def test_multiplication(self):
		run(self, "c->n t OZO n OZl", "10")

	def test_multiplication_of_floats(self):
		run(self, "c->n t OdO n OZdOl", "3.75")

	def test_chain_multiplication(self):
		run(self, "c->n tOn OO n OZZl", "12")

	def test_multiplication_between_integer_and_string(self):
		run(self, "c->n tSOZZZZZO n OOl", "AAA")

	def test_subtraction(self):
		run(self, "c->n m OOO n Ol", "6")

	def test_subraction_to_negative(self):
		run(self, "c->n m OZ n OZZl", "-2")

	def test_subtraction_of_floats(self):
		run(self, "c->n m ZdO n OdZOl", "-0.75")

	def test_chain_subtraction(self):
		run(self, "c->n m OZOZ n OZ n OZOl", "3")

	def test_division(self):
		run(self, "c->n v OZOZ n OZl", "5")

	def test_division_to_float(self):
		run(self, "c->n v OO n OOZl", "0.5")

	def test_division_of_floats(self):
		run(self, "c->n v OdO n ZdOl", "3")

	def test_mod(self):
		run(self, "c->n u OZZZ n OOl", "2")

	def test_chain_mod(self):
		run(self, "c->n u OZZZZZZ n OZOZ n OZl", "0")

	def test_mod_with_floats(self):
		run(self, "c->n u OdZO n ZdOl", "0.25")

	def test_less_than_true(self):
		run(self, "c->n j O n OOl", "True")

	def test_less_than_false(self):
		run(self, "c->n j OZO n OOl", "False")

	def test_less_than_chain_true(self):
		run(self, "c->n j O n OOO n OZZZl", "True")

	def test_less_than_chain_false(self):
		run(self, "c->n j OO n OZZO n OZZZl", "False")

	def test_less_than_with_floats(self):
		run(self, "c->n j OdO n OdOOl", "True")

	def test_greater_than_true(self):
		run(self, "c->n g OOZ n OZl", "True")

	def test_greater_than_false(self):
		run(self, "c->n g O n OZZl", "False")

	def test_chain_greater_than_true(self):
		run(self, "c->n g OOOO n  OZOZ n OOO n Zl", "True")

	def test_chain_greater_than_false(self):
		run(self, "c->n g OOOZ n OOOO n Ol", "False")

	def test_greater_than_with_floats(self):
		run(self, "c->n g ZdOOZO n ZdOZOOl", "True")

	def test_equals_true(self):
		run(self, "c->n q OO n OOl", "True")

	def test_equals_false(self):
		run(self, "c->n q O n Zl", "False")


class TestAccess(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_access_list_integers(self):
		run(self, "e.nc...nZnOnOZlL c->ni.nOZl", "2")

	def test_access_list_strings(self):
		run(self,
			"""e.nc...n SOZZZZZO n SOZZZZOZ lL
			c->ni.nOl""", "B")

	def test_access_map_integer_to_integer(self):
		run(self, "e.nc:nZnOnOnZlL c->ni.nOl", "0")

	def test_access_map_string_to_integer(self):
		run(self,
			"""e.nc:n SOZZZZZO n O n SOZZZZOO n OZZ lL
			c->ni.nSOZZZZOOl""", "4")

	def test_access_map_integer_to_string(self):
		run(self,
			"""e.nc:n OZZZ n SOZZZZOO n OO n SOZZZZOZ lL
			c->ni.nOZZZl""", "C")

	def test_chained_access_list_integers(self):
		run(self,
			"""e-nc...nOOnOOZlL
			e.nc...nZnOn-nOZlL
			c->ni.nOZnOl""", "6")


class TestWhileLoop(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_while_false_wont_start(self):
		run(self, "W Z Wb c->nOlL w", "")


class TestListAndMap(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_list(self):
		run(self, "c->n c...n O n OZ n OO n OZZl l", "[1,2,3,4]")

	def test_map(self):
		run(self, "c->n c:n OnO n OZnOOl l", "{1:1,2:3}")

	def test_list_strings(self):
		run(self,
			"""
			e*n c...n SOZZZZZO sOZZZZOZ n SOZZZZOOl L
			c->n * l
			""",
			"[AB,C]")
		# Lack of quotes around strings may or may not be a problem

	def test_map_strings(self):
		run(self,
			"""
			e*n c:n SOZZZZZO sOZZZZOZnSOZZZZOO l L
			c->n * l
			""",
			"{AB:C}")

	def test_list_append(self):
		run(self,
			"""
			e*n c...n OO n OZ l L
			ci*n SOOZZZZO sOOZZOZZ sOOZZOZZ n Z l L
			c->n * l
			""",
			"[3,2,0]")


if __name__ == "__main__":
	unittest.main()
