from dataclasses import dataclass
from functools import lru_cache
from math import ceil
from fractions import Fraction


@dataclass(frozen=True)
class GameAnalysis:
    minimum_turns: int
    optimal_path_probability: float
    possible_combinations: int


def solve_board_game(houses: int) -> GameAnalysis:
    """
    Analisa o tabuleiro e retorna métricas do jogo.
    """

    if not isinstance(houses, int):
        raise TypeError("houses must be an integer")

    if houses < 3:
        raise ValueError("houses must be greater than or equal to 3")

    target = houses - 1

    minimum_turns = ceil(target / 3)

    optimal_paths = _count_optimal_paths(target, minimum_turns)

    total_possible_paths = 3 ** minimum_turns

    probability = optimal_paths / total_possible_paths

    combinations = _count_valid_combinations(target)

    return GameAnalysis(
        minimum_turns=minimum_turns,
        optimal_path_probability=probability,
        possible_combinations=combinations,
    )


def _count_optimal_paths(target: int, turns: int) -> int:
    """
    Conta quantos caminhos atingem o destino
    usando exatamente o número mínimo de turnos.
    """

    @lru_cache(maxsize=None)
    def dp(remaining: int, remaining_turns: int) -> int:
        if remaining_turns == 0:
            return 1 if remaining == 0 else 0

        if remaining < 0:
            return 0

        return sum(
            dp(remaining - step, remaining_turns - 1)
            for step in (1, 2, 3)
        )

    return dp(target, turns)


def _count_valid_combinations(target: int) -> int:
    """
    Conta combinações válidas sem looping.
    """

    @lru_cache(maxsize=None)
    def dp(position: int) -> int:
        if position == target:
            return 1

        if position > target:
            return 0

        return sum(dp(position + step) for step in (1, 2, 3))

    return dp(0)