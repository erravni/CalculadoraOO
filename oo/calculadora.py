import math

class OperacaoNaoEncontrada(Exception):
    pass

class Operacao:
    def __call__(self, operandos):
        raise NotImplementedError()

class Soma(Operacao):
    def __call__(self,operandos):
        return operandos[0]+operandos[1]
class Subtracao(Operacao):
    def __call__(self,operandos):
        return operandos[0]-operandos[1]
class Produto(Operacao):
    def __call__(self, operandos):
        return operandos[0] * operandos[1]
class Divisao(Operacao):
    def __call__(self, operandos):
        return operandos[0] / operandos[1]
class Elevadoadois(Operacao):
    def __call__(self, operandos):
        return operandos[0] ** 2
class Elevadoatres(Operacao):
    def __call__(self, operandos):
        return operandos[0] ** 3
class RaizQuadrada(Operacao):
    def __call__(self, operandos):
        return math.sqrt(operandos[0])
class RaizCubica(Operacao):
    def __call__(self, operandos):
        return int(round(operandos[0] ** (1./ 3)))
class Log(Operacao):
    def __call__(self, operandos):
        return math.log(operandos[0])


class Calculadora:

    def __init__(self):
        self.operacoes = {}
        self.adicionar_operacao('+', Soma())
        self.adicionar_operacao('-', Subtracao())
        self.adicionar_operacao('*', Produto())
        self.adicionar_operacao('/', Divisao())
        self.adicionar_operacao('^2', Elevadoadois())
        self.adicionar_operacao('^3', Elevadoatres())
        self.adicionar_operacao('RQ', RaizQuadrada())
        self.adicionar_operacao('RC', RaizCubica())
        self.adicionar_operacao('Log', Log())



    def adicionar_operacao(self,sinal,operacao):
        self.operacoes[sinal] = operacao

    def calcular(self):
        operandos = []
        operandos.append(float(input('Digite o primeiro numero:')))
        operandos.append(float(input('***Digite 0 para cálculos com apenas um número*** Digite o segundo numero: ' )))
        sinal = input('Digite o sinal da operação: ')
        try:
            operacao = self.operacoes[sinal]
            resultado = operacao(operandos)
        except KeyError as e:
            raise OperacaoNaoEncontrada(f'Operação não encontrada') from e
        return resultado

