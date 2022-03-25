import sys
import pytest
from pathlib import Path

file = Path( __file__ ). resolve()
package_root_directory = file.parents [1]
sys.path.append(str(package_root_directory))

from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
        (2.5,2.5, 5.0),
        (5 , 5 , 10),
        (12, 4, 16)
])
def test_add(num1 , num2 , expected):
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(5,3) == 15

def test_divide():
    assert divide(15,3) == 5

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50.0

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0.0

def test_bank_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30.0

def test_bank_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70.0

def test_bank_collect_intrest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55.0

@pytest.mark.parametrize("deposited, withdrew, expected", [
        (200, 100, 100),
        (50, 10, 40),
        (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_bank_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
