import mysql.connector


def create_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database if it doesn't already exist.
    Prints a success message or an error message on failure.
    """
    connection = None
    cursor = None
    try:
        # Establish connection (no database specified)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == '__main__':
    create_database()
