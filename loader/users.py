from hidipy.models import User, Role, db
from datetime import datetime
import time


def load_users():
    t0 = time.time()
    dt = datetime.now()
    admin = Role.query.filter_by(name='admin').first()

    if not admin:
        raise ValueError('Admin Role Missing!')

    default_users = [
        'anthony',
        'labrant'
    ]

    for entry in default_users:
        user_entry = User(
            username=entry,
            confirmed_at=dt,
            password='password',
            active=True
        )
        user_entry.roles = [admin]
        db.session.add(user_entry)

    db.session.commit()
    print("Total time for user loading: {} sec".format(
        time.time() - t0)
    )
