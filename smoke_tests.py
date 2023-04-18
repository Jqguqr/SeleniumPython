from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_test import SearchTest

# Variables qeu contienesn los test
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

# Se construye la suit de pruebas
smoke_test = TestSuite([assertions_test, search_test])

# Variable que contien los parametros para generar el reporte
kwargs = {
    "output": 'smoke-report'
}

# Variable para correr los test
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
