from flask import Flask
app = Flask(__name__)


@app.route('/')
def builder():
	return "hello world"


@app.route('/spellbook')
def spellbook():
	return "spellbook built!"


if __name__ == '__main__':
	app.run()