from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://///home/ilde/Documents/Dev/sqlalchemy/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Equipos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    pais = db.Column(db.String(30))

    def __repr__(self):
        return "<Equipos %r>" % self.nombre


if __name__ == "__main__":
    app.run(debug=True)
     