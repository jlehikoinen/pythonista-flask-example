# Pythonista Flask example

Little Flask app that demonstrates iTunes Search API and Pythonista Objective-C APIs in iOS. You can also run the iTunes Search API example on macOS by switching to macos branch.

## macOS Requirements

* virtualenv

## macOS Setup

Clone this repo:

`$ git clone https://github.com/jlehikoinen/pythonista-flask-example.git`

`$ cd pythonista-flask-example`

Switch to `macos` branch:

`$ git checkout macos`

Setup virtualenv:

`$ virtualenv flask`

`$ source flask/bin/activate`

`$ pip install flask`

`$ pip install requests`

## macOS Usage

Run Flask server:

`$ python flask_server.py`

Open `http://localhost:5000` URL in macOS web browser.

After testing, exit virtualenv:

`$ deactivate`