from fila_normal import FilaNormal
from fila_proritaria import FilaPrioritaria

# fila_teste = FilaNormal()
# fila_teste.a
# fila_teste.atualizafila()
#
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(5))
print(fila_teste2.estatistica('10/01/1993', 123, 'detail'))
print(fila_teste2.estatistica('10/01/1993', 123, 'none'))
