from flask import Flask, render_template
from config import Config

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(Config)

class TextForm(FlaskForm):
	textform = StringField('cards', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def builder():
	form = TextForm()
	return render_template('home.html', title='Submission', form=form)


@app.route('/spellbook', methods=['POST'])
def spellbook():
	return "spellbook built!"


if __name__ == '__main__':
	app.run()