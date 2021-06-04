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

* Python 3 installed (including venv)

## macOS Setup

Clone this repo:

`$ git clone https://github.com/jlehikoinen/pythonista-flask-example.git`

`$ cd pythonista-flask-example`

Switch to `macos` branch:

`$ git checkout macos`

Setup venv:

`$ python3 -m venv flask`

`$ source flask/bin/activate`

`$ pip3 install flask`

`$ pip3 install requests`

## macOS Usage

Run Flask server:

`$ python3 flask_server.py`

Open `http://localhost:5000` URL in macOS web browser.

After testing, exit virtualenv:

`$ deactivate`

## macOS TLS tests

Switch to `tls` branch:

`$ git checkout tls`

Install `certs/hoax.fi Root CA Certificate.mobileconfig` config profile.

Setup venv:

`$ python3 -m venv flask`

`$ source flask/bin/activate`

`$ pip3 install --upgrade pip`

`$ pip3 install flask`

`$ pip3 install requests`

`$ pip3 install pyopenssl`

Run Flask server with cert parameters:

`$ python3 flask_server.py certs/300/300.hoax.fi.crt certs/300/300.hoax.fi.key`

Add `<my ip address> 300.hoax.fi` to `/etc/hosts`.

Open `https://300.hoax.fi` URL in macOS web browser.