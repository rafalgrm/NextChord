from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from flask.ext.wtf import Form
from wtforms import TextField, ValidationError, BooleanField,\
	SubmitField, SelectField, FormField, validators
from wtforms.validators import Required

available_models = ['model1', 'model2'] 

class ExampleForm(Form):
    model = SelectField(u"Model Field", choices=[(m, m) for m in available_models],
    	description='dropdown z wyborem gotowego wytrenowanego modelu z melody rnn')

    workspace = TextField('Workspace Field', description='wybor workspace',
                       validators=[Required()])
    checkbox_field = BooleanField('jakies kontorlki od podstaowwej konfiguracji',
                                  description='Checkbox description')

    submit_button = SubmitField('Generuj')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = ExampleForm()
        form.validate_on_submit()  # to get error messages to the browser
        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
