
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
		self.assertRaises(
			SwitchError,
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
		run(self, "e*nOlLc->n*l", "1")

	def test_assignment_star_equals_A(self):
		run(self, "e*nSOZZZZZOlLc->n*l", "A")

	def test_assignment_star_equals_AB(self):
		run(self, "e*nSOZZZZZOsOZZZZOZlLc->n*l", "AB")

	def test_assignment_star_equals_13(self):
		run(self, "e*nOOZOlLc->n*l", "13")

	def test_assignment_percent_equals_1(self):
		run(self, "e%nOlLc->n%l", "1")

	def test_assignment_backslash_equals_1(self):
		run(self, "e\\nOlLc->n\\l", "1")

	def test_assignment_double_quote_equals_1(self):
		run(self, "e\"nOlLc->n\"l", "1")

	def test_assignment_single_quote_equals_1(self):
		run(self, "e\'nOlLc->n\'l", "1")

	def test_assignment_mess_equals_1(self):
		run(self, "e{}{{)(&%^&||\\\"\"nOlLc->n{}{{)(&%^&||\\\"\"l", "1")

	def test_assignment_star_equals_0d25(self):
		run(self, "e*nZdZOlLc->n*l", "0.25")

	def test_words_dont_work_as_var_names(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ token recognition error at: (.*)",
			comp,
			"exnOlLc->nxl")

	def test_numbers_dont_work_as_var_names(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ token recognition error at: (.*)",
			comp,
			"e6nOlLc->n6l")

	def test_variables_can_change(self):
		run(self, "e*nZlLc->n*lLe*nOlLc->n*l", "01")

	def test_variables_can_change_in_loop(self):
		run(self, "e?nZlL W j?nOZOZl Wb c->n?l L e?np?nOll L w", "0123456789")


class TestMath(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_print_addition(self):
		run(self, "c->npOnOZll", "3")

	def test_assign_addition(self):
		run(self, "e.npOnOZllLc->n.l", "3")

	def test_print_addition_of_strings(self):
		run(self,
		"c->n p SOZZZZZO n SOZZZZOZl l",
		"AB")

	def test_chain_addition(self):
		run(self, "c->n pOn OZZ n O n Zl l", "6")

	def test_addition_of_floats(self):
		run(self, "c->n p OdO n ZdZOl l", "1.75")

	def test_multiplication(self):
		run(self, "c->n t OZO n OZl l", "10")

	def test_multiplication_of_floats(self):
		run(self, "c->n t OdO n OZdOl l", "3.75")

	def test_chain_multiplication(self):
		run(self, "c->n tOn OO n OZZl l", "12")

	def test_multiplication_between_integer_and_string(self):
		run(self, "c->n tSOZZZZZO n OOl l", "AAA")

	def test_subtraction(self):
		run(self, "c->n m OOO n Ol l", "6")

	def test_subraction_to_negative(self):
		run(self, "c->n m OZ n OZZl l", "-2")

	def test_subtraction_of_floats(self):
		run(self, "c->n m ZdO n OdZOl l", "-0.75")

	def test_chain_subtraction(self):
		run(self, "c->n m OZOZ n OZ n OZOl l", "3")

	def test_division(self):
		run(self, "c->n v OZOZ n OZl l", "5")

	def test_division_to_float(self):
		run(self, "c->n v OO n OOZl l", "0.5")

	def test_division_of_floats(self):
		run(self, "c->n v OdO n ZdOl l", "3")

	def test_mod(self):
		run(self, "c->n u OZZZ n OOl l", "2")

	def test_chain_mod(self):
		run(self, "c->n u OZZZZZZ n OZOZ n OZl l", "0")

	def test_mod_with_floats(self):
		run(self, "c->n u OdZO n ZdOl l", "0.25")

	def test_less_than_true(self):
		run(self, "c->n j O n OOl l", "True")

	def test_less_than_false(self):
		run(self, "c->n j OZO n OOl l", "False")

	def test_less_than_chain_true(self):
		run(self, "c->n j O n OOO n OZZZl l", "True")

	def test_less_than_chain_false(self):
		run(self, "c->n j OO n OZZO n OZZZl l", "False")

	def test_less_than_with_floats(self):
		run(self, "c->n j OdO n OdOOl l", "True")

	def test_greater_than_true(self):
		run(self, "c->n g OOZ n OZl l", "True")

	def test_greater_than_false(self):
		run(self, "c->n g O n OZZl l", "False")

	def test_chain_greater_than_true(self):
		run(self, "c->n g OOOO n  OZOZ n OOO n Zl l", "True")

	def test_chain_greater_than_false(self):
		run(self, "c->n g OOOZ n OOOO n Ol l", "False")

	def test_greater_than_with_floats(self):
		run(self, "c->n g ZdOOZO n ZdOZOOl l", "True")

	def test_equals_true(self):
		run(self, "c->n q OO n OOl l", "True")

	def test_equals_false(self):
		run(self, "c->n q O n Zl l", "False")


class TestAccess(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_access_list_integers(self):
		run(self, "e.nc...nZnOnOZllL c->ni.nOZll", "2")

	def test_access_list_strings(self):
		run(self,
			"""e.nc...n SOZZZZZO n SOZZZZOZ llL
			c->ni.nOll""", "B")

	def test_access_map_integer_to_integer(self):
		run(self, "e.nc:nZnOnOnZllL c->ni.nOll", "0")

	def test_access_map_string_to_integer(self):
		run(self,
			"""e.nc:n SOZZZZZO n O n SOZZZZOO n OZZ llL
			c->ni.nSOZZZZOOl l""", "4")

	def test_access_map_integer_to_string(self):
		run(self,
			"""e.nc:n OZZZ n SOZZZZOO n OO n SOZZZZOZ llL
			c->ni.nOZZZl l""", "C")

	def test_chained_access_list_integers(self):
		run(self,
			"""e-nc...nOOnOOZl lL
			e.nc...nZnOn-nOZl lL
			c->ni.nOZnOl l""", "6")


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
			e*n c...n SOZZZZZO sOZZZZOZ n SOZZZZOOl l L
			c->n * l
			""",
			"[AB,C]")
		# Lack of quotes around strings may or may not be a problem

	def test_map_strings(self):
		run(self,
			"""
			e*n c:n SOZZZZZO sOZZZZOZnSOZZZZOO l l L
			c->n * l
			""",
			"{AB:C}")

	def test_list_append(self):
		run(self,
			"""
			e*n c...n OO n OZ l l L
			ci*n SOOZZZZO sOOZZOZZ sOOZZOZZl n Z l L
			c->n * l
			""",
			"[3,2,0]")


if __name__ == "__main__":
	unittest.main()
