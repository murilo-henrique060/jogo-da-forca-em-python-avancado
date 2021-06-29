from time import sleep
from modulo.tratamento_de_arquivos.arquivo import *
from modulo.tratamento_de_strings.coisas_estéticas import *
arq = 'palavras.txt'
e = arquivoExiste(arq)
if not e:
    linha('=',42)
    criarArquivo(arq,str(input('Primeira palavra: ')))
while True:
    opc = menu(['Acessar Banco De Palavras','Adicionar Palavra','Remover Palavra','Regras','Jogar','Sair'],'JOGO DA FORCA')
    linha()
    if opc == 1:
        pal = lerArquivo(arq)
        print(pal)
    elif opc == 2:
        adicionarPalavra(arq,'Nova Palavra: ')
    elif opc == 3:
        removerPalavra(arq,input('Palavra: '))
    elif opc == 4:
        regras()
    elif opc == 5:
        iniciarJogo(arq)
    else:
        break
    sleep(2)
print('Encerrando O Programa Jogo da forca...')
print('Volte Sempre.')
sleep(0.5)