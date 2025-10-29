# Projetos
Projetos TPT

Vehicles Proj - Análise de Veículos nos EUA

Este projeto realiza uma **análise exploratória de dados** sobre veículos nos Estados Unidos.  
Foi desenvolvido um **aplicativo web interativo** usando **Streamlit**, com gráficos interativos criados com **Plotly Express**.

Funcionalidades do aplicativo

- **Visualização de dados**: carregamento do dataset `vehicles_us.csv` em um DataFrame.
- **Histograma da quilometragem (`odometer`)**: mostra a distribuição da quilometragem dos veículos.
- **Gráfico de dispersão (`price x odometer`)**: permite analisar a relação entre preço e quilometragem, diferenciando por fabricante (`make`).
- **Interatividade**: o usuário pode criar os gráficos usando **botões** ou **caixas de seleção (checkboxes)**.
- **Rápida prototipagem**: gráficos gerados dinamicamente sem necessidade de recarregar o aplicativo manualmente.

Como rodar o app

1. Ative o ambiente virtual `vehicles_env`:

```powershell
.\vehicles_env\Scripts\Activate.ps1

## Link Projeto Render
https://projetos-2ucr.onrender.com