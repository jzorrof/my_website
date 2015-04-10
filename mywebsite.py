__author__ = 'Fanzhong'

from flask import Flask, render_template

app = Flask(__name__)

'''
This is my website index
I'll create my website from now
data: 2015.04.10
'''
@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)