import flask
from flask import Flask
blueprint = flask.Blueprint(__name__, __name__)

@blueprint.route('/test', methods=['post', 'get'])
def test():
	return flask.render_template('mymap.html')	
	
