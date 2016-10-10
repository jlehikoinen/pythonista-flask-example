# Pythonista Flask example

Little Flask app that demonstrates iTunes Search API and Pythonista Objective-C APIs.

## Requirements

* Pythonista (iOS)

## Setup

Create a new Empty Script in Pythonista to Documents root. Copy & paste [this Gist](https://gist.github.com/jlehikoinen/ebbb77b366d908243ad6).

The setup script will download a simple Pypi package installer script, Flask pkgs install script and this Git repo as a zip file and will extract the zip file.

Note: the setup script will overwrite existing `pythonista-flask-example` folder if it exists.

1. Run setup script

2. Install Flask packages by running run `install_flask_pkgs.py` in `site-packages` folder

## Usage

Run `flask_server.py` in `pythonista-flask-example` folder

Open `http://localhost:5000` URL in iOS web browser

## macOS Setup (optional)

Clone this repo:

`$ git clone https://github.com/jlehikoinen/pythonista-flask-example.git`

`$ cd pythonista-flask-example`

Setup virtualenv:

`$ virtualenv flask`

`$ source flask/bin/activate`

`$ pip install flask`

`$ pip install requests`

Run Flask server:

`$ python flask_server.py`

Open `http://localhost:5000` URL in macOS web browser

** Note that Pythonista Objective-C APIs in "Info" tab doesn't work in macOS **

After testing, exit virtualenv:

`$ deactivate`
