#!/usr/bin/env python
from __future__ import absolute_import

import flask
from flask import Flask
import os
app =  Flask(__name__)
blueprint = flask.Blueprint(__name__, __name__) 

if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = os.urandom(12).encode('hex')
    #import view.views
    import myview
    app.register_blueprint(myview.blueprint)
	#app.register_blueprint(myview.blueprint)
    app.run(host="0.0.0.0")
