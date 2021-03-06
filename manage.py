#!/usr/bin/env python

import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_security.utils import encrypt_password

from shell import create_app
from shell.webinterface.extensions import db
from shell.webinterface.models import User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('STYLES_ENV', 'dev')
app = create_app('shell.webinterface.settings.%sConfig' % env.capitalize(), env=env)

def create_app_with_migrate():
    migrate = Migrate(app, db)
    migrate
    return app

manager = Manager(create_app_with_migrate)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


#===============================================================================
# @manager.shell
# def make_shell_context():
#     """ Creates a python REPL with several default imports
#         in the context of the app
#     """
# 
#     return dict(app=app, db=db, User=User)
#===============================================================================

@manager.command
def initdb(nodata=False):
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """
   
    db.drop_all()
    db.create_all()
    
    if not nodata:
        admin = User(
                username=u'admin',
                email=u'admin@example.com',
                password=encrypt_password('password'),
                #role_code=ADMIN,
                active=True)
    
        db.session.add(admin)
        db.session.commit()


if __name__ == "__main__":
    manager.run()