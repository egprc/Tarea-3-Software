# Creado en 01/02/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)
    

################################################################################
#####################  C A S O S   D E   P R U E B A  ##########################
################################################################################

import unittest
from classBilletera import *

class GlobalTester(unittest.TestCase):

    def testSaldo_Inicializacion(self):
        # Comprobar que el saldo al iniciar la billetera es de cero
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.saldo()
        self.assertEqual(res, 0, "El saldo no es cero al iniciar la cuenta.")

    def testConsumo_PinIncorrecto(self):
        # Se intenta realizar un consumo con un pin que no es el del usuario
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.recargar(500,"Feb 01 2017",4555)
        res = billetera.consumir(400,"Feb 01 2017",4555, "cont44")
        self.assertEqual(res, 0, "La funcion no esta detectando el pin incorrecto.")

    def testSaldo_Negativo(self):
        #Se verifica el saldo y resulta ser negativo
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.consumir(400,"Feb 01 2017",4555, "cont45")
        res = billetera.saldo()
        self.assertTrue(res >= 0, "La funcion registra saldos negativos.")

    def testConsumo_MenosSaldoQueMonto(self):
        # Se intenta realizar un consumo teniendo menos saldo que el monto a gastar
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.consumir(400,"Feb 01 2017",4555, "cont45")
        self.assertEqual(res, 0, "La funcion permite hacer consumos con menos saldo que el monto.")

    def testFecha_FormatoInvalido(self):
        # Comprobar que el programa no admite formatos de fecha no válidos
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(500,"02 01 2017",4555)
        self.assertEqual(res1, 0, "La funcion no detecta la fecha invalida.")
        res2 = billetera.recargar(500,"02 Jan 2017",4555)
        self.assertEqual(res2, 0, "La funcion no detecta la fecha invalida.")
        # Comprobar que el saldo sigue siendo cero
        res3 = billetera.saldo()
        self.assertEqual(res3, 0, "La funcion recargo saldo a pesar de la fecha invalida.")

    def testFecha_DiasInvalidos(self):
        # Comprobar que el programa no admite fechas inexistentes
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(500,"Feb 29 2017",4555)
        self.assertEqual(res1, 0, "La funcion no detecta la fecha inexistente.")
        res2 = billetera.recargar(500,"Jun 31 2017",4555)
        self.assertEqual(res2, 0, "La funcion no detecta la fecha inexistente.")

    def testFecha_AñosBisiestos(self):
        # Comprobar que el programa reconoce años bisiestos
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(500,"Feb 29 2004",4555)
        self.assertEqual(res1, 1, "La funcion no detecta años bisiestos.")
        res2 = billetera.recargar(500,"Feb 29 2012",4555)
        self.assertEqual(res2, 1, "La funcion no detecta años bisiestos.")

    def testInterno_Recarga(self):
        # Comprobar si la billetera lleva una correcta contabilidad del saldo
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.recargar(500,"Feb 01 2017",4555)
        res = billetera.consumir(200,"Feb 01 2017",4555, "cont45")
        res = billetera.recargar(400,"Feb 01 2017",4555)
        res = billetera.saldo()
        self.assertEqual(res, 700, "La funcion no contabiliza bien el saldo.")
        # Verificar que se contabilizaron todas las transacciones:
        numRecargas = len(billetera.listaCreditos)
        numConsumos = len(billetera.listaDebitos)
        self.assertEqual(numRecargas,2,"No se contabilizaron correctamente los creditos.")
        self.assertEqual(numConsumos,1,"No se contabilizaron correctamente los debitos.")

    def testExtremo_Saldo(self):
        # Comprobar que el programa vuelve a ser cero cuando el monto neto de las transacciones es nulo.
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(500,"Jan 31 2016",4555)
        res1 = billetera.consumir(400,"Feb 01 2017",4555, "cont45")
        res1 = billetera.recargar(900,"May 31 2018",4555)
        res1 = billetera.consumir(1000,"Feb 01 2017",4555, "cont45")
        res1 = billetera.saldo()
        self.assertEqual(res1, 0, "El saldo no volvio a ser cero.")

    def testTransaccion_Invalida(self):
        # Comprobar que no se permiten transacciones de montos negativos.
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(-500,"Jan 31 2016",4555)
        res2 = billetera.consumir(-400,"Mar 31 2016",4555, "cont45")
        self.assertEqual(res1, 0, "Se admiten transacciones negativas.")
        self.assertEqual(res2, 0, "Se admiten transacciones negativas.")
        # Comprobar que no se permiten transacciones de montos nulos
        res1 = billetera.recargar(0,"Jan 31 2016",4555)
        res2 = billetera.consumir(0,"Mar 31 2016",4555, "cont45")
        self.assertEqual(res1, 0, "Se admiten transacciones nulas.")
        self.assertEqual(res2, 0, "Se admiten transacciones nulas.")
        # Comprobar que no se permiten transacciones de montos no numericos
        res1 = billetera.recargar("Pepe","Jan 31 2016",4555)
        res2 = billetera.consumir("Jaime","Mar 31 2016",4555, "cont45")
        self.assertEqual(res1, 0, "Se admiten transacciones no numericas.")
        self.assertEqual(res2, 0, "Se admiten transacciones no numericas.")

    def testEsquina_TransaccionNoEntera(self):
        # Comprobar que se permiten transacciones con numeros decimales
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res1 = billetera.recargar(500,"Jan 31 2016",4555)
        res2 = billetera.consumir(400.9999,"Mar 31 2016",4555, "cont45")
        saldo = billetera.saldo()
        self.assertTrue(saldo > 0, "El saldo no se contabiliza correctamente cuando hay decimales.")
        
        
if __name__ == '__main__':
    unittest.main()
