from allure_commons._allure import step


@step
def create_group(db, values):
    query = "INSERT INTO auth_group(name) VALUES (%s)"
    db.execute(query, values)
    return db.connection.commit()


@step
def get_group_name(db):
    query = "SELECT name FROM auth_group"
    db.execute(query)  # вот так return db.execute(query).fetchall() - не работает
    return db.fetchall()
