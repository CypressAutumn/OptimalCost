from flask import render_template, g, jsonify, request, current_app, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/count', methods=['POST'])
def count():
    data = request.json
    print(data)
    return 'render_template()'
