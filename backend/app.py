from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__,
    template_folder='../dist',
    static_folder='../dist/static')

def error(msg):
    return jsonify({'err': msg})

def validate_args(keywords, args, url):
    for kw in keywords:
        if kw not in args:
            return error(f'{kw} not in args ({url})')
    return None

'''Home screen'''
@app.route('/')
def index():
    return render_template('index.html')

'''Get or post subject FC'''
@app.route('/data/fc', methods=(['GET', 'POST']))
def fc():
    args = request.args
# Optional: paradigm, session, format (image or raw), colorbar
    args_err = validate_args(['cohort', 'sub'], args, request.url) 
    if args_err:
        return args_err
    if request.method == 'GET':
        return jsonify({'data': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
