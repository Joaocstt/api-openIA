import json
import os
import re
from openai import OpenAI
from app.pdf_generator import gerar_pdf


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
)

with open("app/prompt.json", "r", encoding="utf-8") as f:
    prompt_template = json.load(f)

def extrair_dados(mensagem: str) -> dict:
    user_prompt = prompt_template["user"].replace("{mensagem}", mensagem)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompt_template["system"]},
            {"role": "user", "content": user_prompt}
        ],
        stream=False
    )
    dados_extraidos = response.choices[0].message.content

    json_match = re.search(r"\{.*\}", dados_extraidos, re.DOTALL)

    if not json_match:
        raise ValueError("Não foi possível encontrar dados JSON válidos na resposta.")

    json_limpo = json_match.group(0)
    dados = json.loads(json_limpo)

    gerar_pdf(dados)

    return dados
