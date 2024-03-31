from flask import Flask, render_template
from project.oracle import get_oracle, get_oracle_color


app = Flask(__name__)

prediction_counter = 0


@app.route('/')
def index():
    global prediction_counter
    
    oracle = get_oracle()
    oracle_color = get_oracle_color(oracle)

    prediction_counter += 1
    
    return render_template(
        'index.html',
        oracle=oracle,
        oracle_color=oracle_color,
        prediction_counter=prediction_counter,
        )


if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)
