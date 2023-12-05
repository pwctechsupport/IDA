from flaskwebgui import FlaskUI
from Python.wsgi import application
FlaskUI(app=application,server='django').run()