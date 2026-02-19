from flask import Flask, jsonify, render_template
import random

from mult_recur import mult_recur

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_problem')
def new_problem():
    card1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    card2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    answer = mult_recur(card1, card2)
    
    return jsonify({
        'card1': card1,
        'card2': card2,
        'answer': answer
    })

if __name__ == '__main__':
    app.run(debug=True)