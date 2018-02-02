from flask import jsonify, Flask, request
import PrinterInfo

app = Flask(__name__)


@app.route('/api/printer')
def printer_view():
  if request.method == 'GET':
    return PrinterInfo.get_printer_info()
  if request.method == 'POST':
    pass
    return "Hello world!"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
