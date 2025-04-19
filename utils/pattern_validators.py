import re
import phonenumbers


def is_valid_email(email: str) -> bool:
    """
    Validates the email address.
    The validation follows this RFC: https://datatracker.ietf.org/doc/html/rfc5322
    Get the regex from here: https://emailregex.com/
    """
    EMAIL_VALIDATOR_PATTERN = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not isinstance(email, str):
        return False
    return bool(re.match(EMAIL_VALIDATOR_PATTERN, email))


def is_possible_phone_number(phone_number: str) -> bool:
    """
    Validates that it's possible phone number.
    This is not a strict validation.
    This validation is based phonenumbers library. 
    Which is based on the Google's libphonenumber library.
    https://github.com/daviddrysdale/python-phonenumbers
    """
    if not isinstance(phone_number, str) or not phone_number:
        return False
    if not phone_number.startswith("+"):
        phone_number = f"+{phone_number}"

    try:
        phone_object = phonenumbers.parse(number=phone_number)
        if not phonenumbers.is_possible_number(phone_object):
            return False
    except phonenumbers.NumberParseException:
        return False
    return True


def is_valid_url(url: str) -> bool:
    """Validates the URL."""

    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$',
        re.IGNORECASE
    )

    return bool(url_pattern.match(url))
