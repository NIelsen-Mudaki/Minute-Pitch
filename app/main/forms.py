from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Post')