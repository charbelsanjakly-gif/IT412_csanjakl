"""customer module - Customer class with validation methods.

This module defines the Customer class for the IT 412 Final Project,
providing data validation for all customer fields.
"""

class Customer:
    """Customer class representing a customer record.
    
    Attributes:
        first_name (str): Customer's first name
        last_name (str): Customer's last name
        company_name (str): Customer's company
        address (str): Customer's street address
        city (str): Customer's city
        county (str): Customer's county
        state (str): Customer's state (2-letter code)
        zip_code (str): Customer's zip code
        phone1 (str): Primary phone number
        phone2 (str): Secondary phone number
        email (str): Customer's email address
    """
    
    def __init__(self, first_name, last_name, company_name, address, city, county, state, zip_code, phone1, phone2, email):
        """Initialize a Customer object.
        
        Args:
            first_name (str): Customer's first name
            last_name (str): Customer's last name
            company_name (str): Customer's company name
            address (str): Customer's street address
            city (str): Customer's city
            county (str): Customer's county
            state (str): Customer's state (2-letter code)
            zip_code (str): Customer's zip code
            phone1 (str): Primary phone number
            phone2 (str): Secondary phone number
            email (str): Customer's email address
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
        """Validate a name field (first or last name).
        
        Valid characters: letters, spaces, apostrophes, and hyphens.
        
        Args:
            name (str): The name to validate
            
        Returns:
            bool: True if name is valid, False otherwise
        """
        if not name or len(name) == 0:
            return False
        for char in name:
            if not (char.isalpha() or char in " '-"):
                return False
        return True
    
    def is_valid_phone(self, phone):
        """Validate a phone number.
        
        Valid formats: 10 digits (1234567890) or 12 characters with dashes/periods (123-456-7890 or 123.456.7890).
        
        Args:
            phone (str): The phone number to validate
            
        Returns:
            bool: True if phone is valid, False otherwise
        """
        if not phone:
            return False
        digits = ''.join(c for c in phone if c.isdigit())
        if len(digits) == 10:
            return True
        if len(phone) == 12 and (phone.count('-') == 2 or phone.count('.') == 2):
            return len(digits) == 10
        return False
    
    def is_valid_email(self, email):
        """Validate an email address.
        
        Valid characters: alphanumeric, dots, hyphens, underscores, and @ symbol.
        Must contain exactly one @ symbol and at least one dot after it.
        
        Args:
            email (str): The email to validate
            
        Returns:
            bool: True if email is valid, False otherwise
        """
        if not email or '@' not in email:
            return False
        if email.count('@') != 1:
            return False
        local, domain = email.split('@')
        if not local or not domain or '.' not in domain:
            return False
        valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_@+')
        return all(c in valid_chars for c in email)
    
    def is_valid_state(self, state):
        """Validate a US state code.
        
        Valid state codes are 2-letter uppercase codes (e.g., MI, CA, NY).
        
        Args:
            state (str): The state code to validate
            
        Returns:
            bool: True if state code is valid, False otherwise
        """
        valid_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        return state in valid_states
    
    def is_valid_zip(self, zip_code):
        """Validate a zip code.
        
        Valid formats: 4 or 5 digits (9876 or 48201).
        
        Args:
            zip_code (str): The zip code to validate
            
        Returns:
            bool: True if zip code is valid, False otherwise
        """
        if not zip_code:
            return False
        if not zip_code.isdigit():
            return False
        return len(zip_code) in [4, 5]
    
    def __str__(self):
        """Return string representation of customer.
        
        Returns:
            str: Formatted customer information
        """
        return f"{self.first_name} {self.last_name} - {self.email}"
    
    def __repr__(self):
        """Return detailed string representation of customer.
        
        Returns:
            str: Detailed customer information
        """
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.company_name}', '{self.address}', '{self.city}', '{self.county}', '{self.state}', '{self.zip_code}', '{self.phone1}', '{self.phone2}', '{self.email}')"
