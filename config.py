import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = (os.environ.get('SECRET_KEY') or 'anime-greasily6-justice-bacon-skimming-chloride-repacking-greeter')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
