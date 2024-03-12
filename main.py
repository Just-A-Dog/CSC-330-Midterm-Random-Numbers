from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/random/<int:n>')
def randNum(n):
    numbers = []
    for i in range(n):
        numbers.append(random.random())
    return render_template('randNumsTable.html', numbers = numbers)
