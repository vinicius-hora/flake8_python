# from fila_normal import FilaNormal
# from fila_proritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

# fila_teste = FilaNormal()
# fila_teste.a
# fila_teste.atualizafila()
#
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

# fila_teste2 = FilaNormal()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# print(fila_teste2.chama_cliente(10))
# print(fila_teste2.chama_cliente(5))
# print(fila_teste2.estatistica('10/01/1993', 123, 'detail'))
# print(fila_teste2.estatistica('10/01/1993', 123, 'none'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaDetalhada('20/10/2022', 10)))
print(teste_fabrica.estatistica(EstatisticaDetalhada('20/10/2022', 10)))
