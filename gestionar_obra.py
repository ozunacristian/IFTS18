from abc import ABC, abstractmethod
import extraer_datos as etl
import modelo_orm as orm
# definición de la clase abstracta “GestionarObra”
class GestionarObra(ABC):
  __dataFrame = None
  def __init__():
    pass
  
  @abstractmethod
  def extraer_datos():
    etl.funcion_extraer_datos()
    print("Extraer datos OK.")
    pass

  @abstractmethod
  def conectar_db():
    orm.funcion_conectar_db()
    print("DB conectada.")
    pass

  @abstractmethod
  def mapear_orm():
    orm.funcion_mapear_orm()
    print("ORM mapeado.")
    pass

  @abstractmethod
  def limpiar_datos():
    global __dataFrame
    __dataFrame = etl.funcion_limpiar()
    print("DataFrame limpio.")
    pass

  @abstractmethod
  def cargar_datos():
    global __dataFrame
    # Obtenemos valores únicos de cada columna.
    lista_etapas = list(__dataFrame['etapa'].unique())
    lista_tipoObras = list(__dataFrame['tipo'].unique())
    lista_area_resps = list(__dataFrame['area_responsable'].unique())
    lista_comunas = list(__dataFrame['comuna'].unique())
    lista_barrios = list(__dataFrame['barrio'].unique())
    lista_contratacion = list(__dataFrame['contratacion_tipo'].unique())
    lista_financiamiento = list(__dataFrame['financiamiento'].unique())
    # Cargamos tablas de consulta (lookups)

    # Etapa
    # TipoObra
    # AreaResponsable
    # Comuna
    # Barrio
    # ContratacionTipo
    # Financiamiento
    # ObraUrbana
    
    for elem in lista_etapas:
        try:
            orm.Etapa.create(nombre_etapa = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Etapa", e)
    print("Se han persistido las etapas en la BD.")
       
    for elem in lista_tipoObras:
        try:
            orm.TipoObra.create(tipo_obra = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla TipoObra", e)
    print("Se han persistido los tipos de obras en la BD.")

    for elem in lista_area_resps:
        try:
            orm.AreaResponsable.create(nombre_area = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla AreaResponsable", e)
    print("Se han persistido las áreas responsables en la BD.")

    for elem in lista_comunas:
        try:
            orm.Comuna.create(nombre_comuna = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Comuna", e)
    print("Se han persistido las comunas en la BD.")

    for elem in lista_barrios:
        try:
            orm.Barrio.create(nombre_barrio = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Barrio", e)
    print("Se han persistido los barrios en la BD.")

    for elem in lista_contratacion:
        try:
            orm.ContratacionTipo.create(contratacion = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla ContratacionTipo", e)
    print("Se han persistido los tipos de contrataciones en la BD.")

    for elem in lista_financiamiento:
        try:
            orm.Financiamiento.create(financiamiento = elem)
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla Financiamiento", e)
    print("Se han persistido los financiamientos en la BD.")


    # Cargamos la tabla principal ObraUrbana
    print("Recorremos las filas del archivo csv e insertamos los valores en la tabla 'viajes' de la BD")
    for elem in __dataFrame.values:
        # Se obtiene el id de la tabla lookup y lo guardamos en una variable.
        etapa = orm.Etapa.get(orm.Etapa.nombre_nombre == elem[1])
        try:
            orm.ObraUrbana.create(etapa=etapa,
                                  date=elem[1],
                                  parcial=elem[2],
                                  quantity=elem[3],
                                  )
        except orm.IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla viajes.", e)
    print("Se han persistido los viajes en sube en la BD.")


  @abstractmethod
  def nueva_obra():
    pass

  @abstractmethod
  def obtener_indicadores():
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
except Exception as e:
  print(e)
