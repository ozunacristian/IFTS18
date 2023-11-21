from abc import ABC, abstractmethod
import extraer_datos as etl
import modelo_orm as orm
# definición de la clase abstracta “GestionarObra”
class GestionarObra(ABC):
  def __init__():
    pass
  
  @abstractmethod
  def extraer_datos():
    etl.funcion_extraer_datos()
    pass

  @abstractmethod
  def conectar_db():
    orm.funcion_conectar_db()
    pass

  @abstractmethod
  def mapear_orm():
    orm.funcion_mapear_orm()
    pass

  @abstractmethod
  def limpiar_datos():
    etl.funcion_limpiar()
    pass

  @abstractmethod
  def cargar_datos():

    pass

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
    4
    e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
    f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.
    g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
    h. Porcentaje total de obras finalizadas.
    i. Cantidad total de mano de obra empleada.
    j. Monto total de inversión. """
    pass