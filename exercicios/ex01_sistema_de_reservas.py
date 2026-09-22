"""
====================================================================
PROJETO: Sistema de Reservas de Apartamentos
AULA / DISCIPLINA: Algoritmos e Programação / Engenharia de Software
====================================================================
Descrição:
    Sistema interativo via terminal para reserva de apartamentos,
    calculando o valor da diária conforme o número de hóspedes e
    o tipo de apartamento.

Conceitos e tecnologias:
    - Módulos: locale, datetime, time e os
    - Funções: def e return
    - Estruturas condicionais: if
    - Entrada e saída de dados
    - Formatação de valores, datas e terminal
====================================================================
"""
import os
import time
import locale #importação da ferramenta de conversão de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #solicitação para usar o padrão especificado
def moeda(valor):
    return locale.currency(valor, grouping=True, symbol=True)
#DEF: criação de função / atalho de tarefa.
#RETURN: informação a ser entregue com o processamento da função
from datetime import datetime #aplicação de hora e data
azul='\033[1;34m'
verde='\033[1;32m'
magneta='\033[1;35m'
fimcor='\033[0m'
arte1=f'''
 _________________________________________________________
|    ╭─╴╭─╮╷  ╭─╮╭╮╷╷╭─╮   ╶┬╮╭─╴   ╭─╴╭─╴╭─╮╷╭─╮╭─╮      |
|    │  │ ││  │ ││╰┤│├─┤    ││├╴    ├╴ ├╴ ├┬╯│├─┤╰─╮      |
|    ╰─╴╰─╯╰─╴╰─╯╵ ╵╵╵ ╵   ╶┴╯╰─╴   ╵  ╰─╴╵╰╴╵╵ ╵╰─╯      |
| ╭─╮╷╭─╮╶┬╴╭─╴╭┬╮╭─╮   ╶┬╮╭─╴   ╭─╮╭─╴╭─╮╭─╴╭─╮╷ ╷╭─╮╭─╮ |
| ╰─╮│╰─╮ │ ├╴ │││├─┤    ││├╴    ├┬╯├╴ ╰─╮├╴ ├┬╯│╭╯├─┤╰─╮ |
| ╰─╯╵╰─╯ ╵ ╰─╴╵ ╵╵ ╵   ╶┴╯╰─╴   ╵╰╴╰─╴╰─╯╰─╴╵╰╴╰╯ ╵ ╵╰─╯ |
|          ╭╮ ╭─╴╭┬╮   ╷ ╷╷╭╮╷╶┬╮╭─╮╭╴╭─╮╶╮╷              |
|          ├┴╮├╴ │││╶─╴│╭╯││╰┤ │││ ││ ├─┤ │╵              |
|          ╰─╯╰─╴╵ ╵   ╰╯ ╵╵ ╵╶┴╯╰─╯╰╴╵ ╵╶╯╵              |
|_________________________________________________________|
         '''
print(arte1)
print(f'''
Olá, esse é o sistema de reservas!

Segue algumas informações: 
- Cada funcionário pode reservar somente {azul}UM{fimcor} apartamento por período.
- Cada apartamento podem ficar até {azul}SEIS{fimcor} pessoas.
- Possuímos {azul}DOIS{fimcor} tipos de apartamentos.
''')
aceite=input('Você está de acordo com as informações? Responda Sim ou Não: ').strip().title()
os.system('cls') #após a resposta o que está acima será apagado do terminal
if aceite=='Sim':
    resultado='Obrigado! Vamos apresentar as informações para reserva: '
    print(resultado)
else:
    resultado='Não é possível prosseguir sem estar de acordo com as informações passadas. Atendimento finalizado.'
    print(resultado)
    exit()
#pra tabela usei 1tab/ 4 tab / 4 tab - 1
dadosimportantes=f'''
Qtd. pessoas        Diária             Diária 
no apartamento      {azul}Tipo 1             Tipo 2{fimcor}

    1             {moeda(20)}    |      {moeda(25)}  
    2             {moeda(28)}    |      {moeda(34)}  
    3             {moeda(35)}    |      {moeda(42)}  
    4             {moeda(42)}    |      {moeda(50)}  
    5             {moeda(48)}    |      {moeda(57)}  
    6             {moeda(53)}    |      {moeda(63)}  
'''
print(dadosimportantes)
ap=int(input('Informe o nº de pessoas no apartamento a ser reservado: ')) 
tipo=int(input('''Agora, informe o tipo de diária desejada 
Digite o tipo (1 ou 2): '''))
if ap==1 and tipo==1:
    escolha=20
if ap==1 and tipo==2:
    escolha=25
if ap==2 and tipo==1:
    escolha=ap*28
if ap==2 and tipo==2:
    escolha=ap*34
if ap==3 and tipo==1:
    escolha=ap*35
if ap==3 and tipo==2:
    escolha=ap*42
if ap==4 and tipo==1:
    escolha=ap*42
if ap==4 and tipo==2:
    escolha=ap*50
if ap==5 and tipo==1:
    escolha=ap*48
if ap==5 and tipo==2:
    escolha=ap*57
if ap==6 and tipo==1:
    escolha=ap*53
if ap==6 and tipo==2:
    escolha=ap*63
linha='='*50
os.system('cls')
print(linha)
print(f'''{magneta}{'PARABÉNS, RESERVA CONCLUÍDA!':^50}{fimcor}
{'AQUI ESTÃO SUAS INFORMAÇÕES: ':^50}''')
print(linha)
print('')
agora=datetime.now() #pego a hora deste momento do código
data=agora.strftime('%d/%m/%Y às %H:%M') #aplico a formatação
print(f'Apartamento reservado: {ap}')
time.sleep(1.0)
print(f'Tipo selecionado: {tipo}')
time.sleep(1.0)
print(f'Valor total da reserva: 💰 {verde}{moeda(escolha)}{fimcor}')
time.sleep(1.0)
print(f'''
Data de processamento da reserva: {data}.
{verde}Obrigado!{fimcor}
''')