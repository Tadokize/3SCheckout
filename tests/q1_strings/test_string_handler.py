import pytest

from q1_strings.string_handler import check_string_bounds


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("BANANA", True),
        ("BOLA", True),
        ("CASA", False),
        ("banana", False),
        ("BA", True),
        ("B", False),
        ("A", False),
        ("", False),
    ],
)
def test_check_string_bounds(text, expected):
    assert check_string_bounds(text) is expected


def test_check_string_bounds_should_raise_type_error():
    with pytest.raises(TypeError):
        check_string_bounds(None)