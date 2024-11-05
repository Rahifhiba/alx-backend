#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

# Pass the required route to the decorator.
@app.route("/")
def hello():
	return render_template('0-index.html')

if __name__ == "__main__":
	app.run(debug=True)
