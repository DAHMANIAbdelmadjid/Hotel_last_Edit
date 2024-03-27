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


def insert_room(connection, *values):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO room (room_num, type, price, stat, discount) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, values)
        connection.commit()
        print("user inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def select_all_rooms(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM room"
        cursor.execute(query)
        rooms = cursor.fetchall()
        close_connection(connection)
        room1 = [["Room number", "Type", "Price", "Status", "Discount"], ]
        for room in rooms:
            room1.append(list(room))
        return room1
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def update_room(connection, room_num, *new_values):
    try:
        cursor = connection.cursor()
        query = "UPDATE room SET type=%s, price=%s, stat=%s, discount=%s WHERE room_num=%s"
        cursor.execute(query, (*new_values, room_num))
        connection.commit()
        print("Book updated successfully")
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def delete_room(connection, room_num):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM room WHERE room_num=%s"
        cursor.execute(delete_query, (room_num,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    close_connection(connection)


def search_room(connection, room):
    if not room:
        return None

    try:
        cursor = connection.cursor()
        WHERE = ["room_num", "type", "price", "stat", "discount"]
        search_results = []

        for i in WHERE:
            query = f"SELECT * FROM room WHERE {i} LIKE %s"
            cursor.execute(query, ('%' + room + '%',))
            search_results.extend(cursor.fetchall())
            if search_results:
                break

        if not search_results:
            print("No matching rooms found.")
        else:
            print("Search Results:")
            return [["Room number", "Type", "Price", "Status", "Discount"]] + [list(room) for room in search_results]

    except Error as e:
        print(f"Error: {e}")
        return None
    close_connection(connection)

# con=create_connection()
# print(search_book(con,"T"))
 