def arquivoExiste(nome):
    """[Identifica se um arquivo existe.]

    Args:
        nome ([str]): [Nome do arquivo a ser identificado.]

    Returns:
        [bool]: [Retorna um valor boleano('True' ou 'False') se ele existe ou não.]
    criado por:
        Murilo-Henrique060
    """
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome,palavra):
    """[Cria um arquivo de texto.]

    Args:
        nome ([str]): [nome do arquivo a ser criado.]
        palavra([str]): [primeira palavra]
    Criado por:
        Murilo-Henrique060
    """
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print(f'Erro ao criar o arquivo {nome}.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
        try:
            a = open(nome,'at')
        except:
            print('Erro ao adicionar a primeira palavra.')
        else:
            try:
                a.write(f'{palavra}')
            except:
                print('Erro ao escrever a palavra')
            else:
                print('Nova palavra adicionada com sucesso.')
            a.close()
def lerArquivo(nome):
    """[lê um arquivo de texto e transforma a última linha em uma lista separada por ,]

    Args:
        nome ([str]): [nome do arquivo]

    Returns:
        [list]: [retorna uma lista dos arquivos]
    Criado por:
        Murilo-Henrique060
    """
    try:
        a = open(nome,'rt')
    except:
        print(f'Erro ao ler o arquivo {nome}')
    else:
        lista = []
        try:
            for linhas in a:
                linhas = linhas.replace('\n','')
                palavras = linhas.split(',')
                for pala in palavras:
                    lista.append(pala)
            n = lista.count('')
            if n > 0:
                for h in range(n):
                    lista.remove('')
            try:
                a.close()
                open(nome,'w').close()
            except:
                print('Erro ao apagar o arquivo')
            else:
                try:
                    a = open(nome, 'at')
                except:
                    print('Erro ao sobreescrever')
                else:
                    try:
                        for v, u in enumerate(lista):
                            if v == 0:
                                a.write(u)
                            else:
                                a.write(f',{u}')
                    except:
                        print('Erro ao escrever')
            return lista
        except:
            print('Erro ao ler a lista.')
    a.close()
def adicionarPalavra(nome,texto):
    """[adiciona uma palavra a um arquivo]

    Args:
        nome ([str]): [nome do arquivo]
        texto ([str]): [titulo do input da palavra a ser adicionada]
    """
    try:
        a = open(nome,'at')
    except:
        print('Erro ao adicionar nova palavra.')
    else:
        while True:
            l = lerArquivo(nome)
            palavra = str(input(texto)).strip()
            if palavra == '':
                print('='*42)
                print('Erro! Digite uma palavra.',end=' ')
                continue
            if palavra in l:
                print('='*42)
                print('Essa Palavra É Repetida. Tente Novamente.',end=' ')
                continue
            break
        try:
            a.write(f',{palavra}')
        except:
            print('Erro ao escrever a palavra')
        else:
            print('='*42)
            print('Nova palavra adicionada com sucesso.')
        a.close()
def removerPalavra(nome,palavra):
    try:
        lista = lerArquivo(nome)
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
            n = lista.count(palavra)
        except:
            print('Erro ao ler a palavra')
        else:
            if n != 0:
                try:
                    lista.remove(palavra)
                except:
                    print('Erro ao ler a posiçao do arquivo')
                else:
                    try:
                        open(nome,'w').close()
                    except:
                        print('Erro ao apagar o arquivo')
                    else:
                        try:
                            a = open(nome,'at')
                        except:
                            print('Erro ao sobreescrever')
                        else:
                            try:
                                for numero,itens in enumerate(lista):
                                    if numero == 0:
                                        a.write(f'{itens}')
                                    else:
                                        a.write(f',{itens}')
                            except:
                                print('Erro ao adicionar palavra')
                            else:
                                print('Palavra Removida Com Sucesso')
            else:
                print('palavra não encontrada')
def atualizartela(resposta,palavra,erros):
    print('')
    print('    |====|')
    print('    |    ',end='')
    if erros > 0:
        print('o',end='')
    print(' ')
    print('    |   ',end='')
    if erros == 2:
        print(' | ',end='')
    elif erros == 3:
        print(' |\\',end='')
    elif erros > 3:
        print('/|\\',end='')
    print(' ')
    print('    |   ',end='')
    if erros == 5:
        print('/',end='')
    elif erros > 5:
        print('/ \\',end='')
    print(' ')
    print('    |         ',end='')
    if len(resposta) == 0:
        for letras in palavra:
            if letras == ' ':
                print(' ',end='')
            else:
                print('_ ',end='')
        print(' ')
    else:
        for letras in palavra:
            letra = str(letras).upper()
            if letra in resposta:
                print(f'{letras} ',end='')
            else:
                if letras == ' ':
                    print(' ',end='')
                else:
                    print('_ ',end='')
        print(' ')
    print('  =====')
    print('')
    print('='*42)
def iniciarJogo(nome):
    from time import sleep
    from random import randint
    erros = 0
    resposta = []
    palavras = lerArquivo(nome)
    p = randint(0,(len(palavras)-1))
    palavra = palavras[p]
    while True:
        atualizartela(resposta,palavra,erros)
        if len(resposta) > 0:
            print(f' letras digitadas: {resposta}\n')
        r = str(input('Digite uma letra: ')).upper()[0]
        palavra2 = str(palavra).upper()
        if r not in palavra2:
            erros += 1
            print(f'Não Tem {r}. Você Tem {erros} Erros')
            sleep(1)
        resposta.append(r)
        print('='*42)
        cont = 1
        if erros == 6:
            atualizartela(resposta,palavra,erros)
            print(f'          VOCÊ PERDEU. A PALALAVRA ERA \'{palavra}\'')
            break
        for letras in palavra:
            letra = str(letras).upper()
            if letra in resposta or letra == ' ':
                cont *= 1
            else:
                cont *= 0
        if cont == 1:
            atualizartela(resposta,palavra,erros)
            print('          VOCÊ GANHOU!!!')
            break