from .meta import db
from datetime import datetime

doors_employees = db.Table(
    'doors_employees',
    db.Column('door_id', db.Integer(), db.ForeignKey('door.id'), index=True),
    db.Column('employee_id', db.Integer(), db.ForeignKey('employee.id'), index=True)
)


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    nickname = db.Column(db.String())

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    door_id = db.Column(db.Integer, db.ForeignKey('door.id'))
    created = db.Column(db.DateTime, default=datetime.now())
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee = db.relationship('Employee')
    door = db.relationship('Door')

    def __repr__(self):
        return '{employee}:{door}:{store}'.format(
            employee=self.employee,
            door=self.door,
            store=self.door.store,
        )


class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name


class Door(db.Model):
    __tablename__ = 'door'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    store = db.relationship('Store', backref='doors', lazy='joined')
    employees = db.relationship('Employee', secondary=doors_employees,
                            backref=db.backref('doors', lazy='dynamic'))

    def __repr__(self):
        return self.name