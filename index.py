import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['GOOGLE_API_KEY'] = config['GOOGLE_API_KEY']

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0)

template = '''
Você é um analista financeiro.
Escreva um relatório financeiro detalhado para a empresa "{empresa}" para o período {periodo}.

O relatório deve ser escrito em {idioma} e incluir a seguinte análise:
{analise}

Certifique-se de fornecer insights e conclusões para esta seção.
Formate o relatório utilizando Markdown para a criacao de tabelas e esstilização quando possível.
'''

prompt_template = PromptTemplate.from_template(template=template)

empresas = ['Google', 'Apple', 'Intel', 'Nvidia', 'Meta']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
anos = [2021, 2022, 2023, 2024]
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão']
analises = [
    "Análise do Balanço Patrimonial",
    "Análise do Fluxo de Caixa",
    "Análise de Tendências",
    "Análise de Receita e Lucro",
    "Análise de Posição de Mercado"
]

st.title('Gerador de Relatório Financeiro:')

empresa = st.selectbox('Selecione a empresa:', empresas)
trimestre = st.selectbox('Selecione o trimestre:', trimestres)
ano = st.selectbox('Selecione o ano:', anos)
periodo = f"{trimestre} {ano}"
idioma = st.selectbox('Selecione o idioma:', idiomas)
analise = st.selectbox('Selecione a análise:', analises)

if st.button('Gerar Relatório - {analises}', analise):
    prompt = prompt_template.format(
        empresa=empresa,
        periodo=periodo,
        idioma=idioma,
        analise=analise
    )

    response = llm.invoke(prompt)

    st.subheader('Relatório Gerado:')
    st.write(response.content)
