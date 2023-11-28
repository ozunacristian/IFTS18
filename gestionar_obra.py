from os import system
from abc import ABC
from peewee import *
from extraer_datos import *
from modelo_orm import *
#import extraer_datos as etl
#import modelo_ as 
# definición de la clase abstracta “GestionarObra”
class GestionarObra(ABC):
  dataFrame = None
  db = None
  Etapa = None
  TipoObra = None
  AreaResponsable = None
  Comuna = None
  Barrio = None
  ContratacionTipo = None
  Financiamiento = None
  Obra = None

  def __init__():
    pass
  
  @classmethod
  def extraer_datos(cls):
    cls.dataFrame = funcion_extraer_datos()

  @classmethod
  def conectar_db(cls):
    cls.db = funcion_conectar_db()


  @classmethod
  def mapear_orm(cls):
    # Guardamos en las variables de clase las clases que estan dentro de una funcion
    cls.Etapa, cls.TipoObra, cls.AreaResponsable, cls.Comuna, cls.Barrio, cls.ContratacionTipo, cls.Financiamiento, cls.Obra = funcion_mapear_orm(cls.db)
    

  @classmethod
  def limpiar_datos(cls):
    cls.dataFrame = funcion_limpiar(cls.dataFrame)
    print("DataFrame limpio.")


  @classmethod
  def cargar_datos(cls):
    # Obtenemos valores únicos de cada columna.
    try:
      lista_etapas = list(cls.dataFrame['etapa'].unique())
      lista_tipoObras = list(cls.dataFrame['tipo'].unique())
      lista_area_resps = list(cls.dataFrame['area_responsable'].unique())
      lista_comunas = list(cls.dataFrame['comuna'].unique())
      lista_contratacion = list(cls.dataFrame['contratacion_tipo'].unique())
      lista_financiamiento = list(cls.dataFrame['financiamiento'].unique())
      print("Valores únicos por columna obtenidos correctamente.")
    except Exception as e:
       print("Error al obtener valores únicos.",e)

    # ---- Las tablas comuna y barrio estan relacionadas, para eso creamos diccionario basándonos en el dataframe--------
    comunas_barrios = {}
    for comuna in lista_comunas:
        comunas_barrios[comuna] = cls.dataFrame[cls.dataFrame['comuna'] == comuna]['barrio'].unique()

    # ---------------------------  Cargamos tablas de consulta (lookups) -------------------
    for elem in lista_etapas:
        try:
            cls.Etapa.create(nombre_etapa = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Etapa", e)
    print("Se han persistido las etapas en la BD.")
       
    for elem in lista_tipoObras:
        try:
            cls.TipoObra.create(tipo_obra = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla TipoObra", e)
    print("Se han persistido los tipos de obras en la BD.")

    for elem in lista_area_resps:
        try:
            cls.AreaResponsable.create(nombre_area = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla AreaResponsable", e)
    print("Se han persistido las áreas responsables en la BD.")

    # Se carga comuna y barrios sirviendose del subdataframe creado en la línea 63
    try:
       for elem in lista_comunas:
          try:
              comuna = cls.Comuna.create(nombre_comuna=elem)
              for barrio in comunas_barrios[elem]:
                  # se asocia cada barrio a su comuna correspondiente
                  cls.Barrio.create(nombre_barrio=barrio, comuna=comuna)
          except IntegrityError as e:
              print("Error al insertar un nuevo registro en la tabla Comuna y barrio", e)
       print("Se han persistido las comunas y sus barrios en la BD.")
    except IntegrityError as e:
       print("Error al persistir datos en tabla Comuna y Barrio", e)

    for elem in lista_contratacion:
        try:
            cls.ContratacionTipo.create(contratacion = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla ContratacionTipo", e)
    print("Se han persistido los tipos de contrataciones en la BD.")

    for elem in lista_financiamiento:
        try:
            cls.Financiamiento.create(financiamiento = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Financiamiento", e)
    print("Se han persistido los financiamientos en la BD.")


    # Cargamos la tabla principal Obra
    cargando = ""
    conteo = 0
    for elem in cls.dataFrame.values:
        # En vista de que tarda mucho, emulamos carga con puntos
        print("Cargando registros en tabla Obra")
        if conteo < 45:
         cargando += "||"
         print(cargando)
         conteo += 1
         system('cls')
        else:
           conteo = 0
           cargando = ""
           system('cls')

        # Se obtiene el id de la tabla lookup y lo guardamos en una variable.
        fk_etapa = cls.Etapa.get(cls.Etapa.nombre_etapa == elem[2])
        fk_obra = cls.TipoObra.get(cls.TipoObra.tipo_obra == elem[3])
        fk_area_resp = cls.AreaResponsable.get(cls.AreaResponsable.nombre_area == elem[4])
        fk_comuna = cls.Comuna.get(cls.Comuna.nombre_comuna == elem[7])
        fk_barrio = cls.Barrio.get(cls.Barrio.nombre_barrio == elem[8])
        fk_contratacion = cls.ContratacionTipo.get(cls.ContratacionTipo.contratacion == elem[17])
        fk_financiamiento = cls.Financiamiento.get(cls.Financiamiento.financiamiento == elem[23])
        try:
            cls.Obra.create(entorno=elem[0], #elem[indice] hace referencia a la columna del dataframe
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
            print("Error al insertar un nuevo registro en la tabla Obra.", e)
    system('cls')
    print("Se han persistido correctamente los registros en la BD.")



  @classmethod
  def nueva_obra(cls):
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
try:
  GestionarObra.extraer_datos()
  GestionarObra.conectar_db()
  GestionarObra.mapear_orm()
  GestionarObra.limpiar_datos()
  GestionarObra.cargar_datos()
except Exception as e:
  print(e)
