# Creado en 25/01/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)

from calendar import*
import datetime
import sys

################################################################################
#########  C L A S E S   Y   F U N C I O N E S   A U X I L I A R E S  ##########
################################################################################


class momento:
    def __init__(self,dia=0,mes=0,anio=0,hora=0,minuto=0):
        self.dia    = dia
        self.mes    = mes
        self.anio   = anio 
        self.hora   = hora    # Va desde 0 hasta 23
        self.minuto = minuto  # Va desde 0 hasta 59
        self.diaSemana = None

class tarifa:
    def __init__(self,tasaDiaNormal,tasaFinSemana):
        self.tasaDiaNormal = tasaDiaNormal
        self.tasaFinSemana = tasaFinSemana

################################################################################
#########  C L A S E S   Y   F U N C I O N E S   A U X I L I A R E S  ##########
################################################################################

def recibirEntrada(diaIni,mesIni,anioIni,horaIni,minIni,diaFin,mesFin,anioFin,horaFin,minFin,tasNorm,tasFin):
    inicioDeServicio = momento()
    inicioDeServicio.dia = diaIni
    inicioDeServicio.mes = mesIni
    inicioDeServicio.anio = anioIni
    inicioDeServicio.anio = horaIni
    inicioDeServicio.anio = minIni

    finDeServicio = momento()
    finDeServicio.dia = diaFin
    finDeServicio.mes = mesFin
    finDeServicio.anio = anioFin
    finDeServicio.hora = horaFin
    finDeServicio.minuto = minFin
    
    tarifa = tarifa()
    tarifa.tasaDiaNormal = tasNorm
    tarifa.tasaFinSemana = tasFin
    
    return inicioDeServicio, finDeServicio, tarifa

def calcularTiempoServicio(inicioDeServicio,finDeServicio):
    final = datetime.datetime(finDeServicio.anio,finDeServicio.mes,finDeServicio.dia,finDeServicio.hora,finDeServicio.minuto)
    inicio = datetime.datetime(inicioDeServicio.anio,inicioDeServicio.mes,inicioDeServicio.dia,inicioDeServicio.hora,inicioDeServicio.minuto)
    
    return final-inicio, inicioDeServicio, finDeServicio

def funcionTecho(numero):
    if numero == int(numero):
        return numero
    else:
        return numero+1
    
def calcularPrecio(tarifa, tiempoDeServicio):       
    numDiasTotales = tiempoDeServicio[0].days
    numMinutosExtra = tiempoDeServicio[0].seconds//60
    numHorasExtra = funcionTecho(tiempoDeServicio[0].seconds//3600)
     
    try:
        assert((numDiasTotales < 7) or (numDiasTotales==7 and numMinutosExtra == 0))
    except:
        print("El tiempo de servicio debe ser menor a siete días")
        
    diaInicio = tiempoDeServicio[1]
    diaFin = tiempoDeServicio[2]
    diaSemanaInicio = weekday(diaInicio.anio,diaInicio.mes,diaInicio.dia)
    diaSemanaFin = weekday(diaFin.anio,diaFin.mes,diaFin.dia)

    if (numDiasTotales == 0) and (numMinutosExtra < 15):
        precio = 0
    
    else:
        if (diaSemanaInicio in [5,6]) and (diaSemanaFin in [5,6]) and (True):
            precio = tarifa.tasaDiaNormal * numHorasExtra
        else:
            precio = tarifa.tasaFinSemana * numHorasExtra
                    
        elif (diaSemanaInicio in [5,6]) and (diaSemanaInicio in [5,6]) and (numDiasTotales < 2):
            precio = tasaFinSemana


################################################################################
#####################  R U T I N A   P R I N C I P A L  ########################
################################################################################

def rutinaPrincipal(diaIni,mesIni,anioIni,horaIni,minIni,diaFin,mesFin,anioFin,horaFin,minFin,tasNorm,tasFin):
    
    (inicioDeServicio,finDeServicio,tarifa) = recibirEntrada(diaIni,mesIni,anioIni,horaIni,minIni,diaFin,mesFin,anioFin,horaFin,minFin,tasNorm,tasFin)
    tiempoDeServicio = calcularTiempoServicio(inicioDeServicio, finDeServicio)
    precio = calcularPrecio(tarifa, tiempoDeServicio)
    
    print("El precio a pagar es:", precio)
    

################################################################################
#####################  C A S O S   D E   P R U E B A ###########################
################################################################################

import unittest
from stack import*

class PrecioTester(unittest.TestCase):
    
    def testUnSoloDiaDeSemanaMenos15(self):
        precio = rutinaPrinicipal(26,1,2017,4,0,26,1,2017,4,5,20,30)
        assertEquals(0,precio,"No da cero, como debería.")
        
    def testUnSoloDiaDeSemanaMas15(self):
        precio = rutinaPrinicipal(26,1,2017,4,0,26,1,2017,4,20,20,30)
        assertEquals(20,precio,"No da el precio de una sola hora de día normal.")
        
    def testUnSoloDiaFinSemanaMas15(self):
        precio = rutinaPrinicipal(28,1,2017,4,0,28,1,2017,4,20,20,30)
        assertEquals(30,precio,"No da el precio de una sola hora de fin de semana.")
            
    def testCasoMaximoMenorValor(self):
    
        
    def testCasoMaximoMenorValor(self):
        
    def testCasoMalicia1(self):
        
    def testCasoMalicia2(self):