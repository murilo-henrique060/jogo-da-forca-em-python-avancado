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
