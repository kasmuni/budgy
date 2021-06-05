from src import expense
import pytest

EXPENSE_NAME = "Tim Hortons"
EXPENSE_CATEGORY = "Food"


@pytest.fixture
def tims():
    tims = expense.Expense("Tim Hortons", "Food")
    return tims


def test_expense_checkinitalbalance(tims):
    initialbalance = 0
    assert initialbalance == tims.get_expense_balance()


def test_expense_event_1(tims):
    tims.expense_event(500)
    currentexpectedbalance = 500
    assert currentexpectedbalance == tims.get_expense_balance()


def test_expense_event_2(tims):
    tims.expense_event(600)
    tims.expense_event(250)
    currentexpectedbalance = 850
    assert currentexpectedbalance == tims.get_expense_balance()


def test_get_expense_name(tims):
    assert tims.name == EXPENSE_NAME


def test_get_expense_category(tims):
    assert tims.category == EXPENSE_CATEGORY
