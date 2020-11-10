from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


class Currency(db.Model):
    """Таблица с данными валют"""

    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    rate = db.Column(db.Float(), nullable=False)
    date_value = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return '<Currency {}>'.format(self.id)

db.create_all()