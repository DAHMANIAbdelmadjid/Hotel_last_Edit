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


def insert_client(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO client (iden_num ,name ,c_ph_number) VALUES (%s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("user inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def select_all_user(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM client"
        cursor.execute(query)
        clients = cursor.fetchall()
        close_connection(connection)
        client1 = [["Client ID", "Identification number", "Client name", "Phone number"], ]
        for client in clients:
            client1.append(list(client))
        return client1
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def update_user(connection, c_id, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE client SET iden_num=%s, c_name=%s, c_ph_numer=%s WHERE c_id=%s"
        cursor.execute(query, (*new_values, c_id))
        connection.commit()
        print("Client updated successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)

    # ["NumeroMatricule","Nom" ,"Prenom"," Adresse"," Email"]
    # try:
    #     cursor = connection.cursor()
    #     query = "UPDATE abonnes SET Nom=%s, Prenom=%s, Adresse=%s, Email=%s WHERE NumeroMatricule=%s"
    #     cursor.execute(query, (*new_values, code_catalogue))
    #     connection.commit()
    #     print("user updated successfully")
    # except Error as e :

    #     print(f"Error: {e}")


def delete_user(connection, c_id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM client WHERE c_id=%s"
        cursor.execute(delete_query, (c_id,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def search_user(connection, name):
    if not name:
        return None
    try:
        cursor = connection.cursor()
        WHERE = ["c_id", "iden_num", "c_name", "c_ph_numer"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM client WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + name + '%',))
            search_results.extend(cursor.fetchall())
            if search_results:
                break

        if not search_results:
            print("No matching clients found.")
        else:
            print("Search Results:")
            return [["Client ID", "Identification number", "Name", "Phone number"]] + [list(client) for client in
                                                                                       search_results]

    except Error as e:
        print(f"Error: {e}")
        return None
    close_connection(connection)
# con=create_connection()
# print(search_user(con,""))
