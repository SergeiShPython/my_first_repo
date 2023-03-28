
input_login = input()
#input_password = input()

class Users():
    def __init__(self):
        data_base = ["Pasha", "Sergey", 'Admin']
        self.y = data_base
    def login(self, input_login):
        if input_login in self.y:
            return "ок"
        else:  return "user not found"

    def register(self):
        if input_login in self.y:
            return 'invalid username'
        else: self.y.append(input_login) and print('ok')

    def all_users(self):
        if input_login == 'admin':

            print(self.y)
        else: print('acces_denied')

Users.all_users(input_login)
Users.login(input_login)
