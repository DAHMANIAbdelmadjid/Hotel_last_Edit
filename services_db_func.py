import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='hotel',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed")


def insert_service(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO service (descp, ser_price, ser_discount) VALUES (%s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("service inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def select_all_services(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM service"
        cursor.execute(query)
        services = cursor.fetchall()
        close_connection(connection)
        service1 = [["Service ID", "Description", "Price", "Discount"], ]
        for service in services:
            service1.append(list(service))
        return service1
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def update_service(connection, ser_id, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE service SET desco=%s, ser_price=%s, ser_discount=%s WHERE ser_id=%s"
        cursor.execute(query, (*new_values, ser_id))
        connection.commit()
        print("Service updated successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def delete_service(connection, ser_id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM service WHERE ser_id=%s"
        cursor.execute(delete_query, (ser_id,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def search_service(connection, service):
    if not service:
        return None

    try:
        cursor = connection.cursor()
        WHERE = ["ser_id", "descp", "ser_price", "ser_discount"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM service WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + service + '%',))
            search_results.extend(cursor.fetchall())
            if search_results:
                break

        if not search_results:
            print("No matching services found.")
        else:
            print("Search Results:")
            return [["Service ID", "Description", "Price", "Discount"]] + [list(service) for service in search_results]

    except Error as e:
        print(f"Error: {e}")
        return None
    close_connection(connection)
