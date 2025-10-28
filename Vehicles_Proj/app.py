import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Ler CSV
csv_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')
car_data = pd.read_csv(csv_path)

# Cabeçalho
st.header("Análise de Veículos nos EUA")
st.write("Exploração dos dados de veículos com gráficos interativos usando Plotly e Streamlit.")

# Botão para histograma
if st.button("Gerar Histograma de Quilometragem"):
    fig = px.histogram(car_data, x="odometer", nbins=50,
                       title="Distribuição de Odometer")
    st.plotly_chart(fig)

# Botão para gráfico de dispersão
if st.button("Gerar Gráfico de Preço x Quilometragem"):
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      color="make", title="Preço x Quilometragem")
    st.plotly_chart(fig2)
