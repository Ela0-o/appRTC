import numpy as np
import matplotlib.pyplot as plt


class LinearFunk:

    def __init__(self, parameters: list):
        # self.__name = name
        self.__a = parameters[0]
        self.__b = parameters[1]

    @property
    def params(self):
        return self.__a, self.__b

    @params.setter
    def params(self, parameters):
        if type(parameters[0]) in (int, float)\
                and type(parameters[1]) in (int, float):
            self.__a = parameters[0]
            self.__b = parameters[1]
        else:
            raise ValueError("Параметры должны быть числами")
        # if name == 'Линейная':
        #     self.__name = name
        # else:
        #     raise 'Неверное имя'

    def calc_l(self, x):
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = self.__a * x[i] + self.__b
        return y

    def default(self):
        self.__a = 1
        self.__b = 0
        # self.__name = 'Линейная'
        return self.__a, self.__b


class Parabola:

    def __init__(self, parameters: list):
        self.__a = parameters[0]
        self.__b = parameters[1]
        self.__c = parameters[2]

    @property
    def params(self):
        return self.__a, self.__b, self.__c

    @params.setter
    def params(self, parameters):
        if type(parameters[0]) in (int, float) \
                and type(parameters[1]) in (int, float) \
                and type(parameters[2]) in (int, float):
            self.__a = parameters[0]
            self.__b = parameters[1]
            self.__c = parameters[2]
        else:
            raise ValueError("Параметры должны быть числами")

    def calc_p(self, x):
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = self.__a * x[i] ** 2 + self.__b * x[i] + self.__c
        return y

    def default(self):
        self.__a = 1
        self.__b = 0
        self.__c = 0
        return self.__a, self.__b, self.__c


if __name__ == "__main__":
    # name = 'Линейная'
    par = [2, 1]
    l = LinearFunk(par)
    l.params = l.default()

    param = [2, 2, 2]
    p = Parabola(param)
    p.params = p.default()

    x = []
    h = 1/10
    for i in range(-100, 101):
        x.append(i*h)
    print(x)

    # print(l.params, l.__dict__)
    print(l.calc_l(x))
    print(p.calc_p(x))
    plt.plot(x, l.calc_l(x))
    plt.plot(x, p.calc_p(x))
    plt.show()

