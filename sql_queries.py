import models


def create_rate_currency(db, data_currencies, date_dt):
    """ Добавление записи со значением валюты """
    for data_currency in data_currencies:
        new_row = models.Currency(code=data_currency['code'],
                                  symbol=data_currency['symbol'],
                                  rate=data_currency['rate'],
                                  date_value = date_dt)
        db.session.add(new_row)
    db.session.commit()

def check_exists_date(date_dt):
    """ Проверка есть ли данные по конкретной дате """

    exists_date = models.Currency.query.filter(models.Currency.date_value == date_dt.strftime('%Y-%m-%d')).first()

    return exists_date

def select_by_dates(db, date_from, date_to):
    """ Выборка по датам """

    sql_request = """
        SELECT * FROM currencies
        WHERE date_value >= '{date_from}' AND date_value <= '{date_to}' ORDER BY date_value ASC""".format(date_from=date_from, date_to=date_to)

    sql_result = db.engine.execute(sql_request)
    sql_result = [dict(row) for row in sql_result]

    return sql_result
