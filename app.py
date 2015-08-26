from flask import Flask, render_template, request, jsonify
from werkzeug.routing import Rule
import datetime

app = Flask(__name__)

app.url_map.add(Rule('/', defaults={'path' : ''}, endpoint='index'))
app.url_map.add(Rule('/<path:path>', endpoint='index'))

webhook_hits = []

def extract(d):
    return {key: value for (key, value) in d.items()}


@app.endpoint('index')
def index(path):
    if not path:
        return render_template('index.html', webhook_hits=webhook_hits)

    data = {
        'success' : True,
        'status' : request.args.get('status'),
        'time' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'path' : request.path,
        'script_root' : request.script_root,
        'url' : request.url,
        'base_url' : request.base_url,
        'url_root' : request.url_root,
        'method' : request.method,
        'headers' : extract(request.headers),
        'data' : request.data.decode(encoding='UTF-8'),
        'host' : request.host,
        'args' : extract(request.args),
        'form' : extract(request.form),
        'cookies' : extract(request.cookies)
    }
    webhook_hits.append(data)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)