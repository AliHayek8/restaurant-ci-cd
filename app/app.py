from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_restaurant(meal):
    conn = sqlite3.connect("restaurants.db")
    c = conn.cursor()
    c.execute("SELECT name FROM restaurants WHERE meal=?", (meal,))
    result = c.fetchone()
    conn.close()
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    if request.method == "POST":
        meal = request.form["meal"]
        result = get_restaurant(meal)
        if result:
            recommendation = result[0]
        else:
            recommendation = "No restaurant found"
    return render_template("index.html", recommendation=recommendation + " 🍽️" )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
