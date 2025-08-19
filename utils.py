def convert_to_float(value):
    """
    Convert a value to float, handling None and empty strings.
    """
    if value is None or value == '':
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def concatenate_strings(*args):
    """
    Concatenate multiple strings into one, ignoring None or empty strings.
    """
    return ''.join(str(arg) for arg in args if arg not in (None, ''))

def capitalize_first_letter(text):
    """
    Capitalize the first letter of a string.
    """
    if not text:
        return text
    return text[0].upper() + text[1:] if len(text) > 1 else text.upper()