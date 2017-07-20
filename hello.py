from flask import Flask, render_template
from flask.ext.script import Manager 
app = Flask(__name__)
manager = Manager(app)

@app.route("/<name>")
def hello(name):
	return render_template('index.html', name=name)

@app.route("/")
def index():
	return "<h1>GOOD<h1>"

@manager.command
def dev():
	from livereload import Server 
	app.debug = True
	live_server = Server(app.wsgi_app)
	live_server.watch('**/*.*')
	live_server.serve()


if __name__ == '__main__':
    manager.run()
