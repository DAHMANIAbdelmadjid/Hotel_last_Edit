import mysql.connector
from mysql.connector import Error
from datetime import datetime,timedelta

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='library',
            user='root',
            password='1234'
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

def insert_borrow(connection, *values):
    current_date = datetime.now().date()
    new_date = current_date + timedelta(days=15)
    try:
        cursor = connection.cursor()
        query = "INSERT INTO prets (NumeroMatricule,CodeCatalogue,DatePret,DateRetourPrevu) VALUES (%s, %s, %s,%s)"
        cursor.execute(query, (*values,current_date,new_date))
        connection.commit()
        print("borrow inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def select_all_borrows(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                prets.NumeroMatricule ,
                abonnes.Nom ,
                prets.CodeCatalogue,
                livres.Titre,
                prets.Cote,
                prets.DatePret,
                prets.DateRetourPrevu
            FROM
                prets 
            JOIN
                abonnes  ON prets.NumeroMatricule = abonnes.NumeroMatricule
            JOIN
                livres ON prets.CodeCatalogue = livres.CodeCatalogue;
        """
        cursor.execute(query)
        borrows = cursor.fetchall()
        close_connection(connection)

        borrow1 = [
            ["User ID", "User", "Book ID", "Book", "CodeCatalogue", "DatePret", "DateRetourPrevu"],
        ]
        for borrow in borrows:
            borrow1.append(list(borrow))
        return borrow1
    except Error as e:
        print(f"Error: {e}")


def delete_borrow(connection, code_catalogue):

    try:
        cursor = connection.cursor()
        delete_query = f"DELETE FROM prets WHERE CodeCatalogue= {code_catalogue}"
        cursor.execute(delete_query)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")

def search_borrow(connection, title):
    if title == "":
        return None

    try:
        cursor = connection.cursor()

        query = f"""
            SELECT
                prets.NumeroMatricule,
                abonnes.Nom,
                prets.CodeCatalogue,
                livres.Titre,
                prets.Cote,
                prets.DatePret,
                prets.DateRetourPrevu
            FROM
                prets
            JOIN
                abonnes ON prets.NumeroMatricule = abonnes.NumeroMatricule
            JOIN
                livres ON prets.CodeCatalogue = livres.CodeCatalogue
            WHERE
                prets.CodeCatalogue = {title};
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

# con=create_connection()
# print(delete_borrow(con,3))
 