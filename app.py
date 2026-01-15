from flask import Flask, render_template, request

# Importações de funções utilitárias do projeto
from utils.text_cleaner import limpar_texto
from utils.huggingface_client import classificar_email
from utils.openai_client import gerar_resposta
from utils.validators import processar_entrada_email

# ============================================================
# Configuração da aplicação Flask
# ============================================================

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Rota principal da aplicação.

    Esta rota permite que o usuário:
    - Cole manualmente o texto de um email no formulário
    - Envie um arquivo (.txt ou .pdf) contendo o email

    Fluxo de processamento:
    1. Valida e processa a entrada do usuário (texto ou arquivo)
    2. Limpa e normaliza o texto
    3. Classifica o email (Produtivo ou Improdutivo)
    4. Gera uma resposta automática com base na classificação

    Returns:
        Template HTML renderizado com:
        - Categoria do email
        - Resposta gerada por IA
        - Mensagens de erro, se houver
    """

    # Variáveis que serão enviadas para o template
    categoria = None
    resposta = None
    mensagem = None
    

    # Verifica se a requisição é do tipo POST (envio do formulário)
    if request.method == "POST":

        # Processa e valida a entrada do usuário
        # Retorna o texto do email ou uma mensagem de erro
        texto, mensagem = processar_entrada_email(request)
        
        # Caso exista mensagem de erro, retorna o template imediatamente
        if mensagem:
            return render_template(
                "index.html",
                mensagem=mensagem
            )

        # Normaliza e limpa o texto recebido
        texto = limpar_texto(texto)

        # Classifica o email utilizando IA
        categoria = classificar_email(texto)

        # Gera uma resposta automática baseada na categoria
        resposta = gerar_resposta(texto, categoria)

    # Renderiza o template principal com os dados processados
    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta, 
        mensagem=mensagem
    )


# ============================================================
# Execução da aplicação
# ============================================================

if __name__ == "__main__":
    # Executa a aplicação Flask em modo de desenvolvimento
    app.run(debug=True)
