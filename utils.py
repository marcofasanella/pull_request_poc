def convert_to_float(value: str) -> float:
    """
    Convert a value to float, handling None and empty strings.
    """
    if value is None or value == '':
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def concatenate_strings(*args: str) -> str:
    """
    Concatenate multiple strings into one, ignoring None or empty strings.
    """
    return ''.join(arg for arg in args if arg)


def capitalize_first_letter(text: str) -> str:
    """
    Capitalize the first letter of a string, ensuring it handles None and empty input gracefully.
    """
    if not text:
        return ''
    return text[0].upper() + text[1:]
