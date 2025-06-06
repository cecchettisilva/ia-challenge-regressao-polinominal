import streamlit as st
import json
import requests

# Titúlo da aplicação 
st.title("Modelo de predição de receita de vendas")

# Inputs o usuário
st.write("Quantos meses o profissional tem de experiência?")
tempo_de_experiencia = st.slider("Meses", min_value=1, max_value=200, value=60, step=1)

st.write("Qual o número de vendas que o profissional realizou?")
numero_de_vendas = st.slider("Número Vendas", min_value=1, max_value=100000, value=5, step=1)

st.write("Qual temporada o profissional realizou as vendas?")
fator_sazonal = st.slider("Fator Sazonal", min_value=1, max_value=10, value=1, step=1)

# Preparar dados para API
input_features = {'tempo_de_experiencia': tempo_de_experiencia,
                  'numero_de_vendas': numero_de_vendas,
                  'fator_sazonal': fator_sazonal}

# Criar um botão e capturar um evento deste botão para disparar a API
if st.button('Estimar receita em reais'):
    res = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_features))
    res_json = json.loads(res.text)
    receita_em_reais = round(res_json['receita_em_reais'], 2)
    st.subheader(f'O receita estimada é de R$ {receita_em_reais}')