from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TerminationBenefits:
    vacation_amount: float
    thirteenth_salary_amount: float
    total_amount: float


def calculate_termination_benefits(
    salary: float,
    admission_date: date,
    resignation_date: date,
) -> TerminationBenefits:
    """
    Calcula os valores proporcionais de férias e décimo terceiro
    no pedido de demissão.
    """

    if salary <= 0:
        raise ValueError("salary must be greater than zero")

    if resignation_date < admission_date:
        raise ValueError(
            "resignation_date cannot be earlier than admission_date"
        )

    vacation_months = _calculate_vacation_months(
        admission_date,
        resignation_date,
    )

    thirteenth_salary_months = resignation_date.month

    vacation_amount = (salary / 12) * vacation_months

    thirteenth_salary_amount = (
        (salary / 12) * thirteenth_salary_months
    )

    total_amount = (
        vacation_amount +
        thirteenth_salary_amount
    )

    return TerminationBenefits(
        vacation_amount=round(vacation_amount, 2),
        thirteenth_salary_amount=round(
            thirteenth_salary_amount,
            2,
        ),
        total_amount=round(total_amount, 2),
    )


def _calculate_vacation_months(
    admission_date: date,
    resignation_date: date,
) -> int:
    """
    Calcula quantos meses se passaram desde
    o último aniversário de empresa.
    """

    months = (
        (resignation_date.year - admission_date.year) * 12
        + resignation_date.month
        - admission_date.month
    )

    return months % 12