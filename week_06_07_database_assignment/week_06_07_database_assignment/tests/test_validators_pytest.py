"""
test_validators_pytest module

Pytest test cases for the validation functions used throughout the
bookstore application.
"""

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


def test_normal_title_is_valid():
    assert validate_title("Moby Dick") is True


def test_empty_title_is_invalid():
    assert validate_title("") is False


def test_normal_author_is_valid():
    assert validate_author("Mark Twain") is True


def test_author_with_numbers_is_invalid():
    assert validate_author("Author2") is False


def test_positive_integer_quantity_is_valid():
    assert validate_quantity("42") is True


def test_negative_number_string_quantity_is_valid_format():
    # Format-wise "-5" is a valid integer string; business logic
    # elsewhere prevents negative inventory.
    assert validate_quantity("-5") is True


def test_decimal_quantity_is_invalid():
    assert validate_quantity("3.14") is False


def test_signed_edition_y_valid():
    assert validate_signed_edition("Y") is True


def test_signed_edition_lowercase_y_valid():
    assert validate_signed_edition("y") is True


def test_signed_edition_invalid_value():
    assert validate_signed_edition("Maybe") is False


def test_price_blank_is_valid():
    assert validate_price("") is True


def test_price_valid_float():
    assert validate_price("9.99") is True


def test_price_invalid_text():
    assert validate_price("nine dollars") is False


def test_required_price_blank_invalid():
    assert validate_required_price("") is False


def test_required_price_valid_float():
    assert validate_required_price("14.50") is True
