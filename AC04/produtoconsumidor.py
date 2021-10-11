
from threading import Thread, Condition
import time
import random

prateleiraMercado = []
controladorFila = Condition()


class Produto(Thread):
    def run(self):
        produtos = ["carne", "ovo", "arroz", "feijão", "macarrão", "banana",
                    "maça", "miojo", "abacaxi", "laranja", "cerveja", "vinho",
                    "cachaça", "creme de leite", "leite condensado", "frango",
                    "café", "óleo", "açucar", "leite", "sal", "detergente",
                    "chocolate", "batata", "cenoura", "quiabo", "acerola",
                    "agua", "suco", "refrigerante", "xuxu", "pepino"]
        global prateleiraMercado
        while True:
            produto = random.choice(produtos)
            controladorFila.acquire()
            prateleiraMercado.append(produto)
            print("Funcionário: Repositor incluiu", produto, "na prateleira.")
            controladorFila.notify()
            controladorFila.release()
            time.sleep(random.random())


class Consumidor(Thread):
    def run(self):
        global prateleiraMercado
        while True:
            controladorFila.acquire()
            if not prateleiraMercado:
                print("Prateleira sem produtos, cliente aguardando repositor.")
                controladorFila.wait()
            produto = prateleiraMercado.pop(0)
            print("Consumidor: Cliente pegou", produto, "da prateleira.")
            controladorFila.release()
            time.sleep(random.random())
