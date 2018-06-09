from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('vc.html')

@app.route('/d3/<string:chapter>')
def d3(chapter):
    return render_template(f'd3-{chapter}.html')


if __name__ == '__main__':
    app.run()
