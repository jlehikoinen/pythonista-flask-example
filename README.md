# Pythonista Flask example

Little Flask app that demonstrates iTunes Search API and Pythonista Objective-C APIs in iOS. You can also run the iTunes Search API example on macOS by switching to `macos` branch.

## iOS Requirements

* Pythonista 3

## iOS Setup

Create a new Empty Script in Pythonista to Documents root. Copy & paste [this Gist](https://gist.github.com/jlehikoinen/ebbb77b366d908243ad6).

The setup script will download this Git repo as a zip file and will extract the zip file.

Note: the setup script will overwrite existing `pythonista-flask-example` folder if it exists.

Run setup script.

## iOS Usage

Run `flask_server.py` in `pythonista-flask-example` folder.

Open `http://localhost:5000` URL in iOS web browser.

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
