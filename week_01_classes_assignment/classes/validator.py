# Validator class and the character rules it uses.

# characters not allowed in a name
name_bad = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+',
            ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']

# characters not allowed in an email
email_bad = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')', '=', '+',
             ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']


class Validator:
    """Validates names, emails, and ID numbers entered by the user."""

    def checkName(self, value):
        """Return True if the name is non-empty and has no forbidden characters."""
        if value == "":
            return False
        for c in value:
            if c in name_bad:
                return False
        return True

    def checkEmail(self, value):
        """Return True if the email is non-empty and has no forbidden characters."""
        if value == "":
            return False
        for c in value:
            if c in email_bad:
                return False
        return True

    def checkStudentID(self, value):
        """Return True if the value is all digits and 7 digits or less."""
        return value.isdigit() and len(value) <= 7

    def checkInstructorID(self, value):
        """Return True if the value is all digits and 5 digits or less."""
        return value.isdigit() and len(value) <= 5

    def checkRequired(self, value):
        """Return True if the value is not blank."""
        return value.strip() != ""
