import io
from flask import Flask, render_template, request, send_file
from utils import *
from screenshot import Screenshot
app = Flask(__name__)

data_list = []

@app.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

@app.route('/', methods=['GET', 'POST'])
def handler():
    global data_list
    data_list = request.get_json()
    ss_get = ss.screenshot()
    if Config.RETURN_PNG:
        return send_file(io.BytesIO(ss_get), mimetype='image/png')
    else:
        return ss_get

@app.route('/quote/', methods=['GET', 'POST'])
def quote():
    global data_list
    return render_template('main-template.html', data_list=data_list)
    
if __name__ == '__main__':
    # init headless browser
    ss = Screenshot()
    
    app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT, debug=True)
