class Obra:
  def __init__(self):
    self.entorno
    self.etapa = "Proyecto"  # Inicia predetermiandamente
    self.tipo_obra
    self.area_responsable
    self.nombre
    self.descripcion
    self.monto_contrato
    self.comuna
    self.direccion
    self.fecha_inicio
    self.fecha_fin_inicial
    self.plazo_meses = 0 # inicia predeterminadamente 
    self.porcentaje_avance
    self.imagen
    self.licitacion_oferta_empresa
    self.licitacion_anio
    self.contratacion_tipo
    self.nro_contratacion
    self.cuit_contratista
    self.mano_obra
    self.destacada
    self.expediente_numero
    self.financiamiento

  #DECORADORES
  @property
  def entorno(self):
    return self.__entorno
  @entorno.setter
  def entorno(self, valor):
    self.__entorno = valor

  @property
  def etapa(self):
    return self.__etapa
  @etapa.setter
  def etapa(self, valor = 4):
      self.__etapa = valor 

  @property
  def tipo_obra(self):
    return self.__tipo_obra
  @tipo_obra.setter
  def tipo_obra(self, valor):
    self.__tipo_obra = valor
    
  @property
  def area_responsable(self):
    return self.__area_responsable
  @area_responsable.setter
  def area_responsable(self, valor):
    self.__area_responsable = valor

  @property
  def nombre(self):
    return self.__nombre
  @nombre.setter
  def nombre(self, valor):
    self.__nombre = valor

  @property
  def descripcion(self):
    return self.__descripcion
  @descripcion.setter
  def descripcion(self, valor):
    self.descripcion = valor

  @property
  def monto_contrato(self):
        return self.__monto_contrato
    
  @monto_contrato.setter 
  def monto_contrato(self, valor):
      self.__monto_contrato = valor

  @property
  def comuna(self):
      return self.__comuna
  
  @comuna.setter
  def comuna(self, valor):
      self.__comuna = valor

  @property
  def direccion(self):
      return self.__direccion
  
  @direccion.setter
  def direccion(self, valor):
      self.__direccion = valor

  @property
  def fecha_inicio(self):
      return self.__fecha_inicio
  
  @fecha_inicio.setter
  def fecha_inicio(self, valor):
      self.__fecha_inicio = valor

  @property
  def fecha_fin_inicial(self):
      return self.__fecha_fin_inicial
  
  @fecha_fin_inicial.setter
  def fecha_fin_inicial(self, valor):
      self.__fecha_fin_inicial = valor

  @property
  def plazo_meses(self):
      return self.__plazo_meses
  
  @plazo_meses.setter
  def plazo_meses(self, valor = 0 ):
      self.__plazo_meses = valor

  @property
  def porcentaje_avance(self):
      return self.__porcentaje_avance
  
  @porcentaje_avance.setter
  def porcentaje_avance(self, valor):
      self.__porcentaje_avance = valor

  @property
  def imagen(self):
      return self.__imagen
  
  @imagen.setter
  def imagen(self, valor):
      self.__imagen = valor

  @property
  def licitacion_oferta_empresa(self):
      return self.__licitacion_oferta_empresa
  
  @licitacion_oferta_empresa.setter
  def licitacion_oferta_empresa(self, valor):
      self.__licitacion_oferta_empresa = valor

  @property
  def licitacion_anio(self):
      return self.__licitacion_anio
  
  @licitacion_anio.setter
  def licitacion_anio(self, valor):
      self.__licitacion_anio = valor

  @property
  def contratacion_tipo(self):
      return self.__contratacion_tipo
  
  @contratacion_tipo.setter
  def contratacion_tipo(self, valor):
      self.__contratacion_tipo = valor

  @property
  def nro_contratacion(self):
      return self.__nro_contratacion
  
  @nro_contratacion.setter
  def nro_contratacion(self, valor):
      self.__nro_contratacion = valor

  @property
  def cuit_contratista(self):
      return self.__cuit_contratista
  
  @cuit_contratista.setter
  def cuit_contratista(self, valor):
      self.__cuit_contratista = valor

  @property
  def mano_obra(self):
      return self.__mano_obra
  
  @mano_obra.setter
  def mano_obra(self, valor):
      self.__mano_obra = valor

  @property
  def destacada(self):
      return self.__destacada
  
  @destacada.setter
  def destacada(self, valor):
      self.__destacada = valor

  @property
  def expediente_numero(self):
      return self.__expediente_numero
  
  @expediente_numero.setter
  def expediente_numero(self, valor):
      self.__expediente_numero = valor

  @property
  def financiamiento(self):
      return self.__financiamiento
  
  @financiamiento.setter
  def financiamiento(self, valor):
      self.__financiamiento = valor

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


