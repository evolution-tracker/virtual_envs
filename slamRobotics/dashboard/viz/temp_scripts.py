from django.db import connection

def my_custom_sql(self):
    cursor = connection.cursor()

    cursor.execute("Select * from pipes", [self.baz])

    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    return row