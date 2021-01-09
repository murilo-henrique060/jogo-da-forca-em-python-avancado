def linha(simb='=',tam=42):
    """[Cria uma linha]

    Args:
        simb (str, optional): [O símbolo que Vai Formar a linha]. Defaults to '='.
        tam (int, optional): [Tamanho da Linha]. Defaults to 42.
    Criado por:
        Murilo_Henrique060
    """
    print(f'{simb}'*tam)
def cabeçalho(simb='=',txt='ESCREVA O CABEÇALHO',tam=0):
    """[Cria um Cabeçalho, com uma linha em cima, o texto e uma linha em baixo.]

    Args:
        simb (str, optional): [O símbolo que vai formar as linhas]. Defaults to '='.
        txt (str, optional): [O texto Do Cabeçalho]. Defaults to 'ESCREVA O CABEÇALHO'.
        tam (int, optional): [O tamanho do cabeçalho, 0 = acompanha o tamanho do texto]. Defaults to 0
    Criado por:
        Murilo_Henrique060
    """
    if tam <= 0:
        linha(f'{simb}',(len(txt)+4))
        print(f'  {txt}')
        linha(f'{simb}',(len(txt)+4))
    else:
        linha(f'{simb}',tam)
        print(f'{" "*((tam-len(txt))//2)}{txt}')
        linha(f'{simb}',tam)
def leiaInt(numero):
    try:
        num = int(numero)
    except:
        print('ERRO! Digite um número inteiro válido')
        leiaInt(input('Digite sua opção: '))
    else:
        return num
def leiaInRange(numero=0,n1=0,n2=1,outRange='ERRO! Número Fora Do Alcance.',cor=False):
    """[Verifica se Um Número Está Dentro de um Range.]

    Args:
        numero (int, optional): [Númaero à Ser Verificado.]. Defaults to 0.
        n1 (int, optional): [começo do range]. Defaults to 0.
        n2 (int, optional): [final do range]. Defaults to 1.
        outRange (str, optional): [Mensagem se o número Estiver Fora do Range]. Defaults to 'ERRO! Número Fora Do Alcance.'.
        cor (bool, optional): [Adicionar ou Não Cores]. Defaults to False.

    Returns:
        [bool]: [retorna True ou False]
    Criado por:
        Murilo_Henrique060
    """
    if cor:
        from colorama import init
        init()
    v = 0
    for n in range(n1,n2+1):
        if n == numero:
            v += 1
    if v != 1:
        print(outRange)
        return False
    else:
        return True
def menu(lista,cabecalho):
    cabeçalho(cabecalho)
    c = 1
    for itens in lista:
        print(f'{c} - {itens}')
        c += 1
    linha('=',42)
    o