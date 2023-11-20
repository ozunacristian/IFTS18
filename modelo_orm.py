from peewee import *

sqlite_db = None
# función que conecta la base de datos con control de excepción.
def conectar_db():
  sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})
  try:
      sqlite_db.connect()
      print("Base de datos fué conectada.")
  except OperationalError as e:
      print("Error al conectar con la BD.", e)
      exit()

# función que mapea y crea las tablas de la base de datos en donde se ingresará el dataset limpio.
def mapear_orm():
  class BaseModel(Model):
    class Meta:
        database = sqlite_db

    # -----------------------------Tablas de consulta (lookups) -------------------------
  class Etapa(BaseModel):
    ID_ETAPA = AutoField() # a definir
    nombre_etapa = CharField(unique=True)
    def __str__(self):
      return self.nombre_etapa
    class Meta:
      db_table = 'Etapa'
      
  class TipoObra(BaseModel):
    ID_TIPO = AutoField() # a definir
    tipo_obra = CharField(unique=True)
    def __str__(self):
      return self.tipo_obra
    class Meta:
      db_table = 'TipoObra'
      
  class AreaResponsable(BaseModel):
    ID_AREA_RESPONSABLE = AutoField() # a definir
    nombre_area = CharField(unique=True)
    def __str__(self):
      return self.nombre_area
    class Meta:
      db_table = 'AreaResponsable'

  class Barrio(BaseModel):
    ID_BARRIO = AutoField() # a definir
    nombre_barrio = CharField(unique=True)
    def __str__(self):
      return self.nombre_barrio
    class Meta:
      db_table = 'Barrio'

  class Comuna(BaseModel):
    ID_COMUNA = AutoField() # a definir
    nombre_comuna = CharField(unique=True)
    barrio = ForeignKeyField(Barrio, backref= 'comuna') # Analizar esto
    def __str__(self):
      return self.nombre_comuna
    class Meta:
      db_table = 'Comuna'

  class ContratacionTipo(BaseModel):
    ID_TIPO_CONTRATACION = AutoField() # a definir
    contratacion = CharField(unique=True)
    def __str__(self):
      return self.contratacion
    class Meta:
      db_table = 'TipoContratacion'

  # -------------------------------Tabla principal--------------------------
  class ObraUrbana(BaseModel):
    ID_OBRA_URBANA = AutoField() # por forma N1 se agrega campo ID, a definir
    entorno = CharField(100) # Se limita a 100 carácteres.
    FK_etapa = ForeignKeyField(Etapa, backref='obra_urbana')
    FK_tipo_obra = ForeignKeyField(TipoObra, backref='obra_urbana')
    FK_area_responsable = ForeignKeyField(AreaResponsable, backref = 'obra_urbana')
    nombre = CharField(100)
    descripcion = CharField(500)
    monto_contrato = IntegerField(20)
    FK_comuna = ForeignKeyField(Comuna, backref = 'obra_urbana')
    FK_barrio = ForeignKeyField(Barrio, BackrefAccessor='obra_urbana') # Analizar mejor : deberíamos poder responder ¿cuántos barrios por comuna?
    direccion = CharField(200)
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = FloatField()
    porcentaje_avance = IntegerField()
    imagen = TextField()
    licitacion_oferta_empresa = TextField()
    licitacion_anio = IntegerField()
    FK_contratacion_tipo = ForeignKeyField(ContratacionTipo, backref = 'obra_urbana')
    nro_contratacion = CharField(50)
    cuit_contratista = IntegerField()
    mano_obra = IntegerField()
    destacada = BooleanField()
    expediente_numero = CharField(100)
    financiamiento = CharField(50)

    def __str__(self):
        pass
    class Meta:
        db_table = 'ObraUrbana'

  # Creamos todas las tablas
  sqlite_db.create_tables([Etapa, TipoObra, AreaResponsable, Comuna, Barrio, ContratacionTipo, ObraUrbana])