import datetime
from flask import flash
from cbr import get_exchange_rates
import config
import sql_queries

def load_currencies_by_date(db, date_generate):
    """ Получение данных с сервера cbr """

    # Проверка есть ли в БД записи для даты
    if sql_queries.check_exists_date(date_generate['date_dt']):
        return False

    # Получение данных с сервера cbr
    data_currencies = get_exchange_rates(date_generate['date_string'])

    # запись в БД
    sql_queries.create_rate_currency(db, data_currencies, date_generate['date_dt'])

    return data_currencies

def date_str_to_datetime(date_value):
    """ Преобразует строку в datetime """
    try:
        return datetime.datetime.strptime(date_value, '%d.%m.%Y')
    except:
        flash(f'Некорректный формат даты! {date_value}')
        return False

def validate_dates(date_from, date_to):
    """ Валидация поля даты """
    date_from_dt = date_str_to_datetime(date_from)
    date_to_dt = date_str_to_datetime(date_to)

    if not date_from_dt or not date_to_dt:
        return False

    if date_from_dt > date_to_dt:
        flash(f'Дата "ОТ" не может быть больше даты "ДО"!')
        return False

    # проверка на максимальный диапазон
    between_dates = date_to_dt - date_from_dt
    if between_dates.days > config.MAX_INTERVAL_DATES:
        flash(f'Интервал не может быть больше {config.MAX_INTERVAL_DATES} дней!')
        return False

    # генерация дат для запросов курса валют
    dates_generate = []
    for day in range(between_dates.days+1):
        date_dt = date_from_dt + datetime.timedelta(days=day)
        dates_generate.append({'date_string': date_dt.strftime('%d.%m.%Y'), 'date_dt':date_dt})

    return dates_generate

def load_results_currencies(db, date_from, date_to):
    """ Получает все строки по дате """
    date_from = date_str_to_datetime(date_from).strftime('%Y-%m-%d')
    date_to = date_str_to_datetime(date_to).strftime('%Y-%m-%d')

    data_currencies = sql_queries.select_by_dates(db, date_from, date_to)

    return data_currencies