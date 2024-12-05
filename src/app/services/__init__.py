import copy
import datetime
import re

from app.db import db
from app.schema.template import Template


def find_matching_template(fields: dict[str, str]) -> Template | None:
    for template in list(db["templates"].find()):
        compare = copy.copy(template)
        compare.update(fields)
        if template == compare:
            return Template(
                id=str(template.pop("_id")),
                name=template.pop("name"),
                fields=template
            )
    return None


def is_valid_date(date_str: str) -> bool:
    formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for fmt in formats:
        try:
            datetime.datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            pass
    return False


def is_valid_phone(phone_str: str) -> bool:
    pattern = r'^[\+\s]7 \d{3} \d{3} \d{2} \d{2}$'
    return bool(re.match(pattern, phone_str))


def is_valid_email(email_str: str) -> bool:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email_str))


def determine_field_type(value: str) -> str:
    if is_valid_date(value):
        return "date"
    if is_valid_phone(value):
        return "phone"
    if is_valid_email(value):
        return "email"
    return "text"
