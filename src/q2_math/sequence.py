def get_value_at_position(pos: int) -> int:
    """
    Retorna o valor correspondente à posição informada
    na sequência aritmética: 11, 18, 25, 32...

    A sequência inicia na posição 1.
    """

    if not isinstance(pos, int):
        raise TypeError("pos must be an integer")

    if pos < 1:
        raise ValueError("pos must be greater than or equal to 1")

    FIRST_TERM = 11
    COMMON_DIFFERENCE = 7

    return FIRST_TERM + (pos - 1) * COMMON_DIFFERENCE