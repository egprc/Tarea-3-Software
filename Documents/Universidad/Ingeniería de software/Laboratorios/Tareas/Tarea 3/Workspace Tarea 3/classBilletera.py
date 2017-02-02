# Creado en 01/02/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)


################################################################################
#####################  C L A S E S   A U X I L I A R E S  ######################
################################################################################

class fecha:
    def __init__(self,dia,mes,anio):
        pass

class transaccion:
    """ Servira para registrar un credito o un debito """
    def __init__(self,monto,fecha,id_local):
        pass

class billeteraElectronica:
    def __init__(self,identificador,nombre1,nombre2,apellido1,apellido2,ci,pin):
        pass

    def saldo(self):
        pass

    def recargar(self,monto,fecha,id_local):
        pass

    def consumir(self,monto,fecha,id_local, pin_usuario):
        pass
            

################################################################################
#####################  R U T I N A   P R I N C I P A L  ########################
################################################################################

class rutinaPrincipal():
    def ejecutar(self):
        pass