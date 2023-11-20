# Aquí irian las definiciones de las clases y atributos
# para persistir lo obtenido del dataset importado,
# en una base de datos SQLite: 'obras_urbanas.db'

# se debe incluir la clase BaseModel de peewee

def conectar_db():
  sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})
  try:
      sqlite_db.connect()
  except OperationalError as e:
      print("Error al conectar con la BD.", e)
      exit()


def mapear_orm():
  pass