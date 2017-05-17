from flask.ext.wtf.form import Form
from wtforms.fields.core import SelectField, StringField, BooleanField, IntegerField
from wtforms.fields.simple import TextField, SubmitField
from wtforms.validators import Required, DataRequired, ValidationError

from data.pretrained_models import pretrained_models_list


class MainForm(Form):

    model = SelectField(u"Model Field", choices=[(m,str(m)) for m in pretrained_models_list],
                        description='dropdown z wyborem gotowego wytrenowanego modelu z melody rnn')

    # workspace = StringField('Workspace Field', description='wybor workspace',
    #                       validators=[DataRequired()])

    outputs_number = IntegerField('Number of outputs')
    steps = IntegerField('Number of steps')
    primer_melody = IntegerField('Primer melody')

    submit_button = SubmitField('Generuj')

