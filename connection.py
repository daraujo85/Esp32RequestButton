import mysql.connector

def login(usuario, senha):
    # Connect to server
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="dbteste")

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM usuario WHERE nome = %s and senha = %s", (usuario, senha))

    myresult = cur.fetchone()


    # Close connection
    cnx.close()

    return myresult

result = login('Diego', '123456')

print(result)
