from datetime import date, timedelta
from random import randint as RI
import pyodbc

# Get the range of ids from customers table
# Decide on a range of visits per day.  Coffee shop.  200-500
# Make a set of customer visits that iterates through the dates of the date range
#   and generates 'visits' which are dates associated with customer IDs. 
# make_table_if_new() with arg (as dictionary) for colums
# Add those values to the table

visits = 0


def get_random_customer_id(connection, table_name):
    # TODO get random customer_id from existing DB
    customer_id = 0
    return customer_id

# Returns a list of strings
def generate_visits_over_date_range(first, last, min, max):
    customer_visits = []
    
    while first <= last:
        current_date = first.strftime("%Y-%m-%d")
        visits = RI(min, max)
        
        for visit in range(0, visits):
            customer_id = RI(0,10000) # TEMP placeholder for get_random_customer_id(connection, table_name)
            customer_visits.append(f"{current_date}, {customer_id}")
        
        first += timedelta(days=1)
        
    return customer_visits

# TODO feed the column names in as args
def make_table_if_new(table_name, connection):
    cursor = connection.cursor()
    if cursor.tables(table=table_name, tableType='TABLE').fetchone():
        print(f"Warning: {table_name} already exists. No changes were commited.")
    else:
        print(f"Creating table name {table_name}")

        # Creating a primary key:
        # https://docs.microsoft.com/en-us/sql/relational-databases/tables/create-primary-keys?view=sql-server-ver15
        cursor.execute(f'''
                        CREATE TABLE {table_name}
                        (
                            visit_id int IDENTITY (1,1) NOT NULL,
                            customer_id int NOT NULL,
                            CONSTRAINT PK_{table_name}_visit_id PRIMARY KEY CLUSTERED (visit_id),
                            CONSTRAINT FK_{table_name}_customer_id FOREIGN KEY (customer_id)
                                REFERENCES customers (customer_id)
                                ON DELETE CASCADE
                                ON UPDATE CASCADE,
                            date datetime
                        )
                       ''')
        connection.commit()

if __name__ == "__main__":
    connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=GANDHARA\SQLEXPRESS;'
                            'Database=TestDB;'
                            'Trusted_Connection=yes;')
    
    make_table_if_new("customer_visits", connection)
    
    print(generate_visits_over_date_range(date(2018,1,1), date(2019,12,31), 3, 5))
    
    # TEMP # TESTING
    # cursor = connection.cursor()
    # print(cursor.primaryKeys("customers").description)