import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import backend

plt.rcParams['figure.figsize'] = [8.0, 4.0]
plt.rcParams['figure.dpi'] = 140


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


def plot_key_rate_for_year(year: str):
    key_rate = backend.get_key_rate_and_inflation()
    key_rate = key_rate[::-1]
    key_rate['Дата'] = key_rate['Дата'].astype('string')
    key_rate = key_rate[key_rate.Дата.str.contains(f'^{year}-..-01')]
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    plt.show()


def plot_key_rate_for_period(start_year: str, start_month: str, end_year: str, end_month: str):
    key_rate = backend.get_key_rate_and_inflation()
    key_rate = key_rate[::-1]
    key_rate['Дата'] = key_rate['Дата'].astype('string')
    index_start = key_rate[key_rate.Дата.str.contains(f'^{start_year}-{start_month}-01')].index
    index_end = key_rate[key_rate.Дата.str.contains(f'^{end_year}-{end_month}-01')].index
    print(index_end, index_start)
    key_rate = key_rate.loc[index_start[0]:index_end[0]]
    key_rate.plot(x='Дата', y=['Ключевая ставка, % годовых', 'Инфляция, % г/г'])
    plt.show()


def pie_diagram_gdp_in_monetary_current():
    gdp_in_monetary = backend.get_gdp_in_monetary_current()
    gdp_in_monetary['Last'] = gdp_in_monetary['Last'].astype('float')
    gdp_in_monetary.plot(kind='pie', y='Last', autopct='%1.0f%%')
    plt.title('ВВП в денежном представлении')
    plt.legend(gdp_in_monetary['Name'], loc='best', bbox_to_anchor=(0.15, 0.37))
    plt.show()


#pie_diagram_gdp_in_monetary_current()
