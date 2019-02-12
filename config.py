import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # General app settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'
    UPLOAD_FOLDER = 'app/tmp'
    MAX_CONTENT_LENGTH = 32 * 1024 * 1024
    DOWNLOAD_DIR = 'tmp'
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    TESTING = int(os.environ.get('TESTING')) or False
