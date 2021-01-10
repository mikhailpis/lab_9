#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# класс Liquid (жидкость), имеющий поля названия и плотности. Определить методы
# переназначения и изменения плотности. Создать производный класс Аlcohol (спирт),
# имеющий крепость. Определить методы переназначения и изменения крепости.
class Liquid:
    def __init__(self, name = "Water", plot = 50):
        self.name = name
        self.plot = plot


    def info(self, prompt):
        line = input() if prompt is None else input(prompt)
        parts = list(line.split(','))
        self.set_name(parts[0])
        self.set_plot(parts[1])


    def get_name(self):
        return self.name


    def get_plot(self):
        return self.plot


    def set_name(self, a):
        self.name = a


    def set_plot(self, a):
        self.plot = int(a)


class Acohol(Liquid):
    def __init__(self, name = "alcohol", plot = 50, krep = 45):
        super(Acohol, self).__init__(name, plot)
        self.krep = krep

    def get_name(self):
        return self.name


    def get_plot(self):
        return self.plot

    def get_krep(self):
        return self.krep

    def set_name(self, a):
        self.name = a


    def set_plot(self, a):
        self.plot = int(a)

    def set_krep(self, s):
        self.krep = int(s)


if __name__ == '__main__':
    r = Liquid()
    d = Acohol()
    r.info("Введите значения через запятую ")
    print(r.get_name(), "Название")
    print(r.get_plot(), "Плотность")
    print(d.get_krep(), "Градусов")
