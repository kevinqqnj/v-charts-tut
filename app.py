from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>my Tutorial of V-charts and D3</h1><br><br>' \
           '<a href="/vc/b">v-charts</a><br>' \
           '<a href="/d3/a">D3 - a</a>'

@app.route('/vc/<string:chapter>')
def vcharts(chapter):
    return render_template(f'vc-{chapter}.html')

@app.route('/d3/<string:chapter>')
def d3(chapter):
    return render_template(f'd3-{chapter}.html')


if __name__ == '__main__':
    app.run()
