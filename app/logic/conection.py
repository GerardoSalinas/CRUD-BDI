import pyodbc

class Connection:
  def __init__(self):
    pass
  # Establishing a connection to the SQL Server
  def connect_to_sql(self, server, database, port):
    global USERNAME, DATABASE
    try:
      connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server},{port};"
        "Trusted_Connection=yes;"
      ) 
      cnxn = pyodbc.connect(connection_string)
      cnxn.autocommit = True
      cursor = cnxn.cursor()
      cursor.execute(f'CREATE DATABASE {database}')
      cursor.execute('SELECT USER_NAME()')
      user_name = cursor.fetchone()[0]
      cursor.close()
      print('connected. Database was created')
      return (user_name, database)
    except Exception as e:
      raise Exception(e)

  def connect_to_database(self, server, database, port):
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server},{port};"
        f"database={database};"
        "Trusted_Connection=yes;"
      ) 

    try:
      conn = pyodbc.connect(connection_string)
      return conn
    except Exception as e:
      raise Exception(e)
    
  def validate_user(self, server, database, port, username, password):
    conn = self.connect_to_database(server, database, port)
    cursor = conn.cursor()

    query = "SELECT * FROM Usuarios WHERE NombreUsuario=? AND Contrasena=?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
      return True
    else:
      return False    