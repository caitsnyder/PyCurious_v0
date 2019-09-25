import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY	') or 'set-pre-deploy'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Come back to this after compartmentalizing sensitive data
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('pycuriousblog')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	ADMINS = os.environ.get('ADMINS')
	MS_TRANSLATOR_KEY = os.environ.get('MAIL_SERVER')
	LANGUAGES = ['en','fr']
	COMMENTS_PER_PAGE = 25