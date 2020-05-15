from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    some_text = "There are 3 websites."
    current_year = datetime.datetime.now().year
    return render_template("About me.html", some_text=some_text, current_year=current_year)


@app.route("/portfolio")
def portfolio():
    return render_template("Portfolio.html")

@app.route("/portfolio/fakebook")
def portfolio_fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/boogle")
def portfolio_boogle():
    return render_template("boogle.html")

@app.route("/portfolio/hair-salon")
def portfolio_hairsalon():
    return render_template("salon.html")

if __name__ == '__main__':
    app.run()


