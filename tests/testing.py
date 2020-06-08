#!/mnt/c/Users/RedKnite/Appdata/local/programs/Python/Python38/python.exe

"""Tests for the Switch programming language"""

import sys
import unittest
from io import StringIO
from subprocess import run as run_pro

from Switch.Sw import *
from Switch.switch_builtins import *
from Switch.errors import *

old_stdout = sys.stdout
old_stderr = sys.stderr


def run(tester, source_code, output, file=False):
	"""Test that the source_code produces the desired output"""

	if file:
		from pathlib import Path
		source_code = Path(__file__).parent.absolute() / source_code
	code = comp(source_code, file=file)
	exec(code, {})
	tester.assertEqual(sys.stdout.getvalue(), output)


class TestPrimitivePrinting(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_print_one(self):
		run(self, "c->nOl", "1")

	def test_print_four(self):
		run(self, "c->nOZZl", "4")

	def test_print_thirteen(self):
		run(self, "c->nOOZOl", "13")

	def test_lowercase_numbers(self):
		run(self, "c->noozol", "13")

	def test_mixedcase_numbers(self):
		run(self, "c->noOZozl", "26")

	def test_numbers_with_spaces(self):
		run(self, "c->no  OZ \n o	z\tl", "26")

	def test_print_A(self):
		run(self, "c->nSOZZZZZOl", "A")

	def test_print_A_lowercase_numbers(self):
		run(self, "c->nSozzzzzol", "A")

	def test_print_A_mixedcase_numbers(self):
		run(self, "c->nSoZZzzzOl", "A")

	def test_print_A_lowercase_s_fails(self):
		self.assertRaises(
			SwitchError,
			comp,
			"c->nsoZZzzzOl")

	def test_print_Hello(self):
		run(
			self,
			"c->nSOZZOZZZsOOZZOZOsOOZOOZZsOOZOOZZsOOZOOOOl",
			"Hello"
		)

	def test_print_Hello_uppercase_s_fails(self):
		self.assertRaisesRegex(
			SwitchError,
			"line [0-9]+:[0-9]+ no viable alternative at input (.*)",
			comp,
			"c->nSOZZOZZZSOOZZOZOSOOZOOZZSOOZOOZZSOOZOOOOl")

	def test_print_Hello_spaces(self):
		run(
			self,
			"c->nSOZZOZZZ sOOZZOZO sOOZOOZZ sOOZOOZZ sOOZOOOOl",
			"Hello"
		)

	def test_print_float_1d0(self):
		run(self, "c->nOdZl", "1")

	def test_print_float_0d25(self):
		run(self, "c->nZdZOl", "0.25")

	def test_print_float_0d75(self):
		run(self, "c->nZdOOl", "0.75")

	def test_print_nothing(self):
		run(self, "c->l", "")


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
		run(self, "e?nZlL W j?nOZOZl B c->n?l L e?np?nOll L w", "0123456789")

	def test_assignment_to_access(self):
		run(self,
			"""e*n c...n OZ n OZZ n OZZZl lL
			e i*nZl n OO lL
			c->n*l""",
			"[3,4,8]")


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

	def test_multiplication_between_whole_float_and_string(self):
		run(self, "c->n tSOZZZZZO n OOdZl l", "AAA")

	def test_multiplication_between_integer_and_function_raise_TypeError(self):
		code = comp("tOOn:l")
		self.assertRaises(TypeError,
			exec,
			code)

	def test_multiplication_between_float_and_function_raise_TypeError(self):
		code = comp("tOdOn:l")
		self.assertRaises(TypeError,
			exec,
			code)

	def test_multiplication_between_float_and_function_raise_TypeError_rmul(self):
		code = comp("t:nOdOl")
		self.assertRaises(TypeError,
			exec,
			code)

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
		run(self, "W Z B c->nOlL w", "")

	def test_normal_while_loop(self):
		run(self, "e!n OOO lL W g!nZl B c->n e!n m!nOl ll L w", "6543210")

	def test_nested_while_loop(self):
		run(self,
			"""e!n OO l L
			W!B
			e*n OZZ l L
			W*B c->n p*n!l lL  e*n m*nOl lL w
			e!n m!nOl lL w
			""",
			"765465435432")


class TestListAndMap(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_list(self):
		run(self, "c->n c...n O n OZ n OO n OZZl l", "[1,2,3,4]")

	def test_list_floats(self):
		run(self, "c->n c...n OdO n OZdZZO n OOdZ n OZZl l", "[1.5,2.125,3,4]")

	def test_map(self):
		run(self, "c->n c:n OnO n OZnOOl l", "{1:1,2:3}")

	def test_list_strings(self):
		run(self,
			"""
			e*n c...n SOZZZZZO sOZZZZOZ n SOZZZZOOl l L
			c->n * l
			""",
			# Lack of quotes around strings may or may not be a problem
			"['AB','C']")

	def test_list_string_num(self):
		run(self,
			"""
			e*n c...n SOOZZOZ sOOZZZZ n SOOZOZZl l L
			c->n * l L
			""",
			"['20','4']")

	def test_map_strings(self):
		run(self,
			"""
			e*n c:n SOZZZZZO sOZZZZOZnSOZZZZOO l l L
			c->n * l
			""",
			"{'AB':'C'}")

	def test_list_append(self):
		run(self,
			"""
			e*n c...n OO n OZ l l L
			ci*n SOOZZZZO sOOZZOZZ sOOZZOZZl n Z l L
			c->n * l
			""",
			"[3,2,0]")

	def test_list_len(self):
		run(self,
			"""c->n
				i
				c...n O n OZ n OO n OZZl
				n  SOOZOOZZ sOOZZOZO sOOZOOOZ l l""",
			"4")

	def test_map_odd_num_elements_raises_error(self):
		code = comp("e*n c:n OnZ n OO ll")
		self.assertRaisesRegex(
			ValueError,
			"Must have an even number of items",
			exec,
			code)

	def test_list_containing_itself_prints(self):
		run(self,
			"""
			e*n c...l lL
			c i*n SOOZZZZO sOOZZOZZ sOOZZOZZl n *l L
			c->n*l
			""",
			"[[...]]")

	def test_map_containing_itself_prints(self):
		run(self,
			"""
			e*n c:l lL
			e i*nOl n * lL
			c->n*l
			""",
			"{1:{...}}")

	def test_list_2cycle_recursion(self):
		run(self,
			"""
			e*n c...nOl lL
			e&n c...nZl lL
			c i*n SOOZZZZO sOOZZOZZ sOOZZOZZl n &l L
			c i&n SOOZZZZO sOOZZOZZ sOOZZOZZl n *l L
			c->n*l
			""",
			"[1,[0,[...]]]")

	def test_map_2cycle_recursion(self):
		run(self,
			"""
			e*n c:nOnOOl lL
			e&n c:nZnOl lL
			e i*n OZZ l n &l L
			e i&n OZZZ l n *l L
			c->n*l
			""",
			"{1:3,4:{0:1,8:{...}}}")


class TestFunctionDefinition(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_func_def(self):
		run(self,
			"F B c->n.l L f L",
			"")

	def test_func(self):
		run(self,
			"c F B c->nZl Lf l",
			"0")

	def test_args(self):
		run(self,
			"c F . n * B c->n p.n* l l L f n O n OZ l",
			"3")

	def test_two_funcs(self):
		run(self,
			"""
			e& n F B c->n SOZZZZZO l L f l L
			e# n F @ B c->n @ l L f l L
			c&l L
			c#nOl L
			""",
			"A1")

	def test_nested(self):
		run(self,
			"""
			c F B c F . B c->n . l L f n OZZ l L f l
			""",
			"4")


class TestFile(unittest.TestCase):
	def setUp(self):
		sys.stdout = StringIO()

	def tearDown(self):
		sys.stdout = old_stdout

	def test_test_file(self):
		run(self, "test.sw", "{1:3}0123456789 20", file=True)

	def test_hello_world_file(self):
		run(self, "hello_world.sw", "Hello World", file=True)


class TestObjectsDirectly(unittest.TestCase):
	def test_SwitchFrac_is_integer_true(self):
		self.assertTrue(SwitchFrac(5).is_integer())

	def test_SwitchFrac_is_integer_true_float(self):
		self.assertTrue(SwitchFrac(5.0).is_integer())

	def test_SwitchFrac_is_integer_false(self):
		self.assertFalse(SwitchFrac(5.5).is_integer())

	def test_SwitchFrac_string_by_float_mul(self):
		self.assertRaises(
			TypeError,
			lambda a, b: a * b,
			SwitchFrac(1.1),
			"hi"
		)

	def test_SwitchFrac_string_by_float_rmul(self):
		self.assertRaises(
			TypeError,
			lambda a, b: a * b,
			"hi",
			SwitchFrac(1.1)
		)

	def test_SwitchFrac_add_float(self):
		self.assertEqual(
			SwitchFrac(1.1).limit_denominator() + .4,
			SwitchFrac(1.5).limit_denominator()
		)

	def test_SwitchFrac_equality_with_floats(self):
		self.assertEqual(SwitchFrac(1.1), 1.1)

	def test_SwitchFrac_equality_with_ints_given_float(self):
		self.assertEqual(SwitchFrac(6.0), 6)

	def test_equal_true(self):
		self.assertTrue(equal(1, 1, 2-1))

	def test_equal_false(self):
		self.assertFalse(equal(4, 5, 2+2))

	def test_less_than_true(self):
		self.assertTrue(less_than(3, 4, 5.5, 5.51))

	def test_less_than_false(self):
		self.assertFalse(less_than(6, 4, 5.5, 5.51))

	def test_less_than_equal_is_not_less(self):
		self.assertFalse(less_than(4, 4, 5.5, 5.51))

	def test_greater_than_true(self):
		self.assertTrue(greater_than(4, 3, 1.1, 1.0))

	def test_greater_than_false(self):
		self.assertFalse(greater_than(4, 4.4, 1.1, 1.0))

	def test_mod(self):
		self.assertEqual(mod(10, 3), 1)

	def test_mod_chain(self):
		self.assertEqual(mod(30, 11, 3), 2)

	def test_truediv(self):
		self.assertEqual(truediv(30, 3), 10.0)

	def test_truediv_decimal(self):
		self.assertEqual(truediv(7, 2), 3.5)

	def test_truediv_type(self):
		self.assertTrue(isinstance(truediv(30, 10), float))

	def test_truediv_chain(self):
		self.assertEqual(truediv(30, 3, 5), 2)

	def test_mul(self):
		self.assertEqual(mul(4, 3), 12)

	def test_mul_decimal(self):
		self.assertEqual(mul(4, 3.5), 14)

	def test_mul_chain(self):
		self.assertEqual(mul(4, 3, .5), 6)

	def test_mul_string(self):
		self.assertEqual(mul(4, "*"), "****")

	def test_sub(self):
		self.assertEqual(sub(2, 1), 1)

	def test_sub_chain(self):
		self.assertEqual(sub(2, 1, 5), -4)

	def test_add(self):
		self.assertEqual(add(4, 3), 7)

	def test_add_chain(self):
		self.assertEqual(add(4, 3, -1), 6)

	def test_add_string(self):
		self.assertEqual(add("yo", " boi"), "yo boi")

	def test_add_string_chain(self):
		self.assertEqual(add("yo", " boi", "!"), "yo boi!")

	def test_print_no_nl(self):
		sys.stdout = StringIO()
		print_no_nl("Hi", "World")
		self.assertEqual(sys.stdout.getvalue(), "Hi World")
		sys.stdout = old_stdout

	def test_Namespace(self):
		n = Namespace()
		self.assertEqual(n.walrus("x", 5), 5)
		self.assertEqual(n["x"], 5)

	def test_SwitchList(self):
		l = SwitchList("hi", "bye")
		self.assertEqual(l[0], "hi")
		self.assertEqual(l[1], "bye")

	def test_SwitchList_str(self):
		l = SwitchList("hi", "bye")
		self.assertEqual(str(l), "['hi','bye']")

	def test_SwitchList_append(self):
		l = SwitchList("hi", "bye")
		l._append("die")
		self.assertEqual(l[0], "hi")
		self.assertEqual(l[1], "bye")
		self.assertEqual(l[2], "die")

	def test_SwitchList_append_index(self):
		l = SwitchList("hi", "bye")
		l["add"]("die")
		self.assertEqual(l[0], "hi")
		self.assertEqual(l[1], "bye")
		self.assertEqual(l[2], "die")

	def test_SwitchList_empty(self):
		l = SwitchList()
		self.assertEqual(str(l), "[]")

	def test_SwitchList_len(self):
		l = SwitchList("hi", "bye")
		self.assertEqual(l["len"], 2)

	def test_SwitchList_pop(self):
		l = SwitchList("hi", "bye")
		self.assertEqual(l["pop"](), "bye")
		self.assertEqual(str(l), "['hi']")

	def test_SwitchList_KeyError(self):
		l = SwitchList("hi", "bye")
		self.assertRaises(KeyError, l.__getitem__, 2)

	def test_SwitchList_walrus(self):
		l = SwitchList("hi", "bye")
		self.assertEqual(l.walrus(1, "die"), "die")
		self.assertEqual(str(l), "['hi','die']")

	def test_SwitchList_walrus_after_end_KeyError(self):
		l = SwitchList("hi", "bye")
		self.assertRaises(KeyError, l.walrus, 2, "die")

	def test_SwitchMap(self):
		m = SwitchMap("me", "max", "you", "Switch")
		self.assertEqual(m["me"], "max")
		self.assertEqual(m["you"], "Switch")

	def test_SwitchMap_str(self):
		m = SwitchMap("me", "max", "you", "Switch")
		self.assertEqual(str(m), "{'me':'max','you':'Switch'}")

	def test_SwitchMap_walrus(self):
		m = SwitchMap("me", "max", "you", "Switch")
		self.assertEqual(m.walrus("him", "Jeff"), "Jeff")
		self.assertEqual(str(m), "{'me':'max','you':'Switch','him':'Jeff'}")

	def test_SwitchMap_raises_on_odd(self):
		self.assertRaises(ValueError, SwitchMap, "key", "arg", "key2")


class TestCLI(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		global Path
		from pathlib import Path

	def test_main(self):
		out = run_pro("python -m Switch.switch c->nOl", capture_output=True, encoding="utf-8")
		self.assertEqual(out.returncode, 0)
		self.assertTrue(out.stdout.startswith("Output:\n"))

	def test_main_f(self):
		file = Path(__file__).parent.absolute() / "hello_world.sw"
		out = run_pro(
			f"python -m Switch.switch -f {file}",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertTrue(out.stdout.startswith("Output:\n"))

	def test_main_m(self):
		out = run_pro(
			"python -m Switch.switch c->nOl -m",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertEqual(out.stdout, "1")

	def test_main_m_f(self):
		file = Path(__file__).parent.absolute() / "hello_world.sw"
		out = run_pro(
			f"python -m Switch.switch -f {file} -m",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertEqual(out.stdout, "Hello World")

	def test_main_c(self):
		out = run_pro(
			"python -m Switch.switch c->nOl -c",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertTrue(out.stdout.startswith("from Switch.switch_builtins import *"))

	def test_main_c_f(self):
		file = Path(__file__).parent.absolute() / "hello_world.sw"
		out = run_pro(
			f"python -m Switch.switch -f {file} -c",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertTrue(out.stdout.startswith("from Switch.switch_builtins import *"))

	def test_main_m_overrides_c(self):
		out = run_pro(
			"python -m Switch.switch c->nOl -c -m",
			capture_output=True,
			encoding="utf-8"
		)
		self.assertEqual(out.returncode, 0)
		self.assertEqual(out.stdout, "1")


if __name__ == "__main__":
	unittest.main()
