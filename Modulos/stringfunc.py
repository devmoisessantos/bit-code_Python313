# This is a module:

"""Modulo para trabalhar com Strings."""

def inverterStr(string):
    """
    Retorna uma string com o texto recebido como parâmetro invertido.

    Parameters
    ----------
    string : str
        O texto a ser invertido.

    Returns
    -------
    str
        O texto invertido.
    """

    return f'O texto: {string} invertido é: {string[::-1]}'

def retornarStrPares(string):
    """
    Retorna uma string com as letras pares do texto
    recebido como parâmetro.

    Parameters
    ----------
    string : str
        O texto a ser processado.

    Returns
    -------
    str
        A string com as letras pares do texto.
    """
    string_pares = [
            f"{indice}: {letra}  "
            for indice, letra in enumerate(string) 
            if indice % 2 == 0
    ]
    mensagem = (
            f"As letras pares do texto = '{string}' é: {' '.join(string_pares)}"
        )
    return mensagem

def retornarStrImpares(string):
    """
    Retorna uma string com as letras pares do texto
    recebido como parâmetro.

    Parameters
    ----------
    string : str
        O texto a ser processado.

    Returns
    -------
    str
        A string com as letras pares do texto.
    """
    string_impares = [
            f"{indice}: {letra}  "
            for indice, letra in enumerate(string) 
            if indice % 2 != 0
    ]
    mensagem = (
            f"As letras pares do texto = '{string}' é: {' '.join(string_impares)}"
        )
    return mensagem