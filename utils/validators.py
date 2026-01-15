from utils.pdf_reader import ler_pdf


def processar_entrada_email(request):
    """
    Processa e valida a entrada do formulário de email.

    A função é responsável por:
    - Identificar se o usuário forneceu texto manualmente
    - Identificar se o usuário enviou um arquivo (.txt ou .pdf)
    - Extrair o conteúdo textual do email
    - Validar se a entrada é válida

    Nenhuma renderização de template é realizada aqui.
    A função apenas retorna os dados processados ou uma mensagem de erro,
    permitindo que a rota Flask controle o fluxo da aplicação.

    Args:
        request (flask.Request):
            Objeto de requisição Flask contendo os dados do formulário.

    Returns:
        tuple:
            (texto, mensagem)

            - texto (str | None):
                Conteúdo do email extraído e validado.
            - mensagem (str | None):
                Mensagem de erro caso a validação falhe.
    """

    # Inicializa as variáveis de retorno
    texto = None
    mensagem = None

    # Texto inserido manualmente pelo usuário
    if request.form.get("email_text"):
        texto = request.form.get("email_text")

    # Arquivo enviado pelo usuário
    elif request.files.get("email_file"):
        arquivo = request.files["email_file"]

        # Arquivo enviado sem nome
        if arquivo.filename == "":
            mensagem = "Por favor, insira um texto ou envie um arquivo."
            return None, mensagem

        # Leitura de arquivo .txt
        if arquivo.filename.endswith(".txt"):
            texto = arquivo.read().decode("utf-8")

        # Leitura de arquivo .pdf
        elif arquivo.filename.endswith(".pdf"):
            texto = ler_pdf(arquivo)

        # Qualquer outro tipo de arquivo não suportado
        else:
            mensagem = "Formato de arquivo não suportado. Use .txt ou .pdf."
            return None, mensagem

    # Validação final: nenhuma entrada válida fornecida
    if not texto or not texto.strip():
        mensagem = "Por favor, insira um texto ou envie um arquivo para análise."
        return None, mensagem
    
    # Retorna o texto válido e nenhuma mensagem de erro
    return texto, None
