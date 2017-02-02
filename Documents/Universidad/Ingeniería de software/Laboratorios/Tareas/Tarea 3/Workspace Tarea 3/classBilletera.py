# Creado en 01/02/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)

#!/usr/bin/python
# -*- coding: <encoding name> -*-

from datetime import datetime
import sys

################################################################################
#####################  C L A S E S   A U X I L I A R E S  ######################
################################################################################

class fechaMetodo:
    def __init__(self,string):
        try:
            datetime_object = datetime.strptime(string, '%b %d %Y')
            return datetime_object
        except:
            print("La fecha debe contener: mes (tres letras iniciales), día y año.")
            return 0
            
class transaccion:
    """ Servira para registrar un credito o un debito """
    def __init__(self,monto,fecha,id_local):
        self.monto = monto
        try:
            self.fecha = datetime.strptime(fecha, '%b %d %Y')
        except:
            self.fecha = None
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

    def recargar(self,monto,fecha,id_local):
        try:
            assert((monto == float(monto)) and (monto > 0))
        except:
            print("El monto a recargar debe ser un entero positivo.")
            return 0
        credito = transaccion(monto,fecha,id_local)
        if credito.fecha == None:
            print("Fecha no válida")
            print("El formato de la fecha debe ser: mes (tres letras iniciales), dia, anio.")
            return 0
        else:
            self.listaCreditos.append(credito)
            self.balanceActual += monto
            print("El saldo fue recargado exitosamente.")
            return 1

    def consumir(self,monto,fecha,id_local, pin_usuario):
        try:
            assert((monto == float(monto)) and (monto > 0))
        except:
            print("El monto a recargar debe ser un entero positivo.")
            return 0
        if pin_usuario != self.pin:
            print("El pin ingresado no es valido.")
            return 0
        elif monto > self.balanceActual:
            print("No posee saldo suficiente para realizar este consumo.")
            return 0
        else:
            debito = transaccion(monto,fecha,id_local)
            if debito.fecha == None:
                print("Fecha no válida.")
                print("El formato de la fecha debe ser: mes (tres letras iniciales), dia, anio.")
                return 0
            else:
                debito.pin = pin_usuario
                self.listaDebitos.append(debito)
                self.balanceActual -= monto
                print("El consumo fue realizado exitosamente.")
                return 1
