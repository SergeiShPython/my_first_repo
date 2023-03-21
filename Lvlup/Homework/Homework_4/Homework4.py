from test_kassa.utils import kassa

price = float(input("Цена товара: "))
payment = input("Полученные купюры: ")
print('Купюры для сдачи: ', kassa(price, payment))