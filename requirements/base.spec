# To rebuild the .pin file, do the following:
#
#     pip install pip-tools
#     pip-compile --rebuild -o requirements/base.pin requirements/base.spec

alembic>=1.8
appdirs>=1.4.4
Flask>=2.2
Flask-SQLAlchemy>=2.5.1
flask-cors>=3.0.10
flask-httpauth>=4.7.0
flask-limiter>=2.6
PyYAML>=6.0
jsonschema>=4.17
requests>=2.28
SQLAlchemy>=1.4
waitress>=2.1
WTForms>=3.0

# Just here as constraints -- not directly used.
greenlet>=2.0.0a2  # 2.x needed for Python 3.11 compat
