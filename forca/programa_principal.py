from modulo.tratamento_de_arquivos.arquivo import criarArquivo, arquivoExiste, lerArquivo, adicionarPalavra
arq = 'palavras.txt'
e = arquivoExiste(arq)
if not e:
    criarArquivo(arq)
adicionarPalavra(arq,str(input('Digite a nova palavra a ser adicionada: ')))
lerArquivo(arq)