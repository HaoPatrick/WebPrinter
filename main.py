from flask import jsonify, Flask, request, render_template

import PrinterHandler
import os
import config

app = Flask(__name__, static_folder='frontend')


def error_response(e, error_code=500):
  response = jsonify({'status': 'error', 'msg': e})
  response.status_code = error_code
  return response


def data_response(data):
  return jsonify({'status': 'ok', 'data': data})


def allowed_file(filename: str):
  return '.' in filename and filename.split(".")[1] == 'pdf'


def secure_filename(filename: str):
  tokens = filename.split('.')
  return tokens[0].replace('.', '_').replace('/', '_') + '.' + tokens[1]


@app.route('/api/printer')
def printer_view():
  if request.method == 'GET':
    try:
      return data_response({'options': PrinterHandler.get_printer_info()})
    except PrinterHandler.PrinterError as e:
      return error_response(e)


@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
      return error_response("file not found", 403)
    file = request.files['file']
    if file.filename == '':
      return error_response("no selected file", 403)
    if file and allowed_file(file.filename):
      rv_filename = secure_filename(file.filename)
      file.save(os.path.join(config.UPLOAD_FOLDER, rv_filename))
      return data_response({'filename': rv_filename})


@app.route('/api/print', methods=['GET', 'POST'])
def print_it():
  if request.method == 'POST':
    user_config = request.json
    if user_config.get('options', None) and user_config.get('token', None):
      if user_config['token'] != config.TOKEN:
        return error_response('incorrect token', 403)
      try:
        PrinterHandler.set_printer(user_config['options'])
        PrinterHandler.print_file(user_config['filename'], user_config['basicOptions'])
        return data_response({'msg': 'printing'})
      except FileNotFoundError as e:
        return error_response('Requested file not found', 400)
    else:
      return error_response('not enough argument', 403)


@app.route('/')
def index_page():
  return app.send_static_file('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
