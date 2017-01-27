from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("main.html")


@app.route('/fixit')
def fixit_page():
    return render_template("fixit.html")


@app.route('/aboutme')
def aboutme_page():
    return render_template("aboutme.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
