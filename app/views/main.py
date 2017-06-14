from flask.globals import request
from flask.templating import render_template
import subprocess
import shlex

from data.main_form import MainForm
from flask import Blueprint


main = Blueprint('main', __name__)

def make_config(model):
	return '/Users/fib1123/Desktop/cognitive/NextChord/app/models/' + model + ".mag"

def make_command(model, outputs_number, steps, primer_melody):
    return 'melody_rnn_generate --config={} \
    --bundle_file={} \
    --output_dir=out \
    --num_outputs={} \
    --num_steps={} \
    --primer_melody={}'.format("'" + model + "'", make_config(model), outputs_number, steps, '"' + primer_melody + '"')

@main.route('/', methods=('GET', 'POST'))
def index():
    form = MainForm()
    if request.method == 'POST':
        
        model = request.form["model"]
        outputs_number = request.form["outputs_number"]
        steps = request.form["steps"]
        primer_melody = request.form["primer_melody"]

        print model, outputs_number, steps, primer_melody

        command = make_command(model, outputs_number, steps, primer_melody)
        print command
        subprocess.call(shlex.split(command))        

    form.validate_on_submit()  # to get error messages to the browser
    return render_template('index.html', form=form)


