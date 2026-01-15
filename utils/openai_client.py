import os
from openai import OpenAI

# ============================================================
# Configuração do cliente OpenAI
# ============================================================

# Inicializa o cliente OpenAI utilizando a chave de API
# A variável de ambiente OPENAI_API_KEY deve estar configurada
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gerar_resposta(texto, categoria):
    """
    Gera uma resposta automática para um email utilizando a API da OpenAI.

    A resposta é construída com base no conteúdo do email e na
    categoria previamente definida (ex: Produtivo ou Improdutivo),
    garantindo um tom profissional, educado e objetivo.

    Args:
        texto (str): Conteúdo do email recebido.
        categoria (str): Categoria atribuída ao email.

    Returns:
        str:
            Texto da resposta gerada pelo modelo de linguagem.
    """

    # Prompt enviado ao modelo contendo o contexto do email
    # e as instruções para geração da resposta
    prompt = f"""
Você é um assistente profissional de uma empresa.

Categoria do email: {categoria}

Email recebido:
{texto}

Escreva uma resposta educada, clara e objetiva.
"""

    # Realiza a chamada à API de Chat Completion da OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente profissional."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )

    # Retorna o conteúdo textual da resposta gerada
    return response.choices[0].message.content.strip()
