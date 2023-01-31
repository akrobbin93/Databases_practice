import sqlalchemy as db

engine = db.create_engine('sqlite:///Users.db')

connection = engine.connect()

metadata = db.MetaData()

users = db.Table('Users', metadata, db.Column('user_id', db.Integer),
                                    db.Column('First Name', db.Text),
                                    db.Column('Last Name', db.Text),
                                    db.Column('Email', db.Text))

metadata.create_all(engine)

insert_query = users.insert().values(
                [(1, 'Bob', 'Smith', 'bsmith@gmail.com'),
                (2, 'Jane', 'Smith', 'jsmith@gmail.com'),
                (3, 'Alan', 'Smith', 'asmith@gmail.com'),
                (4, 'Ethan', 'Smith', 'esmith@gmail.com'),
                (5, 'Ryan', 'Smith', 'rsmith@gmail.com')])
connection.execute(insert_query)

selection = db.select([users.columns.Email])
selection_result = connection.execute(selection)

print(selection_result.fetchall())
