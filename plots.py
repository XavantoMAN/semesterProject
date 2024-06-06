import matplotlib.pyplot as plt
import pandas as pd
import backend

plt.rcParams['figure.figsize'] = [8.0, 4.0]
plt.rcParams['figure.dpi'] = 150


def plot_key_rate_all_time():
    try:
        key_rate = backend.get_key_rate_and_inflation()
    except:
        backend.update_data()
        key_rate = backend.get_key_rate_and_inflation()
    key_rate = key_rate[::-1]
    key_rate['Дата'] = key_rate['Дата'].astype('datetime64[ns]')
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    # plt.axis([datetime.date(2013, 9, 1), datetime.date(2024, 6, 1), 0.0, 25.0])
    # plt.plot(key_rate['Дата'], key_rate['Ключевая ставка, % годовых'], 'b')
    # plt.plot(key_rate['Дата'], key_rate['Инфляция, % г/г'], 'r')
    # plt.legend(['Ключевая ставка, % годовых', 'Инфляция, % г/г'], loc=2)
    plt.show()


def plot_key_rate_for_period(start_year: str, start_month: str, end_year: str, end_month: str):
    key_rate = backend.get_key_rate_and_inflation()
    key_rate = key_rate[::-1]
    key_rate['Дата'] = key_rate['Дата'].astype('string')
    index_start = key_rate[key_rate.Дата.str.contains(f'^{start_year}-{start_month}-01')].index
    index_end = key_rate[key_rate.Дата.str.contains(f'^{end_year}-{end_month}-01')].index
    key_rate = key_rate.loc[index_start[0]:index_end[0]]
    key_rate['Дата'] = key_rate['Дата'].astype('datetime64[ns]')
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    plt.show()


def pie_diagram_gdp_in_monetary_current():
    gdp_in_monetary = backend.get_gdp_in_monetary_current()
    gdp_in_monetary['Last'] = gdp_in_monetary['Last'].astype('float')
    gdp_in_monetary.plot(kind='pie', y='Last', autopct='%1.0f%%')
    plt.title('Распределение ВВП по отраслям')
    plt.legend(gdp_in_monetary['Name'], loc='best', bbox_to_anchor=(0.15, 0.37))
    plt.show()


def plot_gdp_for_period(start_year: str, end_year: str):
    gdp_for_period = backend.get_gdp_all_time()
    gdp_for_period['Amount'] = gdp_for_period['Amount'].astype('float')
    gdp_for_period['Year'] = gdp_for_period['Year'].astype('string')
    index_start = gdp_for_period[gdp_for_period.Year == start_year].index
    index_end = gdp_for_period[gdp_for_period.Year == end_year].index
    gdp_for_period = gdp_for_period.loc[index_start[0]:index_end[0]]
    gdp_for_period.plot(x='Year', y='Amount')
    plt.title('ВВП(в текущих ценах, млрд. рублей)')
    plt.show()


def plot_gdp_growth_for_period(start_year: str, end_year: str):
    gdp_growth_for_period = backend.get_gdp_growth()
    gdp_growth_for_period['Year'] = gdp_growth_for_period['Year'].astype('string')
    index_start = gdp_growth_for_period[gdp_growth_for_period.Year == start_year].index
    index_end = gdp_growth_for_period[gdp_growth_for_period.Year == end_year].index
    gdp_for_period = gdp_growth_for_period.loc[index_start[0]:index_end[0]]
    gdp_for_period.plot(x='Year', y='Percent')
    plt.title('Годовой рост ВВП(в процентах)')
    plt.show()


def plot_currency_for_period(currency_code: str, from_date: str, to_date: str):
    currency_for_period = backend.parse_currency_for_period(currency_code, from_date, to_date)
    currency_for_period.plot(x='Дата', y='Курс')
    plt.title('Динамика курса валюты за выбранный период')
    plt.ylabel('Рубли')
    plt.show()


def diagram_selected_currencies(selected: list):
    currencies = backend.get_today_currencies()
    selected = pd.Series(selected)
    currencies = currencies[currencies['Валюта'].isin(selected)]
    currencies['Курс'] = currencies['Курс'].astype('float')
    currencies.plot(kind='barh', x='Букв. код', y='Курс')
    plt.title('Стоимость одной единицы валюты')
    plt.xlabel('Рубли')
    plt.ylabel('Букв. код страны')
    plt.show()
