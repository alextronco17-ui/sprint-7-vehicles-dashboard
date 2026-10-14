"""Panel interactivo de anuncios de venta de coches — Sprint 7."""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="Anuncios de coches", layout="wide")

# Ubicar el CSV junto a este script, independientemente de la carpeta de inicio.
data_path = Path(__file__).resolve().parent / "vehicles_us.csv"
car_data = pd.read_csv(data_path)

st.header("Explorador de anuncios de venta de coches")
st.write(
    "Explora la distribución del odómetro y su relación con el precio anunciado. "
    "Selecciona una o ambas casillas para mostrar los gráficos."
)
st.caption(f"Base original: {len(car_data):,} anuncios. Los datos no se modifican.")

build_histogram = st.checkbox("Mostrar histograma del odómetro")
build_scatter = st.checkbox("Mostrar dispersión: odómetro y precio")

if build_histogram:
    odometer_data = car_data["odometer"].dropna()
    st.subheader("Distribución del odómetro")
    st.write(f"Anuncios con odómetro disponible: {len(odometer_data):,}.")
    fig_hist = go.Figure(
        data=[go.Histogram(x=odometer_data, nbinsx=50)]
    )
    fig_hist.update_layout(
        title="Distribución de las lecturas del odómetro",
        xaxis_title="Odómetro (unidad original del dataset)",
        yaxis_title="Número de anuncios",
    )
    st.plotly_chart(fig_hist)

if build_scatter:
    scatter_data = car_data[["odometer", "price"]].dropna()
    st.subheader("Relación entre odómetro y precio anunciado")
    st.write(f"Anuncios con ambos valores disponibles: {len(scatter_data):,}.")
    fig_scatter = go.Figure(
        data=[go.Scattergl(
            x=scatter_data["odometer"],
            y=scatter_data["price"],
            mode="markers",
            marker={"size": 5, "opacity": 0.35},
        )]
    )
    fig_scatter.update_layout(
        title="Odómetro frente al precio anunciado",
        xaxis_title="Odómetro (unidad original del dataset)",
        yaxis_title="Precio anunciado (unidad original del dataset)",
    )
    st.plotly_chart(fig_scatter)
    st.caption("Una asociación visual no demuestra causalidad ni equivale a un modelo de valoración.")

st.caption(
    "Los valores ausentes se excluyen únicamente del gráfico que los necesita. "
    "Los valores extremos se conservan. Las unidades requieren confirmación en el diccionario de datos."
)
