from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os.path
import folium
import settings as st

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///map_db'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

#create mab obj
m = folium.Map(location=[st.startPointx, st.startPointy], zoom_start = 12)
# generate map obj
m.save("C:/Users/pmroz/Documents/GitHub\HACKYEAH_project/mapsApp/templates/map.html")

class Hospitals(db.Model):
    __tablename__ = 'hospitals_data'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    mPoint = db.Column(db.Text, primary_key=False)
    xPos = db.Column(db.Float, primary_key=False)
    yPos = db.Column(db.Integer, primary_key=False)
    providence = db.Column(db.Text, primary_key = False)

@app.route('/')
def hello():
    zip_hospitals = Hospitals.query.filter_by(providence = "mazowieckie")
    return render_template('index.html',szpitale_count = Hospitals.query.count(),
        new_infected = 128, zip = zip_hospitals)

@app.route('/map')
def run_map():   
    return render_template("map.html")

@app.route('/admin')
def admin_page():
    return "Admin page :D"

if __name__ == "__main__":
    app.run(debug=True)