from flask.globals import request
from flask.templating import render_template
import subprocess

from data.main_form import MainForm
from flask import Blueprint


main = Blueprint('main', __name__)


@main.route('/', methods=('GET', 'POST'))
def index():
    form = MainForm()
    if request.method == 'POST':
        pass
    form.validate_on_submit()  # to get error messages to the browser
    return render_template('index.html', form=form)


