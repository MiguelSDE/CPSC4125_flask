#app.py
from flask import Flask, render_template, session
app = Flask(__name__)

app.secret_key= "personal secret"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/count")
def hello_named():
    y = session.get('y', None)
    if not y:
        session['y'] = 1
    elif y >= 10:
        session.clear()
        return "The session is clear"
    else:
        session['y'] += 1
    return "Total refreshes for user are : " + str(session['y'])

@app.route("/api")
def api():
    return '{"month": "11", "num": 2386, "link": "", "year": "2020", "news": "", "safe_title": "Ten Years", "transcript": "", "alt": "The ten-year cancerversary is traditionally the Cursed Artifact Granting Immortality anniversary.", "img": "https://imgs.xkcd.com/comics/ten_years.png", "title": "Ten Years", "day": "16"}'

if __name__ == "__main__":
    app.run(debug=True)