from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
returnrender_template("home.html")

@app.route('/about/')
def about():
returnrender_template("about.html")

if __name__ == "__main__":
app.run(debug=True)
