# Creado en 01/02/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)



################################################################################
#####################  C L A S E S   A U X I L I A R E S  ######################
################################################################################

class fecha:
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
        
        if (dia != int(dia)) or (mes != int(mes)) or (anio != int(anio)):
            print("Las fechas solo pueden contener numeros enteros.")
            return 0
        if (dia < 1) or (dia > 31):
            print("Dia invalido.")
            return 0
        if (mes < 1) or (mes > 12):
            print("El mes debe estar entre 1 y 12.")
            return 0
        if mes not in [1,3,5,7,8,10,12]:
            if mes == 2:
                try: 
                    assert(dia <= 29)
                    return 1
                except:
                    print("Dia invalido para el mes")
                    return 0
            else:
                try: 
                    assert(dia <= 30)
                    return 1
                except:
                    print("Dia invalido para el mes")
                    return 0
        else:
            return 1

class transaccion:
    """ Servira para registrar un credito o un debito """
    def __init__(self,monto,fecha,id_local):
        self.monto = monto
        self.fecha = fecha
        self.id_local = id_local
        self.pin = None

class billeteraElectronica:
    def __init__(self,identificador,nombre1,nombre2,apellido1,apellido2,ci,pin):
        # Datos personales
        self.identificador = identificador
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.ci = ci
        self.pin = pin
        # Listas para almacenar creditos y debitos
        self.listaCreditos = []
        self.listaDebitos = []
        # Balance actual
        self.balanceActual = 0

    def saldo(self):
        print("El saldo actual es: "+str(self.balanceActual))
        return self.balanceActual

    def recargar(self,monto,dia,mes,anio,id_local):
        credito = transaccion(monto,fecha,id_local)
        self.listaCreditos.append(credito)
        self.balanceActual += monto
        print("El saldo fue recargado exitosamente.")
        return 1

    def consumir(self,monto,fecha,id_local, pin_usuario):
        if pin_usuario != self.pin:
            print("El pin ingresado no es valido.")
            return 0
        elif monto > self.balanceActual:
            print("No posee saldo suficiente para realizar este consumo.")
            return 0
        else:
            debito = transaccion(monto,fecha,id_local)
            debito.pin = pin_usuario
            self.listaCreditos.append(debito)
            self.balanceActual -= monto
            print("El consumo fue realizado exitosamente.")
            return 1
            

################################################################################
#####################  R U T I N A   P R I N C I P A L  ########################
################################################################################

class rutinaPrincipal():
    def ejecutar(self):
        pass