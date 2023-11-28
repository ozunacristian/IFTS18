from peewee import *
from datetime import datetime

# función que conecta y retorna base de datos.
def funcion_conectar_db():
  sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})
  try:
    sqlite_db.connect()
    print("Base de datos conectada.")
  except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()
  return sqlite_db
  

# función que mapea y crea las tablas de la base de datos en donde se cargará el dataset limpio.
def funcion_mapear_orm(db):
  class BaseModel(Model):
    class Meta:
        database = db

    # -----------------------------Tablas de consulta (lookups) -------------------------
  class Etapa(BaseModel):
    ID_ETAPA = AutoField()
    nombre_etapa = CharField(unique=True)
    def __str__(self):
      return self.nombre_etapa
    class Meta:
      db_table = 'Etapa'
      
  class TipoObra(BaseModel):
    ID_TIPO_OBRA = AutoField()
    tipo_obra = CharField(unique=True)
    def __str__(self):
      return self.tipo_obra
    class Meta:
      db_table = 'TipoObra'
      
  class AreaResponsable(BaseModel):
    ID_AREA_RESPONSABLE = AutoField()
    nombre_area = CharField(unique=True)
    def __str__(self):
      return self.nombre_area
    class Meta:
      db_table = 'AreaResponsable'

  class Comuna(BaseModel):
    ID_COMUNA = AutoField()
    nombre_comuna = CharField(unique=True)
    def __str__(self):
      return self.nombre_comuna
    class Meta:
      db_table = 'Comuna'

  class Barrio(BaseModel):
    ID_BARRIO = AutoField()
    nombre_barrio = CharField(unique=True)
    comuna = ForeignKeyField(Comuna, backref='barrio') # Muchos barrios pueden estar en una comuna
    def __str__(self):
      return self.nombre_barrio
    class Meta:
      db_table = 'Barrio'

  class ContratacionTipo(BaseModel):
    ID_TIPO_CONTRATACION = AutoField()
    contratacion = CharField(unique=True)
    def __str__(self):
      return self.contratacion
    class Meta:
      db_table = 'TipoContratacion'

  class Financiamiento(BaseModel):
    ID_FINANCIAMIENTO = AutoField()
    financiamiento = CharField(unique=True)
    def __str__(self):
      return self.financiamiento
    class Meta:
      db_table = 'Financiamiento'

  # -------------------------------Tabla principal--------------------------
  class Obra(BaseModel):
    ID_OBRA_URBANA = AutoField() # por forma N1 se agrega campo ID, a definir
    entorno = CharField(100) # Se limita a 100 carácteres.
    nombre = CharField(100)
    etapa = ForeignKeyField(Etapa, backref='obra')
    tipo_obra = ForeignKeyField(TipoObra, backref='obra')
    area_responsable = ForeignKeyField(AreaResponsable, backref = 'obra')
    descripcion = CharField(500)
    monto_contrato = IntegerField(20)
    comuna = ForeignKeyField(Comuna, backref = 'obra')
    barrio = ForeignKeyField(Barrio, backref='obra') # Analizar mejor : deberíamos poder responder ¿cuántos barrios por comuna?
    direccion = CharField(200)
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = FloatField()
    porcentaje_avance = IntegerField()
    imagen = TextField()
    licitacion_oferta_empresa = TextField()
    licitacion_anio = IntegerField()
    contratacion_tipo = ForeignKeyField(ContratacionTipo, backref = 'obra')
    nro_contratacion = CharField(50)
    cuit_contratista = IntegerField()
    mano_obra = IntegerField()
    destacada = BooleanField()
    expediente_numero = CharField(100)
    financiamiento = ForeignKeyField(Financiamiento, backref = 'obra')

    def __str__(self):
        pass
    class Meta:
        db_table = 'Obra'
    
    # NUEVA OBRA
  # LLAMA A TODOS LOS METODOS DE INSTANCIA menos rescindir_obra
    
  # La clase “Obra”, que es una de las clases que debe formar parte del modelo ORM, debe incluir
  # los siguientes métodos de instancia con el objetivo de definir las diferentes etapas de avance
  # de obra:
  # a. nuevo_proyecto().
  # 	Asigna "Proyecto" en etapa
  # 	Ingresa entorno
  # 	Ingresa nombre
  # 	Tipo obra*
  # 	Area responsable *
  # 	Ingresa descripción
  # 	Monto contrato (FLOAT)
  # 	Comuna *
  # 	Barrio *
  # 	Direccion 
  # 	plazo_meses (FLOAT)
  # 	Porcentaje_avances (0)
  # 	imagen_1
    
  # b. iniciar_contratacion().	
  # 	COntratacion_tipo *
  # 	nro_contratacion
  # 	cuit_contratista
  # 	liciation_anio (INT)
  # 	contratacion_tipo *
    
  # c. adjudicar_obra().
  # 	Licitacion_oferta_empresa*				
  # 	Expediente numero 
    
  # d. iniciar_obra().
  # 	destacada(BOOL)
  # 	Fecha_inicio
  # 	Fecha_fin_inicial
  # 	financiamiento*
  # 	mano_obra (INT)
    
  # e. actualizar_porcentaje_avance().
  # 	MODIFICA: Porcentaje_avances(0)
    
  # f. incrementar_plazo().
  # 	MODIFICA:plazo_meses (FLOAT)
    
  # g. incrementar_mano_obra().
  # 	MODIFICA:mano_obra (INT)
    
  # h. finalizar_obra().
  # 	MODIFICA:Asigna "Finalizado" en etapa
  # 	MODIFICA:MODIFICA: Porcentaje_avances(0)
  # 	((LLAMA A ACTUALIZAR % AVANCE))
    
  # i. rescindir_obra().
  # 	MODIFICA:Asigna "Rescindida" en etapa


    def nuevo_proyecto(self):
      # VALIDAR TIPO DE DATO
      # Para iniciar un nuevo proyecto de obra se debe invocar al método nuevo_proyecto(). Aquí la etapa inicial de las nuevas instancias de Obra debe tener el valor “Proyecto” (si este valor no existe en la tabla “etapas” de la BD, se deberá crear la instancia y luego insertar el nuevo registro). Los valores de los atributos tipo_obra, area_responsable y barrio deben ser alguno de los existentes en la base de datos.

      # Asigna automáticamente Proyecto al atributo etapa.
      # solicita entorno:str, nombre:str, 
      # Se muestra menu con opciones para tipo_obra, area_responsable, barrio.

      pass

    def iniciar_contratacion(self):
      # A continuación, se debe iniciar la licitación/contratación de la obra, para ello se debe invocar al método iniciar_contratacion(), asignando el TipoContratacion (debe ser un valor existente en la BD) y el nro_contratacion.

      # Se solicita licitación/contratación de la obra
      # Muestra opciones de contratacion_tipo traidas desde la BD.
      # solicita nro_contratacion
      pass

    def adjudicar_obra(self):
      # Para adjudicar la obra a una empresa, se debe invocar al método adjudicar_obra() y asignarle la Empresa (debe ser una empresa existente en la BD) y el nro_expediente.
      pass

    def iniciar_obra(self):
      # Para indicar el inicio de la obra, se debe invocar al método iniciar_obra(), y asignarle valores a los siguientes atributos: destacada, fecha_inicio, fecha_fin_inicial, fuente_financiamiento (debe ser un valor existente en la BD) y mano_obra.
      pass

    def actualizar_porcentaje_avance(self):
      # Para registrar avances de la obra, se debe invocar al método actualizar_porcentaje_avance() y actualizar el valor del atributo porcentaje_avance.
      pass

    def incrementar_plazo(self):
      # Para incrementar el plazo de la obra, se debe invocar al método incrementar_plazo() y actualizar el valor del atributo plazo_meses. (Esta acción es opcional, pero el método debe estar definido).

      # actualizar el atributo plazo_meses 
      pass

    def incrementar_mano_obra(self):
      # Para incrementar la cantidad de mano de obra, se debe invocar al método incrementar_mano_obra() y actualizar el valor del atributo mano_obra. (Esta acción es opcional, pero el método debe estar definido).
      pass

    def finalizar_obra(self):
      # Para indicar la finalización de una obra, se debe invocar al método finalizar_obra() y actualizar el valor del atributo etapa a “Finalizada” y del atributo porcentaje_avance a “100”.
      pass

    def rescindir_obra(self):
      # Para indicar la rescisión de una obra, se debe invocar al método rescindir_obra() y actualizar el valor del atributo etapa a “Rescindida”.
      pass
  
  # Creamos todas las tablas
  db.create_tables([Etapa, TipoObra, AreaResponsable, Comuna, Barrio, ContratacionTipo, Financiamiento, Obra])
  print("ORM mapeado.")
  # Retornamos las clases por estar dentro de una función.
  return Etapa, TipoObra, AreaResponsable, Comuna, Barrio, ContratacionTipo, Financiamiento, Obra