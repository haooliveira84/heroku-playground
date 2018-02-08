#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests
import flask


app = flask.Flask(__name__)


@app.route('/macaddr/<macaddr>', methods=['GET'])
def mac_consult(macaddr=None):
	response = {}
	url = 'http://macvendors.co/api/jsonp/'
	try:
		req_response = requests.get(url+macaddr)
	except:
		response = json.dumps({'status':'error','message':'Error'})

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
	app.run(debug=True, use_reloader=True)
