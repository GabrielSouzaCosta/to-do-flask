from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

from views import app

# migrate = Migrate(app, db)
