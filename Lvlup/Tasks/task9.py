print("Викторина!")
print("Какое животное самое большое?")
answear = input()
points = 0
def check_guess():
    guess = "кит"

    game_continue = True
    number_of_try = 0
    while game_continue == True and number_of_try < 3:
        if answear.lower() == guess.lower():
            points = points + 1
            game_continue = False
        else:
            if number_of_try < 2:
                print("Ответ неверный, попробуйте еще раз!")
                answear = input()
            number_of_try = number_of_try + 1
    if number_of_try == 3:
        print("Вы проиграли, правильный ответ кит ")

check_guess(answear)








