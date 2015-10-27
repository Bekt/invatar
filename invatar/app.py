import hashlib

import flask as f

from . import (make_app, ApiForm, svg)

# Main app.
app = make_app(__name__)


@app.route('/')
def index():
    return f.render_template('index.html')


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/svg/<ini>', defaults={'ini': ''})
@app.route('/svg/<ini>.jpg')
def initials(ini):
    """Generates a SVG body with the given initials.

    The endpoint optionally accepts the following
    URL parameters (see `ApiForm` for details.):

    :param s: (int) height and width of the output
    :param h: (str) unique identifier for hashing purposes
    :param color: (str) color of the text
    :param bg: (str) comma-separated list of color codes to pick from
                     for the SVG background
    :param font_size: (int) font size of the text
    :param font_family: (str) font family for the text
    """
    @f.after_this_request
    def put_header(response):
        if response.status_code != 400:
            response.headers['Content-Type'] = 'image/svg+xml'
        return response

    form = ApiForm(f.request.args)
    if not form.validate():
        return f.jsonify(error=form.errors), 400
    options = _build_options(ini, form.data)
    body = svg.make_svg(**options)
    return body


def _build_options(text, data):
    """Builds and butters options for the `make_svg` method.

    :return (dict)
    """
    options = {k: v for k, v in data.items() if v}
    options['text'] = text.upper()
    if 's' in options:
        options['size'] = options['s']
    # Background color selection.
    bg_args = {'text': options['text']}
    h = options.get('h', '').strip()
    if h:
        bg_args['h'] = h
    colors = options.get('bg', '').strip().split(',')
    if colors and colors[0]:
        bg_args['colors'] = colors
    options['bg'] = _bg_color(**bg_args)
    return options


def _bg_color(colors=None, text=u'', h=u'salty-salt'):
    """Selects a background color to use.

    If `colors` is given, the value is choosen from that.

    If `colors` is not given, a unique and consistent color value is generated.

    :return (str)
    """
    h = hashlib.md5((h + text).encode('utf-8')).hexdigest()
    if colors:
        ind = int(h, 16) % len(colors)
        return colors[ind]
    cut = 142
    r = int(h[:2], 16) % cut
    g = int(h[2:4], 16) % cut
    b = int(h[4:6], 16) % cut
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
