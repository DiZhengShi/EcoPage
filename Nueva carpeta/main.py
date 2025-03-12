from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/memes')
def memes():
    return render_template('memes.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
