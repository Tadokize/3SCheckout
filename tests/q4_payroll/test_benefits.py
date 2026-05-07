from datetime import date

import pytest

from q4_payroll.benefits import (
    TerminationBenefits,
    calculate_termination_benefits,
)


def test_calculate_termination_benefits():
    result = calculate_termination_benefits(
        salary=6000,
        admission_date=date(2020, 5, 10),
        resignation_date=date(2024, 11, 15),
    )

    assert result == TerminationBenefits(
        vacation_amount=3000.0,
        thirteenth_salary_amount=5500.0,
        total_amount=8500.0,
    )


def test_calculate_termination_benefits_same_year():
    result = calculate_termination_benefits(
        salary=3000,
        admission_date=date(2024, 1, 10),
        resignation_date=date(2024, 4, 20),
    )

    assert result.vacation_amount == 750.0
    assert result.thirteenth_salary_amount == 1000.0
    assert result.total_amount == 1750.0


@pytest.mark.parametrize("invalid_salary", [0, -1000])
def test_should_raise_value_error_for_invalid_salary(
    invalid_salary,
):
    with pytest.raises(ValueError):
        calculate_termination_benefits(
            salary=invalid_salary,
            admission_date=date(2020, 1, 1),
            resignation_date=date(2024, 1, 1),
        )


def test_should_raise_value_error_for_invalid_dates():
    with pytest.raises(ValueError):
        calculate_termination_benefits(
            salary=5000,
            admission_date=date(2024, 5, 1),
            resignation_date=date(2023, 5, 1),
        )