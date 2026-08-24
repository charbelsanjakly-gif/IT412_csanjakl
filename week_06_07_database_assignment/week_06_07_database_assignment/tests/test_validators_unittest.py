"""
test_validators_unittest module

unittest test cases for the validation functions used throughout the
bookstore application.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.validators import (
    validate_title,
    validate_author,
    validate_quantity,
    validate_signed_edition,
    validate_price,
    validate_required_price,
)


class TestValidateTitle(unittest.TestCase):

    def test_normal_title_is_valid(self):
        self.assertTrue(validate_title("The Great Gatsby"))

    def test_title_with_quotes_is_valid(self):
        self.assertTrue(validate_title("Charlotte's \"Web\""))

    def test_empty_title_is_invalid(self):
        self.assertFalse(validate_title(""))

    def test_whitespace_only_title_is_invalid(self):
        self.assertFalse(validate_title("   "))


class TestValidateAuthor(unittest.TestCase):

    def test_normal_author_is_valid(self):
        self.assertTrue(validate_author("J.K. Rowling"))

    def test_author_with_hyphen_and_apostrophe_is_valid(self):
        self.assertTrue(validate_author("Anne-Marie O'Brien"))

    def test_author_with_numbers_is_invalid(self):
        self.assertFalse(validate_author("Author123"))

    def test_empty_author_is_invalid(self):
        self.assertFalse(validate_author(""))


class TestValidateQuantity(unittest.TestCase):

    def test_positive_integer_is_valid(self):
        self.assertTrue(validate_quantity("10"))

    def test_zero_is_valid(self):
        self.assertTrue(validate_quantity("0"))

    def test_decimal_is_invalid(self):
        self.assertFalse(validate_quantity("10.5"))

    def test_letters_are_invalid(self):
        self.assertFalse(validate_quantity("ten"))


class TestValidateSignedEdition(unittest.TestCase):

    def test_y_is_valid(self):
        self.assertTrue(validate_signed_edition("Y"))

    def test_n_is_valid(self):
        self.assertTrue(validate_signed_edition("N"))

    def test_blank_is_valid(self):
        self.assertTrue(validate_signed_edition(""))

    def test_other_letter_is_invalid(self):
        self.assertFalse(validate_signed_edition("X"))


class TestValidatePrice(unittest.TestCase):

    def test_valid_float_string(self):
        self.assertTrue(validate_price("19.99"))

    def test_blank_is_valid_for_optional_price(self):
        self.assertTrue(validate_price(""))

    def test_non_numeric_is_invalid(self):
        self.assertFalse(validate_price("free"))


class TestValidateRequiredPrice(unittest.TestCase):

    def test_valid_float_string(self):
        self.assertTrue(validate_required_price("24.99"))

    def test_blank_is_invalid_for_required_price(self):
        self.assertFalse(validate_required_price(""))

    def test_non_numeric_is_invalid(self):
        self.assertFalse(validate_required_price("abc"))


if __name__ == '__main__':
    unittest.main()
