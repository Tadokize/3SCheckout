import pytest

from q3_game.engine import GameAnalysis, solve_board_game


def test_solve_board_game_with_3_houses():
    result = solve_board_game(3)

    assert result == GameAnalysis(
        minimum_turns=1,
        optimal_path_probability=1 / 3,
        possible_combinations=2,
    )

def test_solve_board_game_with_4_houses():
    result = solve_board_game(4)

    assert result == GameAnalysis(
        minimum_turns=1,
        optimal_path_probability=1 / 3,
        possible_combinations=4,
    )


def test_solve_board_game_with_5_houses():
    result = solve_board_game(5)

    assert result.minimum_turns == 2
    assert result.optimal_path_probability == pytest.approx(1 / 3)
    assert result.possible_combinations == 7


@pytest.mark.parametrize("invalid_value", [0, 1, 2, -1])
def test_solve_board_game_should_raise_value_error(invalid_value):
    with pytest.raises(ValueError):
        solve_board_game(invalid_value)


@pytest.mark.parametrize("invalid_type", [None, 1.5, "5", []])
def test_solve_board_game_should_raise_type_error(invalid_type):
    with pytest.raises(TypeError):
        solve_board_game(invalid_type)


