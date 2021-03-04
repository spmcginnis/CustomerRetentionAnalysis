import names
from random import randint as RI
import pyodbc  #(ODBC = Open DataBase Connectivity standard)
# sqlalchemy (SQL abstraction toolkit with optional ORM)

class Person:
    def __init__(self, given, family, gender, age):
        self.given = given
        self.family = family
        self.gender_value = gender
        self.age = age
        
    def to_string(self):
        return f"'{self.given}', '{self.family}', '{self.gender_value}', {self.age}"

def generate_random_name():
    rand_int = RI(0,1)
    gender_value = "" # this should be its own method
    if (rand_int%2 == 0):
        gender_value = "female"
    else:
        gender_value = "male"
    
    given = names.get_first_name(gender=gender_value)
    family = names.get_last_name()
    age =  str(RI(1,100))
    
    person = Person(given, family, gender_value, age)
    return person.to_string()

def make_customer_list(num_customers=100):
    return list(map(lambda n : generate_random_name(), range(num_customers)))
    
    # return list(map(generate_random_name, range(num_customers)))

# range(num_customers) is returning a list of numbers of size num_customers
# map(function_name, range(list_size)) is iterating over the list given in the second argument and executing the function with one argument, that argument being the value of the list at current position
# generate_random_name is now a function from int n that returns a comma delimited string of the customer data

# Generate SQL command as string
# TODO feed the column names in as args
def customer_list_to_sql(customer_list, table_name):
    command = f"INSERT INTO {table_name} (given_name, family_name, gender, age) VALUES "
    value_array = []
    # INSERT INTO table_name (column1, column2, column3, ...)
    # VALUES (value1, value2, value3, ...);
    
    for customer in customer_list:
        value_array.append("(" + customer + ")")
    
    output = command + ",".join(value_array)
    return output

# Check if a certain table exists and if it doesn't make it
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
                           customer_id int IDENTITY (1,1) NOT NULL,
                           CONSTRAINT PK_{table_name}_customer_id PRIMARY KEY CLUSTERED (customer_id),
                           given_name NVARCHAR(50),
                           family_name NVARCHAR(50),
                           gender NCHAR(10),
                           age INT
                       )
                       ''')
        connection.commit()

# Add list of customers to table
# TODO feed the column names in as args and pass them to the function calls, once they are set to receive them
def add_customer_list_to_table(table_name, connection):
    make_table_if_new(table_name, connection)
    cursor = connection.cursor()
    customer_list = make_customer_list(1000)
    cursor.execute(customer_list_to_sql(customer_list, table_name))
    connection.commit()

if __name__ == "__main__":
# Order of operations:
#   1. Open a connection to the database
#   2. Run the sql command process as many times as is needed
#   3. Close the connection (pyodbc does this automatically when connection or cursor are deleted, upon leaving scope)

    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=GANDHARA\SQLEXPRESS;'
                                'Database=TestDB;'
                                'Trusted_Connection=yes;')
    
    add_customer_list_to_table("customers", connection)