
list_of_numbers = [5, 6, 6, 8, 8, 31, 33, 44, 44, 999]
def different_elements(list_of_numebrs, amount = 0):
    for i in range(len(list_of_numebrs)):
        if i == list_of_numbers[0] or list_of_numbers[i] != list_of_numebrs[i-1]:
            amount = amount + 1

    return (amount)

print("Количество различных элементов:", different_elements(list_of_numbers))