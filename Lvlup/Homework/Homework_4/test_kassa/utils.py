bills = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
bills = sorted(bills, reverse=True)
def kassa(price, payment):
    price = float(price)
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    list_of_cash = [float(i) for i in payment.split()]
    sum_of_cash = sum(list_of_cash)
    list_of_bills = []
    if price > sum_of_cash:
        raise ValueError("Дали недостаточно денег!")
    elif price == sum_of_cash:
        return "Сдача не нужна"
    delivery_to_the_client = sum_of_cash - price
    print('Сдача для покупателя:', "%.2f" % delivery_to_the_client)
    for i in bills:
        difference = int(delivery_to_the_client // i)
        for j in range(difference):
            list_of_bills.append(i)
        delivery_to_the_client = delivery_to_the_client - difference * i
    list_of_bills = (" ".join([str(i) for i in list_of_bills]))
    return list_of_bills

if __name__ == "__main__":
    price = input("Цена товара: ")
    payment = input("Полученные купюры: ")
    print('Купюры для сдачи: ', kassa(price, payment))