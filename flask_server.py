import os

# PyPI
from flask import Flask, render_template, request

import device_info
import itunes_api

###

app = Flask(__name__)

# Index / search
@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	
	if request.method == 'GET':
		data = None
	if request.method == 'POST':
		search_input = request.form['search']
		data = itunes_api.search_album(search_input, 'album', 100)
		if not data:
			error = 'No search results for ' + search_input
	return render_template('index.html', data=data, error=error)

# Info
@app.route('/info')
def show_info():
	info = device_info.all_info()
	return render_template('info.html', info=info)

# Launch server
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)