# Creado en 01/02/2017
# Autores: Stephanie Espinoza (09-11100)
#          Ronald Becerra     (12-10706)
    

################################################################################
#####################  C A S O S   D E   P R U E B A  ##########################
################################################################################

import unittest
from classBilletera import *

class GlobalTester(unittest.TestCase):

    def testConsumo_PinIncorrecto(self):
        """Se intenta realizar un consumo con un pin que no es el del usuario"""
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.recargar(500,"20 01 2017",4555)
        res = billetera.consumir(400,"20 01 2017",4555, "cont44")
        self.assertEqual(res, 0, "La funcion no esta detectando el pin incorrecto.")

    def testSaldo_Negativo(self):
        """Se verifica el saldo y resulta ser negativo"""
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.consumir(400,"20 01 2017",4555, "cont45")
        res = billetera.saldo()
        self.assertTrue(res >= 0, "La funcion registra saldos negativos.")

    def testConsumo_MenosSaldoQueMonto(self):
        """Se intenta realizar un consumo teniendo menos saldo que el monto a gastar"""
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.consumir(400,"20 01 2017",4555, "cont45")
        self.assertEqual(res, 0, "La funcion permite hacer consumos con menos saldo que el monto.")

    def testRecarga(self):
        """Comprobar si la billetera lleva una correcta contabilidad del saldo"""
        billetera = billeteraElectronica(34,"Ronald","Alfonso","Becerra","Gil",23714250,"cont45")
        res = billetera.recargar(500,"20 01 2017",4555)
        res = billetera.consumir(200,"20 01 2017",4555, "cont45")
        res = billetera.recargar(400,"20 01 2017",4555)
        res = billetera.saldo()
        self.assertEqual(res, 700, "La funcion no contabiliza bien el saldo.")
        
if __name__ == '__main__':
    unittest.main()


