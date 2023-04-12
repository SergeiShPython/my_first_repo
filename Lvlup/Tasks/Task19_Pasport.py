import datetime
import time
from datetime import date
class Passport():
    def __init__(self,name, surname, birthday, country, passport_number):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.country= country
        self.passport_number = passport_number
    def PrintInfo(self, **kwargs):
        passport_single = []
        passport_single.append(self.name)
        passport_single.append(self.surname)
        passport_single.append(self.birthday)
        passport_single.append(self.country)
        passport_single.append(self.passport_number)
        return passport_single

passport_1 = Passport("Вася","Петров","08.07.1983","Россия","56 05 566781")
print(passport_1.PrintInfo())
class ForeignPassport(Passport):
    def __init__(self,visa, expiration_date):
        super().__init__(name="Дядя",surname="Федр",birthday="15.06.1999",country="Россия",passport_number="56 05 566789")
        self.visa = visa
        self.expiration_date = expiration_date
        self.time_now = date.today()

    def PrintInfo(self):
        return  super().PrintInfo(), 'Visa:',self.visa , 'Expiration date :', self.expiration_date
    def day_before_expiration(self):
        self.day_before_expiration_bebebe = self.expiration_date - self.time_now
        return self.day_before_expiration_bebebe
    def next_visa(self, new_visa):
        self.day_before_expiration_bebebe = self.day_before_expiration() + new_visa
        return self.day_before_expiration_bebebe

passport_2 = ForeignPassport('USA', '06.09.2025')
print(passport_2.PrintInfo())
passport_list = []
passport_list.append(passport_1)
passport_list.append(passport_2)
print(passport_2.day_before_expiration())