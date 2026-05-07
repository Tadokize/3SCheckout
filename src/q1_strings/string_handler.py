def check_string_bounds(text: str) -> bool:
    """
    Verifica se a string começa com 'B' e termina com 'A'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return False

    return text.startswith("B") and text.endswith("A")