import re
from datetime import datetime


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
        date_formats = ["%Y-%m-%d",
                        "%d.%m.%Y"]
        result = []
        for i in date_formats:
            try:
                if datetime.strptime(date, i):
                    result.append(True)
            except:
                result.append(False)
        if any(result):
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
