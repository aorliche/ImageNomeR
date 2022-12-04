from flask import Flask, request, jsonify, render_template
import os
import multiprocessing as mp
import json

# Our modules
import power
import data
import image
import cohort

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

'''List cohorts'''
@app.route('/data/list', methods=(['GET']))
def list():
    args = request.args
    task = args['task'] if 'task' in args else None
    return jsonify({'cohorts': cohort.ls_cohorts('anton')})

'''Get info about subjects'''
@app.route('/data/info', methods=(['GET']))
def info():
    args = request.args
    args_err = validate_args(['cohort'], args, request.url) 
    if args_err:
        return args_err
    coh = args['cohort']
    return jsonify(cohort.get_cohort('anton', coh))

'''Get subgroup of cohort'''
@app.route('/data/group', methods=(['GET']))
def group():
    args = request.args
    args_err = validate_args(['cohort', 'query'], args, request.url) 
    if args_err:
        return args_err
    cohort = args['cohort']
    query = args['query']
    demo = data.get_demo('anton', cohort)
    df = data.demo2df(demo)
    group = data.make_group_query(df, query)
    return jsonify(group)

'''Get demographics graph'''
@app.route('/data/demo/hist', methods=(['GET', 'POST']))
def demo_hist():
    if request.method == 'GET':
        args = request.args
    else:
        args = request.form
    args_err = validate_args(['cohort', 'groups', 'field'], args, request.url)
    if args_err:
        return args_err
    cohort = args['cohort']
    field = args['field']
    groups = json.loads(args['groups'])
    demo = data.get_demo('anton', cohort)
    df = data.demo2df(demo)
    img = image.groups_hist(df, groups, field)
    return jsonify({'data': img})

'''Get or post subject FC'''
@app.route('/data/fc', methods=(['GET', 'POST']))
def fc():
    args = request.args
    # Optional: task, session
    args_err = validate_args(['cohort', 'sub'], args, request.url) 
    if args_err:
        return args_err
    if request.method == 'GET':
        # Params
        cohort = args['cohort']
        sub = args['sub']
        task = args['task'] if 'task' in args else None
        ses = args['ses'] if 'ses' in args else None
        colorbar = 'colorbar' in args
        remap = 'remap' in args
        # Load and display FC
        fc = data.get_fc('anton', cohort, sub, task, ses)
        fc = data.vec2mat(fc)
        if remap:
            fc = power.remap(fc)
        # Weird stuff with matplotlib and multithreading? crashes the process
        # Can fix with mutliprocessing
        q = mp.Queue()
        def wrapper(q, fc, colorbar):
            img = image.imshow(fc, colorbar)
            q.put(img)
        p = mp.Process(target=wrapper, args=(q,fc,colorbar))
        p.start()
        img = q.get()
        p.join()
        return jsonify({'data': img})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
