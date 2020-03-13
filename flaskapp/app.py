from application import routes
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')

