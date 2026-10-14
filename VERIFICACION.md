# Verificación del proyecto preparado

Fecha: 14 de octubre de 2026.

## Comprobado

- Dataset descargado del enlace propuesto: 51,525 filas y 13 columnas.
- Variables `odometer` y `price` presentes y numéricas.
- 7,892 ausentes de odómetro, cero ausentes de precio y cero duplicados exactos.
- 43,633 observaciones para el histograma y la dispersión.
- Aplicación ejecutada con `streamlit.testing.v1.AppTest` sin excepciones.
- Las cuatro combinaciones de casillas generan 0, 1, 1 y 2 figuras,
  respectivamente; el encabezado está presente siempre.
- Se verificaron las trazas Plotly: `histogram` y `scattergl`, ambas con los
  43,633 datos correspondientes, sin muestreo ni eliminación de extremos.
- Las seis celdas de código del notebook se ejecutaron secuencialmente en una
  sesión IPython; se guardaron sus salidas y dos figuras Plotly interactivas.
- Se validó el esquema del notebook con nbformat.
- Pearson calculado sobre pares completos: aproximadamente −0.4203.
- La guía explica todas las líneas no vacías de `app.py`.

## Entorno de comprobación

Python 3.12; Pandas 2.2.3; Streamlit 1.66.0; Plotly 7.1.0; nbformat 5.11.1.
`requirements.txt` conserva las tres librerías sin versiones, como pide el
enunciado. El entorno local y Render pueden instalar versiones distintas;
esta lista informa el entorno efectivamente comprobado.

## Pendientes manuales

- Instalar/configurar el entorno en tu equipo y elegir el kernel de VS Code.
- Verificar los gráficos visualmente en tu navegador.
- Crear o utilizar tu repositorio público de GitHub y enviar los archivos.
- Vincular y configurar el servicio web de Render.
- Comprobar la URL pública, actualizar el README y entregar al revisor.

No se creó un repositorio ni se publicó un servicio en tus cuentas. El README
no contiene un enlace público real todavía. La revisión y aprobación formal
siguen pendientes.

## Alcance de la ejecución del notebook

El entorno disponible no permitió iniciar un kernel externo por restricciones
de sockets. Se ejecutaron las mismas celdas en una sesión IPython dentro del
proceso y se guardaron las salidas. Esto verifica código y cálculos, pero no
prueba la configuración de tu kernel local. Reejecuta y guarda desde VS Code
con `vehicles_env` antes de entregar.
