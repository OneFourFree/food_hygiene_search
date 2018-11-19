from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    postcode = StringField('Post Code',
                           validators=[DataRequired(), Length(min=4, max=7)],
                           render_kw={"placeholder": "IG1 1JF"})
    submit = SubmitField('Search')