from DateTime import DateTime as dt
from random import randint as RI
import pyodbc

# Get the range of ids from customers table
# Decide on a date range for the project.  2 years.
# Decide on a range of visits per day.  Coffee shop.  200-500
# Make a set of customer visits that iterates through the dates of the date range
#   and generates 'visits' which are dates associated with customer IDs. 
# make_table_if_new() with arg (as dictionary) for colums
# Add those values to the table

if __name__ == "__main__":
    connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=GANDHARA\SQLEXPRESS;'
                            'Database=TestDB;'
                            'Trusted_Connection=yes;')