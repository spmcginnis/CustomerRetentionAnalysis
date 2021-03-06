import pyodbc

def get_table_names(connection):
    cursor = connection.cursor()
    command = '''
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='TestDB'
    '''
    table_names = []
    for item in cursor.execute(command).fetchall():
        table_names.append(item[0])
    return table_names

def drop_tables(connection, table_names):
    cursor = connection.cursor()

    if type(table_names) == str:
        table_names = [table_names]    
    for table_name in table_names:
        command = f'''
            DROP TABLE {table_name}
            '''
        cursor.execute(command).commit()

# Doesn't work this simply because of FK constraints.
# def drop_all_tables(connection):
#     cursor = connection.cursor()
#     table_names = get_table_names(connection)
#     drop_tables(connection, table_names)

if __name__ == "__main__":
    connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=GANDHARA\SQLEXPRESS;'
                            'Database=TestDB;'
                            'Trusted_Connection=yes;')
    
    drop_tables(connection, 'customer_visits')
    