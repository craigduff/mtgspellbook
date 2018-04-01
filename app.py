from flask import Flask, flash, render_template, redirect, request
from config import Config
import json
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(Config)

class TextForm(FlaskForm):
	textform = TextAreaField('cards', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def builder():
	form = TextForm()
	if request.method == 'POST':
		return request.form.to_dict(flat=False)['textform'][0]
		redirect('home.html')
	return render_template('home.html', title='Submission', form=form)


@app.route('/spellbook')
def spellbook():
	return "spellbook built!"


if __name__ == '__main__':
	app.run()