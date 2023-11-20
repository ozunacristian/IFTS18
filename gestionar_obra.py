from abc import ABC, abstractmethod
# definición de la clase abstracta “GestionarObra”
class GestionarObra(ABC):
  def __init__():
    pass
  
@abstractmethod
class nuevo_proyecto():
  pass

@abstractmethod
class iniciar_contratacion():
  pass

@abstractmethod
class adjudicar_obra():
  pass

@abstractmethod
class iniciar_obra():
  pass

@abstractmethod
class actualizar_porcentaje_avance():
  pass

@abstractmethod
class incrementar_plazo():
  pass

@abstractmethod
class incrementar_mano_obra():
  pass

@abstractmethod
class finalizar_obra():
  pass

@abstractmethod
class rescindir_obra():
  pass

@abstractmethod
class obtener_indicadores():
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