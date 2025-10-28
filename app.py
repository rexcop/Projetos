import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Caminho do CSV (assumindo que está na raiz do projeto)
csv_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')

# Função para carregar dados com cache


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


# Carregar dados
car_data = load_data(csv_path)

# Cabeçalho do app
st.header("Análise de Veículos nos EUA")
st.write("Explore os dados de anúncios de carros com gráficos interativos.")

# --- Botão para histograma ---
hist_button = st.button("Criar Histograma de Quilometragem")
if hist_button:
    st.write("Criando um histograma para a coluna 'odometer'")
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribuição de Quilometragem"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Botão para scatter plot ---
scatter_button = st.button("Criar Gráfico de Preço x Quilometragem")
if scatter_button:
    st.write("Criando gráfico de dispersão entre preço e quilometragem")

    # Amostragem para evitar travar o navegador
    sample_data = car_data.sample(n=5000, random_state=42) if len(
        car_data) > 5000 else car_data

    fig2 = px.scatter(
        sample_data,
        x="odometer",
        y="price",
        color="condition",  # coluna existente no CSV
        title="Preço x Quilometragem"
    )
    st.plotly_chart(fig2, use_container_width=True)
