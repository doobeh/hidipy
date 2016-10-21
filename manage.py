from flask_script import Manager, Shell
from hidipy.models import User, Role, Log, Store, Door, Employee, db
from hidipy.core import app
import loader

def _make_context():
    return dict(
        app=app, db=db,
        User=User, Role=Role,
        Door=Door, Log=Log, Store=Store, Employee=Employee
    )

manager = Manager(app)
manager.add_command('shell', Shell(make_context=_make_context))

@manager.command
def nuke():
    db.drop_all()
    db.create_all()


@manager.command
def populate():
    nuke()
    roles = [
        Role(name='admin'),
    ]

    db.session.add_all(roles)
    loader.load_users()
    loader.load_stores()
    db.session.commit()


if __name__ == '__main__':
    manager.run()