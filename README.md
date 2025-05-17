
# API para Extrair Dados e Gerar PDF

API simples em Flask que recebe um texto via JSON, extrai dados específicos usando OpenAI e retorna um PDF com essas informações.

---

## Funcionalidades

- Recebe texto bruto via JSON no corpo da requisição POST.
- Usa OpenAI para extrair dados (cliente, endereço, data/hora, telefones, produto).
- Gera um PDF com os dados extraídos.
- Retorna o PDF para download.

---

## Requisitos

- Python 3.8+
- Flask
- openai (ou cliente OpenAI compatível)
- fpdf
- requests (opcional, para testes)
- Variável de ambiente `OPENAI_API_KEY` configurada

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Joaocstt/api-openIA
cd seuprojeto
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Variáveis de ambiente

Configure (CMD) sua chave da API OpenAI:

```bash
export OPENAI_API_KEY="sua_chave_aqui"  # Linux/Mac
set OPENAI_API_KEY="sua_chave_aqui"     # Windows
```

---

## Uso

### Rodar a API localmente

```bash
python run.py
```

Por padrão, a API roda em `http://localhost:5000`

### Endpoint

`POST /sendMessage`

- **Headers**: `Content-Type: application/json`
- **Body**:

```json
{
  "mensagem": "texto copiado aqui"
}
```

### Resposta

Retorna o PDF com as informações extraídas.


---

## Estrutura do projeto

```
.
├── run.py              # arquivo para rodar o app Flask
├── app                 # pasta do app
│   ├── __init__.py     # inicialização da aplicação
│   ├── routes.py       # definição das rotas
│   ├── prompt.json     # arquivo JSON com o prompt da OpenAI
│   ├── pdf_generator.py # código para gerar o PDF
│   └── openai_client.py # código para chamada OpenAI
├── requirements.txt    # dependências do Python
└── README.md
```

---

## Como modularizar

- `routes.py`: define rotas e recebe a requisição JSON.
- `openai_client.py`: encapsula a chamada à API OpenAI.
- `pdf_generator.py`: gera o PDF com as informações extraídas.
- `prompt.json`: mantém o prompt para facilitar manutenção.

---

## Observações

- Lembre-se de configurar o cabeçalho `Content-Type` para `application/json` nas requisições.
- O PDF gerado é temporário e pode ser ajustado para salvar ou retornar em memória.
- Customize o prompt no `prompt.json` conforme a necessidade.

---

