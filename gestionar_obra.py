from peewee import *
from abc import ABC
from os import system
from preprocesado import *

class GestionarObra(ABC):
  def __init__():
    pass
  
  @classmethod
  def extraer_datos(cls): # retorna DataFrame sin preprocesado.
    try:
        df = pd.read_csv('observatorio-de-obras-urbanas.csv', encoding = 'UTF-8')
        print("Datos extraidos correctamente.")
    except Exception as e:
        print("Error al extraer datos ,", e)
    return df

  @classmethod
  def conectar_db(cls): # retorna el sqlite_db
    sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})
    try:
        sqlite_db.connect()
        return sqlite_db
    except OperationalError as e:
        print("Se ha generado un error en la conexion a la BD.", e)
        exit()

  @classmethod
  def mapear_orm(cls, db, tablas): # toma sqlite_db y una lista de tablas para mapear
    db.create_tables(tablas)
    
  @classmethod
  def limpiar_datos(cls): # retorna DataFrame limpio
    df = limpiar(cls.extraer_datos())
    return df

  @classmethod
  def cargar_datos(cls, Etapa, TipoObra, AreaResponsable, Comuna, Barrio, ContratacionTipo, Financiamiento, Obra):
    df = cls.limpiar_datos()
    # Obtenemos valores únicos de cada columna.
    try:
      lista_etapas = list(df['etapa'].unique())
      lista_tipoObras = list(df['tipo'].unique())
      lista_area_resps = list(df['area_responsable'].unique())
      lista_comunas = list(df['comuna'].unique())
      lista_contratacion = list(df['contratacion_tipo'].unique())
      lista_financiamiento = list(df['financiamiento'].unique())
      print("Valores únicos por columna obtenidos correctamente.")
    except Exception as e:
       print("No se obtuvieron los valores únicos",e)

    # ---- Las tablas comuna y barrio estan relacionadas, para eso creamos diccionario basándonos en el dataframe--------
    comunas_barrios = {}
    for comuna in lista_comunas:
        comunas_barrios[comuna] = df[df['comuna'] == comuna]['barrio'].unique()

    # ---------------------------  Cargamos tablas de consulta (lookups) -------------------
    for elem in lista_etapas:
        try:
            Etapa.create(nombre_etapa = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Etapa", e)
    print("Se han persistido las etapas en la BD.")
       
    for elem in lista_tipoObras:
        try:
            TipoObra.create(tipo_obra = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla TipoObra", e)
    print("Se han persistido los tipos de obras en la BD.")

    for elem in lista_area_resps:
        try:
            AreaResponsable.create(nombre_area = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla AreaResponsable", e)
    print("Se han persistido las áreas responsables en la BD.")

    # Se carga comuna y barrios sirviendose del diccionario creado en la línea 63
    for elem in lista_comunas:
      try:
          comuna = Comuna.create(nombre_comuna=elem)
          for barrio in comunas_barrios[elem]:
              # se asocia cada barrio a su comuna correspondiente
              Barrio.create(nombre_barrio=barrio, comuna=comuna)
          print("Se han persistido las comunas y sus barrios en la BD.")
      except IntegrityError as e:
          print("Error al insertar un nuevo registro en la tabla Comuna y barrio", e)

    for elem in lista_contratacion:
        try:
            ContratacionTipo.create(contratacion = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla ContratacionTipo", e)
    print("Se han persistido los tipos de contrataciones en la BD.")

    for elem in lista_financiamiento:
        try:
            Financiamiento.create(financiamiento = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Financiamiento", e)
    print("Se han persistido los financiamientos en la BD.")


    # Cargamos la tabla principal ObraUrbana
    print("cargando registros en tabla ObraUrbana...")
    cargando = ""
    for elem in df.values:
        # En vista de que tarda mucho, imprimimos un punto por cada iteracion para emular carga
        cargando = cargando + "."
        print(cargando)
        # Se obtiene el id de la tabla lookup y lo guardamos en una variable.
        fk_etapa = Etapa.get(Etapa.nombre_etapa == elem[2])
        fk_obra = TipoObra.get(TipoObra.tipo_obra == elem[3])
        fk_area_resp = AreaResponsable.get(AreaResponsable.nombre_area == elem[4])
        fk_comuna = Comuna.get(Comuna.nombre_comuna == elem[7])
        fk_barrio = Barrio.get(Barrio.nombre_barrio == elem[8])
        fk_contratacion = ContratacionTipo.get(ContratacionTipo.contratacion == elem[17])
        fk_financiamiento = Financiamiento.get(Financiamiento.financiamiento == elem[23])
        try:
            Obra.create(entorno=elem[0], #elem[indice] hace referencia a la columna del dataframe
                                  nombre=elem[1],
                                  etapa=fk_etapa,
                                  tipo_obra=fk_obra,
                                  area_responsable=fk_area_resp,
                                  descripcion=elem[5],
                                  monto_contrato=elem[6],
                                  comuna=fk_comuna,
                                  barrio=fk_barrio,
                                  direccion=elem[9],
                                  fecha_inicio=elem[10],
                                  fecha_fin_inicial=elem[11],
                                  plazo_meses=elem[12],
                                  porcentaje_avance=elem[13],
                                  imagen=elem[14],
                                  licitacion_oferta_empresa=elem[15],
                                  licitacion_anio=elem[16],
                                  contratacion_tipo=fk_contratacion,
                                  nro_contratacion=elem[18],
                                  cuit_contratista=elem[19],
                                  mano_obra=elem[20],
                                  destacada=elem[21],
                                  expediente_numero=elem[22],
                                  financiamiento=fk_financiamiento
                                  )
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla ObraUrbana.", e)
    system('cls')
    print("Se han persistido correctamente los registros en la BD.")

  @classmethod
  def nueva_obra(cls):
    # desarrollando...
    pass
  
  @classmethod
  def obtener_indicadores(cls):
    """ mostrar por consola la siguiente información:
    a. Listado de todas las áreas responsables.
    b. Listado de todos los tipos de obra.
    c. Cantidad de obras que se encuentran en cada etapa.
    d. Cantidad de obras y monto total de inversión por tipo de obra.
    e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
    f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.
    g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
    h. Porcentaje total de obras finalizadas.
    i. Cantidad total de mano de obra empleada.
    j. Monto total de inversión. """
    pass

