from modulo.tratamento_de_arquivos.arquivo import criarArquivo, arquivoExiste, lerArquivo, adicionarPalavra
from modulo.tratamento_de_strings.coisas_estéticas import cabeçalho, linha
arq = 'palavras.txt'
e = arquivoExiste(arq)
if not e:
    linha('=',42)
    criarArquivo(arq,str(input('Primeira palavra: ')))
cabeçalho('=','JOGO DA FORCA',42)
