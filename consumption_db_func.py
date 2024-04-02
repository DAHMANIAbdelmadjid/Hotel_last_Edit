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

def insert_consum(connection,*values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO consumption (cnt, ser_id, c_id) VALUES (%s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("Consumption inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)

def select_all_consum(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                consumption.cons_id ,
                service.ser_id ,
                service.descp,
                consumption.cnt,
                client.c_id,
                client.c_name
            FROM
                consumption 
            JOIN
                service  ON consumption.ser_id = service.ser_id
            JOIN
                client ON consumption.c_id = client.c_id;
        """
        cursor.execute(query)
        consums = cursor.fetchall()
        close_connection(connection)

        consum1 = [
            ["Consumption ID", "Service ID", "Description", "Count", "Client ID", "Client name"],
        ]
        for consum in consums:
            consum1.append(list(consum))
        return consum1
    except Error as e:
        print(f"Error: {e}")

def update_consum(connection, cons_id, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE consumption SET cnt=%s, ser_id=%s, c_id=%s WHERE cons_id=%s"
        cursor.execute(query, (*new_values, cons_id))
        connection.commit()
        print("Client updated successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)

def delete_consum(connection, cons_id):

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM consumption WHERE cons_id=%s"
        cursor.execute(delete_query, (cons_id,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_consum(connection, consum):
    if consum == "":
        return None

    try:
        cursor = connection.cursor()

        query = f"""
            SELECT
                consumption.cons_id ,
                service.ser_id ,
                service.descp,
                consumption.cnt,
                client.c_id,
                client.c_name
            FROM
                consumption 
            JOIN
                service  ON consumption.ser_id = service.ser_id
            JOIN
                client ON consumption.c_id = client.c_id;
            WHERE
                consumption.cons_id = {consum};
        """
        cursor.execute(query)
        search_results = cursor.fetchall()

        consum1 = [
            ["Consumption ID", "Service ID", "Description", "Count", "Client ID", "Client name"],
        ]

        if search_results:
            for result in search_results:
                consum1.append(list(result))
            return consum1
        else:
            return None

    except Error as e:
        print(f"Error: {e}")
        return None