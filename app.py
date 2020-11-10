from flask import request, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import controllers
import models


app = Flask(__name__)

app.config.from_pyfile('config.py')
app.secret_key = 'EFFw434#$#$@#f3'
db = SQLAlchemy(app)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    data_currencies = []

    # если были переданы даты, то идет проверка есть ли данные в БД, если нет, то идет запрос на cbr, а затем сохраняется в БД
    if request.method == 'POST':
        date_from = request.form['date_from'].strip()
        date_to = request.form['date_to'].strip()

        # валидация дат и преобразование в datetime
        dates_generate = controllers.validate_dates(date_from, date_to)

        # получение и запись данных в БД
        if dates_generate:
            for date_generate in dates_generate:
                controllers.load_currencies_by_date(db, date_generate)

            # получение данных из БД
            data_currencies = controllers.load_results_currencies(db, date_from, date_to)


    return render_template('index.html', data_currencies=data_currencies, request_form=request.form)


app.run(host='0.0.0.0', port=2323)
