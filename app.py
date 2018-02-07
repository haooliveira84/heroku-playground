import json
import requests
import flask

app = flask.Flask(__name__)

@app.route('/macaddr', methods=['GET','POST'])
@app.route('/macaddr/<macaddr>', methods=['GET'])

def macaddr(macaddr=None):
	if flask.request.method == 'POST':
    			json_dict = flask.request.get_json()
			if flask.request.headers.get('macaddr'):
    				macaddr = flask.request.headers.get('macaddr')
			else:
					macaddr = json_dict['macaddr']
	else:
			if flask.request.args.get('macaddr'):
					macaddr = flask.request.args.get('macaddr')
	response = connected_Database(macaddr)
	return response

def mac_consult(macaddr):
    response = {}
    url = 'http://macvendors.co/api/jsonp/'
    response = requests.get(ural+macaddr)
    return response

def json_view(response, status_code):
	response = flask.Response(
		response,
		status=status_code,
		mimetype='application/json'
	)
	return response

def datetime_converter(obj):
    if isinstance(obj, datetime.datetime):
    		return obj.__str__()


if __name__ == "__main__":
	app.run(host='0.0.0.0')