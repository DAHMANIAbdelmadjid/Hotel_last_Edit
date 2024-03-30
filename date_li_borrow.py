import mysql.connector
from mysql.connector import Error
from datetime import datetime,timedelta

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

def insert_reserv(connection,check_out, c_id, room_num):
    check_in= datetime.now().date()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT price, discount FROM room WHERE room_num = %s", (room_num,))
        room_data = cursor.fetchone()
        room_price = room_data[0]
        room_discount = room_data[1]
        check_out_datetime = datetime.strptime(check_out, '%Y-%m-%d')
        check_out_date = check_out_datetime.date()

        dur = (check_out_date - datetime.now().date()).days

#
        if room_discount != '0%':
            discount_fact = (100 - int(room_discount.strip('%'))) / 100
            discounted_price = room_price * discount_fact
            payment = dur * discounted_price
        else:
            payment = dur * room_price
        cursor.execute("""
UPDATE client
SET faithful = CASE 
                    WHEN EXISTS (SELECT 1 FROM reservation WHERE c_id = client.c_id) THEN
                        CASE 
                            WHEN (SELECT MAX(check_out) FROM reservation WHERE c_id = client.c_id) >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH) THEN 'Loyal'
                            ELSE 'Unloyal'
                        END
                    ELSE 'Unloyal'
                END;
""")
        cursor.execute(
            "INSERT INTO reservation (check_in, check_out, c_id, room_num, payment) VALUES (%s, %s, %s, %s, %s)",
            (check_in, check_out, c_id, room_num, payment))
        connection.commit()
        print("Reservation inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def select_all_reserv(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                reservation.res_id ,
                reservation.check_in ,
                reservation.check_out,
                reservation.payment,
                client.c_id,
                client.c_name,
                room.room_num
            FROM
                reservation 
            JOIN
                client  ON reservation.c_id = client.c_id
            JOIN
                room ON reservation.room_num = room.room_num;
        """
        cursor.execute(query)
        reservs = cursor.fetchall()
        close_connection(connection)

        reserv1 = [
            ["Reservation ID", "Check in", "Check out", "Payment", "Client ID", "Client name", "Room number"],
        ]
        for reserv in reservs:
            reserv1.append(list(reserv))
        return reserv1
    except Error as e:
        print(f"Error: {e}")


def delete_reserv(connection, res_id):

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM reservation WHERE res_id=%s"
        cursor.execute(delete_query, (res_id,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_reserv(connection, reserv):
    if reserv == "":
        return None

    try:
        cursor = connection.cursor()

        query = f"""
            SELECT
                reservation.res_id ,
                reservation.check_in ,
                reservation.check_out,
                reservation.payment,
                client.c_id,
                client.c_name,
                room.room_num
            FROM
                reservation 
            JOIN
                client  ON reservation.c_id = client.c_id
            JOIN
                room ON reservation.room_num = room.room_num;
            WHERE
                reservation.res_id = {reserv};
        """
        cursor.execute(query)
        search_results = cursor.fetchall()

        borrow1 = [
            ["User ID", "User", "Book ID", "Book", "CodeCatalogue", "DatePret", "DateRetourPrevu"],
        ]

        if search_results:
            for result in search_results:
                borrow1.append(list(result))
            return borrow1
        else:
            return None

    except Error as e:
        print(f"Error: {e}")
        return None

con=create_connection()
print(insert_reserv(con,'2021-10-10',5,1))