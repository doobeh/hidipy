from hidipy.models import Store, db
from datetime import datetime
import time


def load_stores():
    t0 = time.time()

    iga = Store(name='IGA')
    gg = Store(name='Gourmet')
    smart = Store(name='Smart')

    db.session.add_all([iga, gg, smart])
    db.session.commit()
    print("Total time for Store loading: {} sec".format(
        time.time() - t0)
    )
