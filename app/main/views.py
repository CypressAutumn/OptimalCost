from flask import render_template, g, jsonify, request, current_app, url_for
from . import main
from ..core import optimalCost

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/count', methods=['POST'])
def count():
    data = request.json
    tarland = float(data['c'][0])
    minmax = data['c'][1].split(',')
    cmin = int(minmax[0])
    cmax = int(minmax[1])
    error = float(data['c'][2])
    oc = optimalCost(tarland, (cmin,cmax), error)
    group = {}
    for i in range(0,len(data['spec'])):
        group[float(data['spec'][i])] = float(data['cost'][i])
    ocg = oc.optimalGroup(group)
    return jsonify(ocg)
