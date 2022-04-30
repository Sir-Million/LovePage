from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def principal():
    return render_template('index.html')

@app.route('/opinion-general')
def opinion():
    return render_template('opinion.html')

@app.route('/my-mind')
def mind():
    return render_template('mind.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)