from os import system
from abc import ABC, abstractmethod
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
  ObraUrbana = None

  def __init__():
    pass
  
  @classmethod
  def extraer_datos(cls):
    GestionarObra.dataFrame = funcion_extraer_datos()

  @classmethod
  def conectar_db(cls):
    GestionarObra.db = funcion_conectar_db()


  @classmethod
  def mapear_orm(cls):
    # Guardamos en las variables de clase las clases que estan dentro de una funcion
    GestionarObra.Etapa, GestionarObra.TipoObra, GestionarObra.AreaResponsable, GestionarObra.Comuna, GestionarObra.Barrio, GestionarObra.ContratacionTipo, GestionarObra.Financiamiento, GestionarObra.ObraUrbana = funcion_mapear_orm(GestionarObra.db)
    

  @classmethod
  def limpiar_datos(cls):
    GestionarObra.dataFrame = funcion_limpiar(GestionarObra.dataFrame)
    print("DataFrame limpio.")


  @classmethod
  def cargar_datos(cls):
    # Obtenemos valores únicos de cada columna.
    try:
      lista_etapas = list(GestionarObra.dataFrame['etapa'].unique())
      lista_tipoObras = list(GestionarObra.dataFrame['tipo'].unique())
      lista_area_resps = list(GestionarObra.dataFrame['area_responsable'].unique())
      lista_comunas = list(GestionarObra.dataFrame['comuna'].unique())
      lista_barrios = list(GestionarObra.dataFrame['barrio'].unique())
      lista_contratacion = list(GestionarObra.dataFrame['contratacion_tipo'].unique())
      lista_financiamiento = list(GestionarObra.dataFrame['financiamiento'].unique())
      print("Valores únicos por columna obtenidos correctamente.")
    except Exception as e:
       print("No se obtuvieron los valores únicos",e)

    # ---------------------------  Cargamos tablas de consulta (lookups) -------------------
    for elem in lista_etapas:
        try:
            GestionarObra.Etapa.create(nombre_etapa = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Etapa", e)
    print("Se han persistido las etapas en la BD.")
       
    for elem in lista_tipoObras:
        try:
            GestionarObra.TipoObra.create(tipo_obra = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla TipoObra", e)
    print("Se han persistido los tipos de obras en la BD.")

    for elem in lista_area_resps:
        try:
            GestionarObra.AreaResponsable.create(nombre_area = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla AreaResponsable", e)
    print("Se han persistido las áreas responsables en la BD.")

    for elem in lista_comunas:
        try:
            GestionarObra.Comuna.create(nombre_comuna = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Comuna", e)
    print("Se han persistido las comunas en la BD.")

    for elem in lista_barrios:
        try:
            GestionarObra.Barrio.create(nombre_barrio = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Barrio", e)
    print("Se han persistido los barrios en la BD.")

    for elem in lista_contratacion:
        try:
            GestionarObra.ContratacionTipo.create(contratacion = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla ContratacionTipo", e)
    print("Se han persistido los tipos de contrataciones en la BD.")

    for elem in lista_financiamiento:
        try:
            GestionarObra.Financiamiento.create(financiamiento = elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Financiamiento", e)
    print("Se han persistido los financiamientos en la BD.")


    # Cargamos la tabla principal ObraUrbana
    print("cargando registros en tabla ObraUrbana...")
    cargando = ""
    for elem in GestionarObra.dataFrame.values:
        # En vista de que tarda mucho, imprimimos un punto por cada iteracion para emular carga
        cargando = cargando + "..."
        print(cargando)
        # Se obtiene el id de la tabla lookup y lo guardamos en una variable.
        fk_etapa = GestionarObra.Etapa.get(GestionarObra.Etapa.nombre_etapa == elem[2])
        fk_obra = GestionarObra.TipoObra.get(GestionarObra.TipoObra.tipo_obra == elem[3])
        fk_area_resp = GestionarObra.AreaResponsable.get(GestionarObra.AreaResponsable.nombre_area == elem[4])
        fk_comuna = GestionarObra.Comuna.get(GestionarObra.Comuna.nombre_comuna == elem[7])
        fk_barrio = GestionarObra.Barrio.get(GestionarObra.Barrio.nombre_barrio == elem[8])
        fk_contratacion = GestionarObra.ContratacionTipo.get(GestionarObra.ContratacionTipo.contratacion == elem[17])
        fk_financiamiento = GestionarObra.Financiamiento.get(GestionarObra.Financiamiento.financiamiento == elem[23])
        try:
            GestionarObra.ObraUrbana.create(entorno=elem[0], #elem[indice] hace referencia a la columna del dataframe
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
