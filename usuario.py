from connection import * 

def login(usuario, senha):
    

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM usuario WHERE nome = %s and senha = %s", (usuario, senha))

    myresult = cur.fetchone()


    # Close connection
    cnx.close()

    return myresult