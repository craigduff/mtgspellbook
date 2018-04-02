from flask import Flask, flash, render_template, redirect, request
from config import Config
import json
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import StringIO


app = Flask(__name__)
app.config.from_object(Config)

class TextForm(FlaskForm):
	textform = TextAreaField('cards', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def builder():
	form = TextForm()
	if request.method == 'POST':
		cards = []
		failed_to_find = []
		input = StringIO.StringIO(request.form.to_dict(flat=False)['textform'][0])
		for line in input:
			# check if card is real
			# if found, put in cards
			# else put in failed_to_find
		return input
		redirect('home.html')
	return render_template('home.html', title='Submission', form=form)


@app.route('/spellbook')
def spellbook():
	return "spellbook built!"


if __name__ == '__main__':
	app.run()