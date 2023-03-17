
list_of_numbers = [5, 6, 4, 8, 58, 44, 3, 4, 1]
def neighbours(list_of_numebrs, amount = 0):
    for i in range(len(list_of_numebrs)):
        if i == list_of_numebrs[0] or i == len(list_of_numbers)-1:
            continue
        elif list_of_numebrs[i] > list_of_numebrs[i+1] and list_of_numbers[i] > list_of_numebrs[i-1]:
            amount = amount + 1
        else: continue
    return (amount)

print(neighbours(list_of_numbers))