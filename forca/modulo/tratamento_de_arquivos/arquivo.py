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
        for linhas in a:
            palavras = linhas.split(',')
            for pala in palavras:
                lista.append(pala)
        return lista
    a.close()
def adicionarPalavra(nome,palavra):
    """[adiciona uma palavra a um arquivo]

    Args:
        nome ([str]): [nome do arquivo]
        palavra ([]): [description]
    """
    try:
        a = open(nome,'at')
    except:
        print('Erro ao adicionar nova palavra.')
    else:
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
                            for numero,itens in enumerate(lista):
                                if numero == 0:
                                    a.write(f'{itens}')
                                else:
                                    a.write(f',{itens}')
                            print('Palavra Removida Com Sucesso')
            else:
                print('palavra não encontrada')