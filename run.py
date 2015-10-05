"""Main WSGI module.

To run:
    python run.py
-or-
    gunicorn run:app
"""

from invatar.app import app


if __name__ == '__main__':
    app.run(debug=True)
