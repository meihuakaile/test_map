import flask
from flask import Flask
import form.forms as forms

blueprint = flask.Blueprint(__name__, __name__)

@blueprint.route('/back', methods=('POST', 'GET'))
def back ():
    form = forms.testForm()
    return "sucess"+ " " + str(form.building.data) + str(form.zoom.data)+ str(form.grass.data)+ str(form.lng.data) + str(form.lat.data) 

@blueprint.route('/test', methods=('post', 'get'))
def test ():
    
    form = forms.testForm()
    print "two"
    if form.validate_on_submit():
        print "one"
        return "sucess"+ " " + str(form.building.data) + str(form.zoom.data)+str(form.grass.data) + str(form.lng.data) + str(form.lat.data)
    return flask.render_template('mymap.html', form=form)
	
