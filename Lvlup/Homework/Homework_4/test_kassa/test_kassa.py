import pytest
from Homework.Homework_4.test_kassa.utils import kassa

def test_kassa():
    price = "9800"
    payment = "5000 5000"
    result = kassa(price, payment)
    assert result == "100 100"
def test_kassa_sale_penny():
    price = "4586.48"
    payment = "5000"
    result = kassa(price, payment)
    assert result == "100 100 100 100 10 2 1 0.5 0.01 0.01"
def test_kassa_no_money_to_return():
    price = "1000"
    payment = "1000"
    result = kassa(price, payment)
    assert result == "Сдача не нужна"
def test_kassa_minus():
    price = "-5000"
    payment = "5000"
    with pytest.raises(ValueError):
        kassa(price, payment)
def test_kassa_error():
    price = "10000"
    payment = "5000"
    with pytest.raises(ValueError):
        kassa(price, payment)
