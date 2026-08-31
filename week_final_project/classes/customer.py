"""
customer module

Contains the Customer class which represents a single customer record
with validation for all fields.
"""

import re


class Customer:
    """
    Represents a customer record with validated fields.

    A customer contains first name, last name, company, address, city,
    county, state, zip, phone numbers, and email.
    """

    def __init__(self, first_name, last_name, company_name, address,
                 city, county, state, zip_code, phone1, phone2, email):
        """
        Initialize a Customer with provided data.

        Args:
            first_name -- customer first name
            last_name -- customer last name
            company_name -- customer company name
            address -- street address
            city -- city name
            county -- county name
            state -- two-letter state abbreviation
            zip_code -- zip or postal code
            phone1 -- primary phone number
            phone2 -- secondary phone number
            email -- email address
        """
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.county = county
        self.state = state
        self.zip_code = zip_code
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email

    def is_valid_name(self, name):
        """
        Validate that a name contains only letters, spaces, apostrophes, and dashes.

        Args:
            name -- the name string to validate

        Returns:
            True if valid, False otherwise
        """
        pattern = r"^[a-zA-Z' -]+$"
        return bool(re.match(pattern, name))

    def is_valid_phone(self, phone):
        """
        Validate phone number format.

        Phone must be either 10 digits or 12 characters (with dashes/periods).

        Args:
            phone -- the phone number string to validate

        Returns:
            True if valid, False otherwise
        """
        if not phone:
            return True
        if len(phone) == 10 and phone.isdigit():
            return True
        if len(phone) == 12:
            pattern = r"^[0-9.\-]+$"
            return bool(re.match(pattern, phone))
        return False

    def is_valid_email(self, email):
        """
        Validate email address format.

        Args:
            email -- the email string to validate

        Returns:
            True if valid, False otherwise
        """
        if not email:
            return True
        pattern = r"^[a-zA-Z0-9._+@-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def is_valid_state(self, state):
        """
        Validate that state is a valid US state abbreviation.

        Args:
            state -- the state abbreviation to validate

        Returns:
            True if valid, False otherwise
        """
        valid_states = [
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
        ]
        return state.upper() in valid_states

    def is_valid_zip(self, zip_code):
        """
        Validate that zip code is 4-5 digits.

        Args:
            zip_code -- the zip code to validate

        Returns:
            True if valid, False otherwise
        """
        if not zip_code:
            return True
        return len(zip_code) in [4, 5] and zip_code.isdigit()

    def __str__(self):
        """Return a formatted string representation of the customer."""
        return (f"{self.first_name} {self.last_name} | "
                f"{self.company_name} | {self.city}, {self.state}")

    def __repr__(self):
        """Return a detailed representation of the customer."""
        return (f"Customer('{self.first_name}', '{self.last_name}', "
                f"'{self.company_name}', '{self.email}')")
