# 📧 Classificador de Emails com Inteligência Artificial

Aplicação web desenvolvida em **Python + Flask** que utiliza **Inteligência Artificial** para:

- Classificar emails como **Produtivos** ou **Improdutivos**  
- Gerar **respostas automáticas inteligentes**  
- Aceitar entrada por **texto manual**, **arquivo `.txt`** ou **arquivo `.pdf`**  

O projeto foi estruturado de forma **modular**, seguindo boas práticas de organização, validação de dados e documentação de código, simulando um ambiente de produção.

---

## 🧠 Objetivo do Projeto

Este projeto tem como objetivo demonstrar, de forma prática:

- Uso de IA aplicada a problemas reais  
- Integração com APIs de IA ([Hugging Face](https://huggingface.co/) e [OpenAI](https://openai.com/))  
- Boas práticas de backend com Flask  
- Organização de código em camadas (`utils`)  
- Validação de entrada de dados  
- Geração de respostas automáticas baseadas em contexto  

---

## 🚀 Funcionalidades

- ✍️ Inserção manual de texto do email  
- 📄 Upload de arquivos `.txt`  
- 📑 Upload de arquivos `.pdf`  
- 🧹 Limpeza e normalização do texto  
- 🤖 Classificação automática do email (Produtivo / Improdutivo)  
- ✨ Geração de resposta automática baseada na classificação  
- ⚠️ Validação completa de entradas inválidas  
- 💬 Exibição de mensagens de erro amigáveis  
- 🌐 Interface web simples e objetiva  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**  
- **Flask**  
- **HTML5 / CSS3**  
- **OpenAI API**  
- **Hugging Face Transformers**  
- **Leitura de PDFs**  
- **Arquitetura modular**  
- **Boas práticas de documentação e validação**  

---

## 📂 Estrutura do Projeto



```text
email-classifier-ai/
│
├── app.py                     # Arquivo principal da aplicação Flask
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
│
├── templates/
│   └── index.html             # Interface web
│
├── static/
│   └── style.css              # Estilos da aplicação
│
├── utils/
│   ├── __init__.py
│   ├── validators.py          # Validação e processamento de entrada
│   ├── text_cleaner.py        # Limpeza e normalização de texto
│   ├── huggingface_client.py  # Classificação do email
│   ├── openai_client.py       # Geração de resposta automática
│   └── pdf_reader.py          # Leitura de arquivos PDF
```

---
## ⚙️ Pré-requisitos

Antes de iniciar, você precisa ter instalado:

- **Python 3.10 ou superior**  
- **pip**  
- **Virtualenv (recomendado)**  

---

## 🧪 Criação do Ambiente Virtual

```bash
# Clonar o repositório
git clone git@github.com:Arthurtrin/classificador-email.git

# Acessar o diretório do projeto
cd nome-do-projeto

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
```

---

## 🔐 Configuração de Variáveis de Ambiente

Para que a aplicação funcione corretamente, é necessário configurar as chaves de API da **OpenAI** e da **Hugging Face**.

### 1️⃣ Criando a OpenAI API Key

1. Acesse [OpenAI](https://platform.openai.com/) e faça login ou crie uma conta.  
2. No menu, clique em **View API Keys** ou vá para [API Keys](https://platform.openai.com/account/api-keys).  
3. Clique em **Create new secret key**.  
4. Copie a chave gerada (será algo como `sk-xxxxxxxxxxxxxxxxxxxx`) e guarde com segurança.  

### 2️⃣ Criando a Hugging Face API Token

1. Acesse [Hugging Face](https://huggingface.co/) e faça login ou crie uma conta.  
2. Clique na sua foto de perfil e vá para **Settings → Access Tokens**.  
3. Clique em **New token**, dê um nome e selecione o tipo **Read**.  
4. Copie o token gerado (algo como `hf_xxxxxxxxxxxxxxxxxxxxx`) e guarde com segurança.  

### 3️⃣ Criando o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` e adicione:

```env
OPENAI_API_KEY=sua_openai_api_key_aqui
HF_API_TOKEN=sua_huggingface_api_key_aqui

```

---

▶️ Executando a Aplicação

```bash
python app.py
```

A aplicação ficará disponível em:
```bash
python app.py
```

---

## 🧩 Fluxo de Funcionamento

- **O usuário envia um texto ou arquivo**  
- **A entrada é validada (validators.py)**  
- **O texto é extraído e limpo (text_cleaner.py)**  
- **O email é classificado via Hugging Face (huggingface_client.py)**  
- **Uma resposta automática é gerada via OpenAI (openai_client.py)**  
- **O resultado é exibido na interface web**  

---

## 📌 Tratamento de Erros

O sistema trata os seguintes cenários:
- **Nenhuma entrada fornecida**  
- **Arquivo sem nome**  
- **Formato de arquivo inválido**  
- **Texto vazio**    

---

## 👨‍💻 Autor

Arthur Trindade

Estudante de Sistemas de Informação, com foco em desenvolvimento backend, Python, Flask e aplicações com Inteligência Artificial.
Projeto desenvolvido com foco em boas práticas, organização e portfólio profissional.



