class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_ECHO = False

    CACHE_TYPE = 'simple'

    # This allows us to test the forms from WTForm
    WTF_CSRF_ENABLED = False
    #SEND_EMAIL = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_LOGIN_USER_TEMPLATE = 'user/log_in.html'
    SECURITY_REGISTER_USER_TEMPLATE = 'user/register_user.html'
    SECURITY_FORGOT_PASSWORD_TEMPLATE = 'user/forgot_password.html'
    SECURITY_RESET_PASSWORD_TEMPLATE = 'user/reset_password.html'
    # This needs to be set to implement verification code
    SECURITY_POST_REGISTER_VIEW = '/'
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_POST_LOGOUT_VIEW = '/'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email', 'username']
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = '4f1WQbWEKMPv9S7p'
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = False
    #SECURITY_CHANGE_URL = '/change_password'
    #SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    
    SOCIAL_TWITTER = {
        'consumer_key': 'twitter consumer key',
        'consumer_secret': 'twitter consumer secret'
    }
    
    SOCIAL_FACEBOOK = {
        'consumer_key': 'twitter consumer key',
        'consumer_secret': 'twitter consumer secret'
    }