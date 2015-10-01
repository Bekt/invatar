import flask as f
import wtforms as wt
from wtforms import validators as vdr

from flask_cache import Cache
from flask_wtf import Form


# Adjust cache type if not running on App Engine.
cache = Cache(config={'CACHE_TYPE': 'gaememcached'})


def make_app(name):
    """Creates a Flask application."""
    app = f.Flask(__name__)
    app.config.from_object('invatar.configs')
    cache.init_app(app)
    return app


class ApiForm(Form):
    """API request model."""
    s = wt.IntegerField('Size', [vdr.Optional(),
                                 vdr.NumberRange(min=10, max=2000)])
    h = wt.StringField('Identifier', [vdr.Optional()])
    font_size = wt.IntegerField('Font size', [vdr.Optional(),
                                              vdr.NumberRange(min=5, max=1000)])
    font_family = wt.StringField('Font family', [vdr.Optional()])
    bg = wt.StringField('Background colors', [vdr.Optional()])
    color = wt.StringField('Text color', [vdr.Optional()])
