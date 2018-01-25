from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/action', methods=['POST'])
def action():
    print(request.json)
    return jsonify(response='утка')

if __name__ == "__main__":
    app.run()
