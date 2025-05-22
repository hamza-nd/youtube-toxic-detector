import mysql.connector
from mysql.connector import Error
import os
import re

db_url = os.environ.get("DATABASE_URL")

print(f"DATABASE_URL: {db_url}")

def parse_mysql_url(url):
    # Example: mysql://user:password@host:port/database
    pattern = r"mysql:\/\/(.*?):(.*?)@(.*?):(\d+)\/(.*)"
    match = re.match(pattern, url)
    if not match:
        raise ValueError("Invalid DATABASE_URL format")
    user, password, host, port, database = match.groups()
    return {
        "user": user,
        "password": password,
        "host": host,
        "port": int(port),
        "database": database
    }

def create_connection():
    try:
        if not db_url:
            raise ValueError("DATABASE_URL environment variable not set")
        params = parse_mysql_url(db_url)
        connection = mysql.connector.connect(
            host=params["host"],
            user=params["user"],
            password=params["password"],
            database=params["database"],
            port=params["port"]
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        return None

def create_tables():
    try:
        connection = create_connection()
        if connection is None:
            return
        
        cursor = connection.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                isadmin BOOLEAN DEFAULT FALSE
            )
        """)
        
        # Create scraped_data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scraped_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                videoid VARCHAR(255) NOT NULL,
                title TEXT,
                thumbnail TEXT,
                length VARCHAR(50),
                views INT,
                published DATETIME,
                url TEXT,
                scraped_by INT,
                FOREIGN KEY (scraped_by) REFERENCES users(id)
            )
        """)
        
        connection.commit()
        print("Tables created successfully")
        
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_user(name, username, email, password, isadmin=False):
    try:
        connection = create_connection()
        if connection is None:
            return None
        
        cursor = connection.cursor()
        query = """
            INSERT INTO users (name, username, email, password, isadmin)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, username, email, password, isadmin))
        connection.commit()
        return cursor.lastrowid
        
    except Error as e:
        print(f"Error inserting user: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_scraped_data(videoid, title, thumbnail, length, views, published, url, scraped_by):
    try:
        connection = create_connection()
        if connection is None:
            return None
        
        cursor = connection.cursor()
        query = """
            INSERT INTO scraped_data 
            (videoid, title, thumbnail, length, views, published, url, scraped_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (videoid, title, thumbnail, length, views, published, url, scraped_by))
        connection.commit()
        return cursor.lastrowid
        
    except Error as e:
        print(f"Error inserting scraped data: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_user_by_username(username):
    try:
        connection = create_connection()
        if connection is None:
            return None
        
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone()
        
    except Error as e:
        print(f"Error getting user: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_scraped_data_by_user(user_id):
    try:
        connection = create_connection()
        if connection is None:
            return None
        
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM scraped_data WHERE scraped_by = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
        
    except Error as e:
        print(f"Error getting scraped data: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


