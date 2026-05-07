import pytest

from q2_math.sequence import get_value_at_position


@pytest.mark.parametrize(
    ("position", "expected"),
    [
        (1, 11),
        (2, 18),
        (3, 25),
        (200, 1404),
        (254, 1782),
        (3542158, 24795110),
    ],
)
def test_get_value_at_position(position, expected):
    assert get_value_at_position(position) == expected


@pytest.mark.parametrize("invalid_position", [0, -1, -10])
def test_get_value_at_position_should_raise_value_error(invalid_position):
    with pytest.raises(ValueError):
        get_value_at_position(invalid_position)


@pytest.mark.parametrize("invalid_type", [None, 1.5, "10", []])
def test_get_value_at_position_should_raise_type_error(invalid_type):
    with pytest.raises(TypeError):
        get_value_at_position(invalid_type)