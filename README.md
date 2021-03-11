# Customer Retention Analysis Project for Practicing SQL
The goal is to practice SQL in the context of Customer Retention Analysis for an imaginary coffee shop.

## TODO
- Customer Retention Analysis  
- Simple retention curve
- Week-to-week customer retention
- Cohort tables
- Extend data generation code to work with Postgres
- Data analysis leg
- Explore variations in the way customer data is randomized and selected

## Complete
- GenerateCustomers makes a list of sample customers  
- GenerateCustomers constructs a SQL statement to add the customers to a table  
- GenerateCustomers checks to see if a table exists and adds one if it does not exist  
- GenerateCustomers connects to the local DB and executes the SQL command
- Generate sample customer visit data
- Methods to delete tables for easy project iteration
- Template for display created (HTML5 with Bootstrap)  

## Files: Data Generation
GenerateCustomers.py
- Methods to generate n number of random customers and add them to a local SQLServer DB instance.

GenerateCustomerVisits.py
- Methods to generate visits over a given date range.

DeleteTables.py
- Methods to delete tables by name, for quick iteration
- Note: does not delete constraints, so a table with a FK can't be deleted until the FK home table is deleted.

## Files: Data Analysis