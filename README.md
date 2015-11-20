flask-webhook-server
====================

A server that catches and displays network requests. It will catch all network requests
not sent to the base path. The base path is used to display the network requests with a GET
request, or reset the caught requests with a POST request. This is all available via the UI.

Running the app requires python3 and flask. To run with a virtual envivonment:

```
$ virtualenv -p /usr/bin/python3 venv
$ . venv/bin/activate
$ pip install flask
$ python app.py
```