import re


class ValidateForm:

    @staticmethod
    def validate_number(phone: str):
        if re.fullmatch(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", phone):
            return "phone", phone
        raise ValueError("Неправильно указан номер")

    @staticmethod
    def validate_email(email: str):
        if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return "email", email
        raise ValueError("Неправильно указан email")

    @staticmethod
    def validate_date(date: str):
        if re.fullmatch(r"(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})", date):
            return "date", date
        raise ValueError("Неправильно указана дата")


    def main_validator(self, incoming_data: dict):
        validated_types = {}
        for key, value in incoming_data.items():
            try:
                type, valid_value = self.validate_number(value)
            except ValueError:
                try:
                    type, valid_value = self.validate_email(value)
                except ValueError:
                    try:
                        type, valid_value = self.validate_date(value)
                    except ValueError:
                        type, valid_value = "text", value
            validated_types[key] = {'type': type, 'incoming_value': valid_value}
        return validated_types
