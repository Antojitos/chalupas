from flask import Flask

app = Flask(__name__)
app.config.from_object('chalupas.config')
app.config.from_envvar('CONFIG', silent=True)

from chalupas import routes
