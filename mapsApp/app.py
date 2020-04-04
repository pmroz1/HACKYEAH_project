from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

DATABASE = '/map_db'

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:///map_db'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

class Szpitale(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    x = db.Column(db.number())

@app.route('/')
def hello():
    print("total number of hospitals is", Szpitale.query.count())
    return render_template('index.html')

@app.route('/admin')
def admin_page():
    return "Admin page :D"

if __name__ == "__main__":
    app.run(debug=True)