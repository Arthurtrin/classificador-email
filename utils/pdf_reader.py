import PyPDF2


def ler_pdf(arquivo):
    """
    Lê o conteúdo textual de um arquivo PDF e retorna o texto extraído.

    A função percorre todas as páginas do PDF e concatena
    o texto encontrado em cada uma delas. Caso uma página
    não contenha texto extraível, ela é ignorada.

    Args:
        arquivo (file-like object):
            Arquivo PDF aberto em modo binário (ex: open('arquivo.pdf', 'rb')).

    Returns:
        str:
            Texto completo extraído do PDF.
    """

    # Inicializa o leitor de PDF a partir do arquivo informado
    leitor = PyPDF2.PdfReader(arquivo)

    # Variável que armazenará o texto extraído de todas as páginas
    texto = ""

    # Percorre todas as páginas do PDF
    for pagina in leitor.pages:
        # Extrai o texto da página atual
        # Caso não haja texto, evita erro adicionando string vazia
        texto += pagina.extract_text() or ""

    return texto
