from datetime import datetime

class Validation:
    @staticmethod  # ✅ No need for 'self'
    def is_valid_date(date_str, date_format="%d-%m-%Y"):
        try:
            if datetime.strptime(date_str, date_format):  # Try parsing
                return True  # Valid date
            else:
                return False
        except ValueError:
            return False  # Invalid date