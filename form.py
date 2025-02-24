from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, URLField
from wtforms.validators import DataRequired, URL



# WTForm for creating new Cafe
class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = URLField("Cafe Map URL", validators=[DataRequired(), URL()])
    img_url = URLField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField("Cafe Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets")
    has_toilet = BooleanField("Has Toilet")
    has_wifi = BooleanField("Has WiFi")
    can_take_calls = BooleanField("Can Take Calls")
    seats = StringField("How many seats are there ?", validators=[DataRequired()])
    coffee_price = StringField("☕️ Price", validators=[DataRequired()])
    submit = SubmitField("Submit Cafe")