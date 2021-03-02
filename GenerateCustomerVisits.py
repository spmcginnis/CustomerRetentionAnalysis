from datetime import date, timedelta
from random import randint as RI
import pyodbc

# Get the range of ids from customers table
# Decide on a range of visits per day.  Coffee shop.  200-500
# Make a set of customer visits that iterates through the dates of the date range
#   and generates 'visits' which are dates associated with customer IDs. 
# make_table_if_new() with arg (as dictionary) for colums
# Add those values to the table
# Do I need to give the customers table a primary key or is it automatically generated?

visits = 0


def get_random_customer_id(connection, table_name):
    # TODO get random customer_id from existing DB
    return RI(0,10000) # TEMP placeholder

# Returns a list of strings
def generate_visits_over_date_range(first, last, min, max):
    customer_visits = []
    
    while first <= last:
        current_date = first.strftime("%Y-%m-%d")
        visits = RI(min, max)
        
        for visit in range(0, visits):
            customer_id = get_random_customer_id('temp', 'temp')
            customer_visits.append(f"{current_date}, {customer_id}")
        
        first += timedelta(days=1)
        
    return customer_visits


if __name__ == "__main__":
    connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=GANDHARA\SQLEXPRESS;'
                            'Database=TestDB;'
                            'Trusted_Connection=yes;')
    
    print(generate_visits_over_date_range(date(2018,1,1), date(2019,12,31), 3, 5))
    
    # TEMP # TESTING
    # cursor = connection.cursor()
    # print(cursor.primaryKeys("customers").description)