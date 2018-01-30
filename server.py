from typograf import beautify_text
from werkzeug.utils import unescape
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/action', methods=['POST'])
def action():
    response = request.json
    text = beautify_text(response['text'])
    return jsonify(beauty_text=unescape(text))

if __name__ == "__main__":
    app.run()
