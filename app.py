from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sudoku.html')
    # return '<h1>my Tutorial of V-charts and D3</h1><br><br>' \
    #        '<a href="/pixi/a">PIXIJS - demo</a><br>' \
    #        '<a href="/vc/b">v-charts</a><br>' \
    #        '<a href="/d3/a">D3 - demo</a>'

@app.route('/pixi/<string:chapter>')
def pixi(chapter):
    return render_template(f'pixi-{chapter}.html')

@app.route('/vc/<string:chapter>')
def vcharts(chapter):
    return render_template(f'vc-{chapter}.html')

@app.route('/d3/<string:chapter>')
def d3(chapter):
    return render_template(f'd3-{chapter}.html')


if __name__ == '__main__':
    app.run()
