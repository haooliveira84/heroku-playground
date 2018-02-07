#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
	response = mac_consult(macaddr)
	return response

def mac_consult(macaddr):
	response = {}
	url = 'http://macvendors.co/api/jsonp/'
	try:
		req_response = requests.get(url+macaddr)
	except:
		response = json.dumps({'status':'error','message':'Error'})
	finally:
		if req_response == None:
			status_code=404
			response=json.dumps({'code':status_code,'status':'error','message':'MAC Not Found!'})
		else:
			status_code=200
			response = req_response
	return json_view(response, status_code)

def json_view(response, status_code):
	response = flask.Response(
		response,
		status=status_code,
		mimetype='application/json'
	)
	return response

if __name__ == "__main__":
	app.run(host='0.0.0.0')