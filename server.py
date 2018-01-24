from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/action', methods=['POST'])
def action():
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run()
