from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange

class RegisterForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField('CONFIRM PASSWORD', validators=[EqualTo('password')])
    submit = SubmitField('REGISTER')


class LoginForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired()])
    password = PasswordField('PASSWORD', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('LOGIN')

class ProductForm(FlaskForm):
    category = SelectField('Pick a category', validators=[DataRequired()], choices=[('Pick a category'), ('Dairy'), ('Breadstuff'), ('Meat'), ('Fruit'), ('Vegetable'), ('Drink'), ('Grain'), ('Pasta'), ('Honey'), ('Nuts'), ('Fats'), ('Misc'), ('Made')])
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    maker = StringField('Maker', validators=[Length(max=30)])
    proteins = FloatField('Proteins', validators=[DataRequired(), Length(max=10)])
    carbo = FloatField('Carbohydrates', validators=[DataRequired(), Length(max=10)])
    fats = FloatField('Fats', validators=[DataRequired(), Length(max=10)])
    kcal = FloatField('Kcal', validators=[DataRequired(), Length(max=10)])


class MealForm(FlaskForm):
    category = SelectField('Pick a category', validators=[DataRequired()], choices=[('Pick a category'), ('Dairy'), ('Breadstuff'), ('Meat'), ('Fruit'), ('Vegetable'), ('Drink'), ('Grain'), ('Pasta'), ('Honey'), ('Nuts'), ('Fats'), ('Misc'), ('Made')])
    name = SelectField('Name', validators=[DataRequired()], coerce=int) #coerce potrzebny do dynamic data
    weight = FloatField('Weight [g]/Volume [ml]', validators=[DataRequired()])
        # class UserDetails(Form):
        #     group_id = SelectField(u'Group', coerce=int)

        # def edit_user(request, id):
        #     user = User.query.get(id)
        #     form = UserDetails(request.POST, obj=user)
        #     form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]