# Explorador de anuncios de venta de coches — Sprint 7

Aplicación web desarrollada con Python, Pandas, Plotly y Streamlit como proyecto
del sprint de herramientas de desarrollo de software de TripleTen.

## Aplicación desplegada

**Pendiente de despliegue.** Antes de enviar al revisor, reemplazar esta línea
por el enlace real de Render, por ejemplo `https://nombre-real.onrender.com/`.
Ese ejemplo no corresponde a una aplicación publicada.

## Funcionalidad

- Encabezado y descripción del panel.
- Casilla para mostrar un histograma del odómetro.
- Casilla para mostrar un gráfico de dispersión entre odómetro y precio.
- Ambos gráficos pueden visualizarse al mismo tiempo.
- Gráficos Plotly interactivos: zoom y consulta de valores al pasar el cursor.
- Conteos explícitos de anuncios disponibles para cada gráfico.

La base original no se modifica. Los ausentes se excluyen solamente de las
variables requeridas para cada gráfico; los valores extremos se conservan.
Las visualizaciones describen anuncios, no ventas concretadas ni efectos
causales. Los ejes mantienen las unidades originales sin convertirlas ni
atribuir unidades no documentadas.

## Archivos

| Archivo | Propósito |
|---|---|
| `app.py` | Aplicación Streamlit |
| `vehicles_us.csv` | Dataset utilizado |
| `requirements.txt` | Dependencias del servicio web |
| `requirements-dev.txt` | Herramientas locales adicionales para el notebook |
| `notebooks/EDA.ipynb` | Exploración y visualizaciones con explicaciones |
| `.gitignore` | Excluye entornos y archivos que no se publican |
| `.streamlit/config.toml` | Colores de la interfaz |
| `GUIA_PASO_A_PASO.md` | Explicación del código y guía de los pasos manuales |

## Ejecutar en Windows

Desde la raíz del proyecto y con Python 3.11 o 3.12:

```powershell
python -m venv vehicles_env
.\vehicles_env\Scripts\python.exe -m pip install -r requirements-dev.txt
.\vehicles_env\Scripts\python.exe -m streamlit run app.py
```

En VS Code, selecciona el intérprete `vehicles_env` y el mismo kernel en el
notebook. El código del notebook admite iniciarlo desde la raíz o desde
`notebooks/`. El dataset se incluye; no se descarga al arrancar la aplicación.

## Ejecutar en macOS/Linux

```bash
python3 -m venv vehicles_env
vehicles_env/bin/python -m pip install -r requirements-dev.txt
vehicles_env/bin/python -m streamlit run app.py
```

## Desplegar en Render

- Tipo de servicio: **Web Service**, conectado al repositorio público de GitHub.
- Runtime: Python. Root Directory: vacío si `app.py` está en la raíz.
- Build Command:

```bash
python -m pip install --upgrade pip && python -m pip install -r requirements.txt
```

- Start Command:

```bash
python -m streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true
```

Antes de entregar, comprobar la URL pública y ambas casillas, actualizar este
README con el enlace real y enviar los cambios a GitHub.

## Fuente de datos y documentación

Dataset de práctica propuesto por TripleTen:
[vehicles_us.csv](https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv).

- [Plotly: histogramas](https://plotly.com/python/histograms/)
- [Plotly: gráficos de dispersión](https://plotly.com/python/line-and-scatter/)
- [Streamlit: gráficos Plotly](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
- [Render: servicios web y puerto](https://render.com/docs/web-services)

El proyecto estará completado cuando se publique, se entregue y lo apruebe el
revisor. Tener el código preparado no equivale a haber desplegado el servicio.
