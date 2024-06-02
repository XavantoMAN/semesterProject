import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import backend


def plot_key_rate_all_time():
    key_rate = backend.get_key_rate_and_inflation()
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    # plt.axis([datetime.date(2013, 9, 1), datetime.date(2024, 6, 1), 0.0, 25.0])
    # plt.plot(key_rate['Дата'], key_rate['Ключевая ставка, % годовых'], 'b')
    # plt.plot(key_rate['Дата'], key_rate['Инфляция, % г/г'], 'r')
    # plt.legend(['Ключевая ставка, % годовых', 'Инфляция, % г/г'], loc=2)
    plt.show()


def plot_key_rate_for_year(year: str):
    key_rate = backend.get_key_rate_and_inflation()
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    plt.show()


plot_key_rate_all_time()
