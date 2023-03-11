def calculater():
    enter_data= input()
    list_of_input = enter_data.split()
    operation = list_of_input[1]
    del list_of_input[1]
    list_of_input = [int(i) for i in list_of_input]
    first_number = list_of_input[0]
    second_number = list_of_input[1]
    if second_number == 0 and operation == "/":
        print("На ноль делить нельзя!")
    elif operation == "+":
          print(first_number + second_number)
    elif operation == "-":
          print(first_number - second_number)
    elif operation == "*":
          print(first_number * second_number)
    elif operation == "/":
          print(first_number / second_number)
calculater()