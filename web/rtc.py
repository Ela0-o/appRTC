import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from FunkPack.function import Parabola, LinearFunk

# Функция для отрисовки графика линейной функции
def plot_linear_function(ax, lin):
    x = np.linspace(-10, 10, 100)
    a, b = lin.params
    y = lin.calc_l(x)
    ax.plot(x, y, label=f'Linear Function: y = {a}x + {b}')

# Функция для отрисовки графика параболы
def plot_parabola(ax, par):
    x = np.linspace(-10, 10, 100)
    a, b, c = par.params 
    y = par.calc_p(x)
    ax.plot(x, y, label=f'Parabola: y = {a}x^2 + {b}x + {c}')

# Основная часть приложения
def main():
    # Определение колонок для размещения элементов
    params_column, plot_column, buttons_column= st.columns(3)

    lin = LinearFunk()
    par = Parabola()

    with buttons_column:
        linear_button = st.button("Линейная функция")
        parabola_button = st.button("Парабола")
        default_button = st.button("Сброс")
    if linear_button:
        with params_column:
            linear_a = st.number_input("Введите значение a для линейной функции", value=2.0)
            linear_b = st.number_input("Введите значение b для линейной функции", value=1.0)
            if default_button:
                linear_a, linear_b = lin.default()
            lin.params = [linear_a, linear_b] 

    if parabola_button:
            with params_column:
                parabola_a = st.number_input("Введите значение a для параболы", value=2.0)
                parabola_b = st.number_input("Введите значение b для параболы", value=1.0)
                parabola_c = st.number_input("Введите значение c для параболы", value=1.0)
                if default_button:
                    parabola_a, parabola_b, parabola_c = par.default()
                par.params = [parabola_a, parabola_b,parabola_c] 
        

    with plot_column:
        st.subheader("Линейная функция")
        fig1, ax1 = plt.subplots(figsize=(5, 3))
        plot_linear_function(ax1, lin)
        plt.legend()
        st.pyplot(fig1)
        st.write()
        
        st.subheader("Парабола")
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        plot_parabola(ax2, par)
        plt.legend()
        st.pyplot(fig2)
        st.write()

if __name__ == "__main__":
    main()
