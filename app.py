from flask import Flask, render_template, request, current_app, jsonify
from sudo_recur import Sudo
import logging

app = Flask(__name__)

# DEBUG INFO WARNING ERROR CRITICAL
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
# format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-7s %(message)s')
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('sudoku.html')
    # return '<h1>my Tutorial of V-charts and D3</h1><br><br>' \
    #        '<a href="/pixi/a">PIXIJS - demo</a><br>' \
    #        '<a href="/vc/b">v-charts</a><br>' \
    #        '<a href="/d3/a">D3 - demo</a>'

@app.route('/solve', methods=['GET', 'POST'])
def solve_sudo():
    # {'puzzle': '8,0,0,0,0,0,0,0,0,0,0,3...'}
    # jsondata = request.get_json()
    # app = current_app._get_current_object()
    data = request.get_json().get('puzzle', '')
    app.logger.debug(f'puzzle: {data}')
    if data:
        data = [int(x) for x in data.split(',')]
        sudo = Sudo(data)
        sudo.sudo_solve_iter()
        return jsonify({
            'code': 'success',
            'result': sudo.value.tolist()
        })
    else:
        return jsonify({
            'code': 'fail',
            'result': '无效的数独！'
        })

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
