from flask import Flask
import logging
from logging import Formatter, FileHandler
from flask_sqlalchemy import SQLAlchemy
from forms import SearchForm

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask('application')


app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


import views

if __name__ == '__main__':
    app.run(debug=True)
