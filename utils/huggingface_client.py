import os
import requests

# ============================================================
# Configuração de autenticação da API Hugging Face
# ============================================================

# Token de autenticação obtido a partir de variável de ambiente
# A variável HF_API_TOKEN deve estar configurada no sistema
HF_TOKEN = os.getenv("HF_API_TOKEN")

# Cabeçalhos padrão para requisições HTTP à API da Hugging Face
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# Endpoint do modelo de classificação zero-shot
# Modelo: facebook/bart-large-mnli
CLASSIFIER_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"


def safe_json(response):
    """
    Tenta converter a resposta HTTP para JSON de forma segura.

    Essa função evita que o sistema quebre caso a API
    retorne um conteúdo inválido ou inesperado.

    Args:
        response (requests.Response): Resposta HTTP da requisição.

    Returns:
        dict | list | None:
            - JSON convertido, caso seja válido
            - None, caso a conversão falhe
    """
    try:
        return response.json()
    except Exception:
        return None


def classificar_email(texto):
    """
    Classifica um texto de email como 'Produtivo' ou 'Improdutivo'
    utilizando um modelo de Zero-Shot Classification da Hugging Face.

    Args:
        texto (str): Conteúdo textual do email a ser classificado.

    Returns:
        str:
            - 'Produtivo' ou 'Improdutivo', conforme o maior score
            - 'Indefinido' em caso de erro na requisição ou resposta inválida
    """

    # Payload enviado para a API contendo o texto
    # e as categorias candidatas para classificação
    payload = {
        "inputs": texto,
        "parameters": {
            "candidate_labels": ["Produtivo", "Improdutivo"]
        }
    }

    # Realiza a requisição HTTP POST para o modelo
    response = requests.post(
        CLASSIFIER_URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    # Valida o status HTTP da resposta
    if response.status_code != 200:
        print("Erro HTTP classificação:", response.status_code, response.text)
        return "Indefinido"

    # Converte a resposta para JSON de forma segura
    result = safe_json(response)

    # Valida o formato esperado da resposta
    if not result or not isinstance(result, list):
        return "Indefinido"

    # Seleciona o rótulo com maior score de confiança
    melhor = max(result, key=lambda x: x["score"])

    return melhor["label"]
