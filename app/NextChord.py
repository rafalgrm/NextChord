from flask import Flask
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig

# blueprints
from views.main import main


def create_app(configfile=None):

    app = Flask(__name__)

    # registering blueprints
    app.register_blueprint(main)

    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
    # highly recommend =)
    # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    return app


app = None
if __name__ == '__main__':
    app = create_app().run(debug=True)
