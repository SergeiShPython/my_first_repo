def calculator(string):
    enter_data= string
    string_del_space=enter_data.replace(" ", "", -1)
    for j in string_del_space:
        if j == '+':
            list_of_input = string_del_space.split("+")
            operation = "+"
        elif j == '-':
            list_of_input = string_del_space.split("-")
            operation = "-"
        elif j == '*':
            list_of_input = string_del_space.split("*")
            operation = "*"
        elif j == '/':
            list_of_input = string_del_space.split("/")
            operation = "/"
    list_of_input = [int(_) for _ in list_of_input]
    #print(list_of_input)
    #print(operation)
    first_number = list_of_input[0]
    second_number = list_of_input[1]
    if second_number == 0 and operation == "/":
        return "На ноль делить нельзя!"
    elif operation == "+":
          return first_number + second_number
    elif operation == "-":
          return first_number - second_number
    elif operation == "*":
          return first_number * second_number
    elif operation == "/":
         return first_number / second_number
#calculator(operations)
