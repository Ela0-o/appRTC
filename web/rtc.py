import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from FunkPack.function import Parabola, LinearFunk

# Инициализация st.session_state
if 'linear_params' not in st.session_state:
    st.session_state.linear_params = {'a': 1.0, 'b': 0.0}

if 'parabola_params' not in st.session_state:
    st.session_state.parabola_params = {'a': 1.0, 'b': 0.0, 'c': 0.0}

# Инициализация функций
if 'lin' not in st.session_state:
    st.session_state.lin = LinearFunk()

if 'par' not in st.session_state:
    st.session_state.par = Parabola()

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

def transfer(ax, lin, par):
    x = np.linspace(-10, 10, 100)
    y = lin.calc_l(x)
    a, b, c = par.params 
    z = par.calc_p(y)
    ax.plot(y, z, label=f'Parabola: y = {a}x^2 + {b}x + {c}')

# Основная часть приложения
def main():
    # Определение колонок для размещения элементов
    params_column, plot_column, buttons_column= st.columns(3)

    # Определение флага активной кнопки
    if 'active_button' not in st.session_state:
        st.session_state.active_button = None

    with buttons_column:
        linear_button = st.button("Линейная функция", key="linear_button")
        parabola_button = st.button("Парабола", key="parabola_button")
        default_button = st.button("Сброс", key="default_button")
        transfer_button = st.button("Передача", key="transfer_button")
       
    if linear_button and (st.session_state.active_button != "linear"):
        st.session_state.active_button = "linear"

    if parabola_button and (st.session_state.active_button != "parabola"):
        st.session_state.active_button = "parabola"

    if default_button:
        st.session_state.active_button = None
        linear_a, linear_b = st.session_state.lin.default()
        parabola_a, parabola_b, parabola_c = st.session_state.par.default()


    with params_column:
        if st.session_state.active_button == "linear":
            linear_a = st.number_input("Введите значение a для линейной функции", value=st.session_state.linear_params['a'])
            linear_b = st.number_input("Введите значение b для линейной функции", value=st.session_state.linear_params['b'])
            st.session_state.lin.params = [linear_a, linear_b] 
            st.session_state.linear_params = {'a': linear_a, 'b': linear_b}
            
        if st.session_state.active_button == "parabola":
            parabola_a = st.number_input("Введите значение a для параболы", value=st.session_state.parabola_params['a'])
            parabola_b = st.number_input("Введите значение b для параболы", value=st.session_state.parabola_params['b'])
            parabola_c = st.number_input("Введите значение c для параболы", value=st.session_state.parabola_params['c'])
            st.session_state.par.params = [parabola_a, parabola_b, parabola_c] 
            st.session_state.parabola_params = {'a': parabola_a, 'b': parabola_b, 'c': parabola_c}


    with plot_column:
        st.subheader("Линейная функция")
        fig1, ax1 = plt.subplots(figsize=(5, 3))
        plot_linear_function(ax1, st.session_state.lin)
        plt.legend()
        st.pyplot(fig1)
        st.write()
        
        st.subheader("Парабола")
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        plot_parabola(ax2, st.session_state.par)
        plt.legend()
        st.pyplot(fig2)
        st.write()
        if transfer_button:
            st.subheader("Передача")
            fig3, ax3 = plt.subplots(figsize=(5, 3))
            transfer(ax3, st.session_state.lin, st.session_state.par)
            plt.legend()
            st.pyplot(fig3)
            st.write()

if __name__ == "__main__":
    main()