from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField("Grocery Title", 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your Grocery Title needs to be between 3 and 80 characters.")
        ])
    address = StringField("Address", validators=[
        DataRequired(),
        Length(min=3, max=80, message="Your Address needs to be between 3 and 80 characters.")
    ])
    submit = SubmitField("Submit")

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField("Item Name", 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your Item Name needs to be between 3 and 80 characters.")
        ])
    price = FloatField("Price", 
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Price must be a positive number.")
        ])
    category = SelectField("Category",
        choices=[(choice.name, choice.value) for choice in ItemCategory],
        validators=[
            DataRequired()
        ])
    photo_url = StringField("Photo URL", validators=[
        DataRequired(),
        URL(message="Please enter a valid URL.")
    ])
    store = QuerySelectField("Store", query_factory=lambda: GroceryStore.query.all(), allow_black=False, get_label="title")
    submit = SubmitField("Submit")
