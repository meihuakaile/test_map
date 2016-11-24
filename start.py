#!/usr/bin/env python
from __future__ import absolute_import

import flask
from flask import Flask
app =  Flask(__name__)
blueprint = flask.Blueprint(__name__, __name__) 

if __name__ == "__main__":
    app.debug = True
    import view.views
    app.register_blueprint(view.views.blueprint)
    app.run(host="0.0.0.0")
