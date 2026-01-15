import re


def limpar_texto(texto):
    """
    Normaliza e limpa um texto para facilitar o processamento posterior.

    A função realiza as seguintes etapas:
    - Converte todo o texto para letras minúsculas
    - Remove espaços em branco duplicados
    - Remove caracteres especiais e pontuações
    - Remove espaços em branco no início e no fim do texto

    Args:
        texto (str): Texto bruto a ser normalizado.

    Returns:
        str: Texto limpo e padronizado.
    """

    # Converte todo o texto para letras minúsculas
    texto = texto.lower()

    # Substitui múltiplos espaços em branco por um único espaço
    texto = re.sub(r"\s+", " ", texto)

    # Remove caracteres que não sejam letras, números ou espaços
    texto = re.sub(r"[^\w\s]", "", texto)

    # Remove espaços em branco no início e no fim do texto
    return texto.strip()
