from config import app, render_template
from models import Flat
import random


@app.route("/")
def index_1():
    cat_name = "Chsuke"
    return render_template("cats.html", cat_name=cat_name)

@app.route("/flats/")
def flats_view():
    flats = Flat.query.all()
    return render_template("flats.html", flats=flats)

@app.route(f"/random/<number_1>/<number_2>/")
def index_2(number_1, number_2):
    text = random.randint(int(number_1), int(number_2))
    return str(text)


app.run(debug=True)
