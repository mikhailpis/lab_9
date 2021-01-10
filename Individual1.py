#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Реализовать класс Account, представляющий собой банковский счет. В классе должны быть
#четыре поля: фамилия владельца, номер счета, процент начисления и сумма в рублях.
#Открытие нового счета выполн яется операцией инициализации. Необходимо выполнять
#следующие операции: сменить владельца счета, снять некоторую сумму денег со счета,
#положить деньги на счет, начислить проценты, перевести сумму в доллары, перевести
#сумму в евро, получить сумму прописью (преобразовать в числительное).

class Account:

    def __init__(self, secName = "Anton", num = "232332323", pos = "0.13",rub = 15000):
        self.secName = secName
        self.num = num
        self.pos = pos
        self.rub = rub


    def info(self, prompt):
        line = input() if prompt is None else input(prompt)
        parts = list(line.split(','))
        self.set_secName(parts[0])
        self.set_num(parts[1])
        self.set_pos(parts[2])
        self.set_rub(parts[3])


    def get_secName(self):
        return self.secName


    def get_num(self):
        return self.num


    def get_pos(self):
        return self.pos


    def get_rub(self):
        return self.rub



    def set_secName(self, a):
        self.secName = a


    def set_num(self, a):
        self.num = int(a)


    def set_pos(self, a):
        self.pos = float(a)


    def set_rub(self, a):
        self.rub = int(a)


    def snyatsymm(self):
        a = int(input("Введите сумму которую хотите снять "))
        return self.rub - a


    def dobav(self):
        b = int(input("Введите сумму которую хотите положить"))
        return self.rub + b


    def prosent(self):
        a = float(input("Введите процент хотите положить"))
        return self.pos + a


    def dollars(self):
       return self.rub * 73.52


    def euro(self):
       return self.rub * 90.08


if __name__ == '__main__':
    r = Account()
    r.info("Введите все через запятую ")
    r.set_secName("Vasya")
    print(r.get_secName())
    print(r.get_num())
    print(r.get_pos())
    print(r.get_rub())
    print(r.snyatsymm())
    print(r.dobav())
    print(r.prosent())
    print(r.dollars())
    print(r.euro())
