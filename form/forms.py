from flask.ext.wtf import Form

from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
#from import  

class testForm(Form):
    building = BooleanField("building")
	#building = True
    grass = BooleanField("grass")
    lng = FloatField("lng")
    lat = FloatField("lat")
    zoom = FloatField("zoom")
