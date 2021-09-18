import json
import requests
import time
from unittest import TestCase
import unittest


apontarErro = False


class CovidSP:
    def __init__(self, casos):
        self.casos = casos

    def casos_covid_sp(self):
        covid_sp = "https://covid19-brazil-api.now.sh\
/api/report/v1/brazil/uf/sp"
        response = requests.get(covid_sp)
        return response.json()

    def __repr__(self):
        return '<COVID: {}>'.format(self.casos)


class Testes(TestCase):
    def test_get_json(self):
        start = time.time()
        covidsp = CovidSP("Teste")
        result = covidsp.casos_covid_sp()
        with open('casos_covid_sp.json', 'w') as json_file:
            json.dump(result, json_file)
        end = time.time()
        execution_time = end - start
        print("O arquivo foi criado em %0.3f ms " % (execution_time * 1000.))

    def teste_dict(self):
        start = time.time()
        covidsp = CovidSP("Teste")
        result = covidsp.casos_covid_sp()
        end = time.time()
        execution_time = end - start
        print("O teste foi realizado em %0.3f ms " % (execution_time * 1000.))
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def teste_state(self):
        start = time.time()
        covidsp = CovidSP("Teste")
        result = covidsp.casos_covid_sp()
        end = time.time()
        execution_time = end - start
        print("O teste foi realizado em %0.3f ms " % (execution_time * 1000.))
        self.assertIsNotNone(result)
        self.assertEqual(result['state'], 'São Paulo')

    def teste_len_dict(self):
        start = time.time()
        covidsp = CovidSP("Teste")
        result = covidsp.casos_covid_sp()
        end = time.time()
        execution_time = end - start
        print("O teste foi realizado em %0.3f ms " % (execution_time * 1000.))
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 8)

    def teste_dict_equal(self):
        dict_teste = {"uid": 35, "uf": "SP", "state": "São Paulo",
                      "cases": 4325189, "deaths": 147811, "suspects": 5334,
                      "refuses": 596, "datetime": "2021-09-17T22:34:48.256Z"}
        start = time.time()
        covidsp = CovidSP("Teste")
        result = covidsp.casos_covid_sp()
        end = time.time()
        execution_time = end - start
        print("O teste foi realizado em %0.3f ms " % (execution_time * 1000.))
        self.assertIsNotNone(result)
        self.assertDictEqual(result, dict_teste)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity=2,
                            failfast=apontarErro).run(suite)


if __name__ == "__main__":
    runTests()
