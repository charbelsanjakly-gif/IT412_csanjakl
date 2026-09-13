"""database module - MariaDB connection and customer management.

This module provides database operations for the IT 412 Final Project,
handling customer data storage and retrieval from a MariaDB database.
"""
import pymysql
from classes.customer import Customer

class Database:
    """Database class for managing customer records in MariaDB.
    
    Attributes:
        connection: PyMySQL connection object to the database
        cursor: Database cursor for executing SQL queries
    """
    
    def __init__(self):
        """Initialize database connection to IT412_final database.
        
        Raises:
            pymysql.Error: If connection to database fails
        """
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='IT412_final'
        )
        self.cursor = self.connection.cursor()
    
    def add_customer(self, customer):
        """Add a customer to the database.
        
        Args:
            customer (Customer): A Customer object with validated fields
            
        Returns:
            None
            
        Raises:
            Exception: If database insert fails
        """
        try:
            sql = "INSERT INTO customers (first_name, last_name, company_name, address, city, county, state, zip_code, phone1, phone2, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (customer.first_name, customer.last_name, customer.company_name, customer.address, customer.city, customer.county, customer.state, customer.zip_code, customer.phone1, customer.phone2, customer.email))
            self.connection.commit()
        except Exception as e:
            print(f"Error adding customer: {e}")
    
    def get_all_customers(self):
        """Retrieve all customers from the database.
        
        Returns:
            list: List of Customer objects, empty list if none exist
            
        Raises:
            Exception: If database query fails
        """
        try:
            sql = "SELECT * FROM customers"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            customers = []
            for row in results:
                customer = Customer(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                customers.append(customer)
            return customers
        except Exception as e:
            print(f"Error getting customers: {e}")
            return []
    
    def get_customer_by_index(self, index):
        """Retrieve a single customer by list index.
        
        Args:
            index (int): The position in the customer list
            
        Returns:
            Customer: Customer object if found, None otherwise
        """
        customers = self.get_all_customers()
        if 0 <= index < len(customers):
            return customers[index]
        return None
    
    def update_customer(self, index, customer):
        """Update an existing customer record.
        
        Args:
            index (int): The position of the customer to update
            customer (Customer): Updated Customer object
            
        Returns:
            None
            
        Raises:
            Exception: If database update fails
        """
        customers = self.get_all_customers()
        if 0 <= index < len(customers):
            old_customer = customers[index]
            sql = "UPDATE customers SET first_name=%s, last_name=%s, company_name=%s, address=%s, city=%s, county=%s, state=%s, zip_code=%s, phone1=%s, phone2=%s, email=%s WHERE first_name=%s AND last_name=%s AND email=%s"
            self.cursor.execute(sql, (customer.first_name, customer.last_name, customer.company_name, customer.address, customer.city, customer.county, customer.state, customer.zip_code, customer.phone1, customer.phone2, customer.email, old_customer.first_name, old_customer.last_name, old_customer.email))
            self.connection.commit()
    
    def delete_customer(self, index):
        """Delete a customer from the database.
        
        Args:
            index (int): The position of the customer to delete
            
        Returns:
            None
            
        Raises:
            Exception: If database delete fails
        """
        customers = self.get_all_customers()
        if 0 <= index < len(customers):
            customer = customers[index]
            sql = "DELETE FROM customers WHERE first_name=%s AND last_name=%s AND email=%s"
            self.cursor.execute(sql, (customer.first_name, customer.last_name, customer.email))
            self.connection.commit()
    
    def clear_all(self):
        """Clear all customers from the database.
        
        Returns:
            None
            
        Raises:
            Exception: If database clear fails
        """
        try:
            sql = "DELETE FROM customers"
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f"Error clearing customers: {e}")
    
    def get_customer_count(self):
        """Get total number of customers in database.
        
        Returns:
            int: Number of customers, 0 if error
            
        Raises:
            Exception: If database query fails
        """
        try:
            sql = "SELECT COUNT(*) FROM customers"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Error getting count: {e}")
            return 0
    
    def close(self):
        """Close the database connection.
        
        Returns:
            None
        """
        self.connection.close()
