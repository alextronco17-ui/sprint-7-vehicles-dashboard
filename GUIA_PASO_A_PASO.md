# Sprint 7 — Construir, entender y publicar tu aplicación

Trabajaremos como en una clase: primero el propósito, después el código y su
razonamiento, y finalmente los pasos que harás en tu equipo. Aquí tienes todo
el recorrido; podemos avanzar una etapa a la vez por el chat.

## 1. Qué estamos construyendo

Una aplicación web que lee anuncios de coches y permite mostrar dos gráficos:

- **Histograma:** cuenta anuncios por intervalos de odómetro; responde dónde
  se concentran las lecturas y cómo se distribuyen.
- **Dispersión:** cada punto representa un anuncio con odómetro y precio;
  permite explorar su relación y detectar observaciones poco frecuentes.

El objetivo principal del sprint es ingeniería de software: entorno, aplicación,
repositorio y despliegue. No necesitamos un modelo predictivo ni un análisis
tan amplio como el del Sprint 6.

| Herramienta | Qué hace en nuestro proyecto |
|---|---|
| Python | Ejecuta la lógica |
| Pandas | Lee el CSV y selecciona los datos |
| Plotly | Construye los gráficos interactivos |
| Streamlit | Convierte el script en una interfaz web |
| Git | Registra cambios en archivos |
| GitHub | Aloja el repositorio |
| Render | Ejecuta la aplicación y proporciona una URL pública |

El notebook es el laboratorio de exploración. `app.py` es el programa que verá
el usuario. El servidor de Render ejecuta `app.py`, no el notebook.

## 2. Decisiones de los datos

El CSV incluido tiene **51,525 anuncios y 13 columnas**. Las variables de los
gráficos son `odometer` y `price`; no cambiamos tipos que ya son numéricos.

- `odometer` tiene 7,892 ausentes; quedan **43,633 lecturas** para el histograma.
- `price` no tiene ausentes; la dispersión también usa **43,633 pares completos**.
- Hay cero duplicados exactos en el archivo descargado.
- No imputamos ceros: una lectura no registrada no significa odómetro cero.
- No eliminamos extremos ni alteramos el CSV; investigarlos excede el objetivo
  mínimo y su existencia se informa en la exploración.
- No interpretamos ausentes de `is_4wd` como cero sin confirmar su significado.
- Los anuncios no son ventas realizadas. El precio anunciado no demuestra
  cuánto pagó alguien ni cuánto vale causalmente una lectura adicional.
- No atribuimos kilómetros, millas o moneda sin un diccionario confirmado.

`dropna()` se aplica a una columna o a una selección de dos columnas, devuelve
otro objeto y no cambia `car_data`. Esto evita eliminar anuncios por ausentes
en variables que no usamos, como `paint_color`.

## 3. Cómo leer el código de app.py

En el anexo de este documento encontrarás **cada línea del archivo, su código
y su explicación**. Aquí está el razonamiento de los bloques:

### Importaciones

```python
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
```

`Path` maneja rutas de archivos. Las otras líneas cargan librerías y crean
alias cortos. Importar una librería no instala el paquete: la instalación se
realiza antes con pip.

### Lectura del dataset

```python
data_path = Path(__file__).resolve().parent / "vehicles_us.csv"
car_data = pd.read_csv(data_path)
```

`__file__` identifica este archivo Python. `resolve()` obtiene su ruta absoluta;
`parent` obtiene su carpeta. `/` une esa carpeta con el nombre del CSV. Así no
dependemos de desde qué carpeta se ejecutó el comando.

`read_csv()` lee el archivo y devuelve un DataFrame, que guardamos en `car_data`.
En un notebook usamos `Path.cwd()` porque normalmente no existe `__file__`.

### Interacción

```python
build_histogram = st.checkbox("Mostrar histograma del odómetro")
if build_histogram:
    odometer_data = car_data["odometer"].dropna()
```

La casilla devuelve `True` si está marcada y `False` si no. El `if` ejecuta
el bloque solamente con `True`. La sangría define qué líneas pertenecen al
bloque. Las casillas permiten mantener ambos gráficos visibles simultáneamente.

Streamlit vuelve a ejecutar el script cuando cambias una casilla. No necesitas
escribir un bucle para esperar clics. Con un botón, su valor es verdadero en
la ejecución provocada por el clic; por eso elegimos casillas para esta versión.

### Construcción y presentación

```python
fig_hist = go.Figure(data=[go.Histogram(x=odometer_data, nbinsx=50)])
st.plotly_chart(fig_hist)
```

`go.Histogram` define una traza: qué datos y qué representación tendrá el
gráfico. `go.Figure` reúne trazas y diseño. `nbinsx=50` indica un máximo deseado
de intervalos; Plotly puede ajustar el número y los límites a valores apropiados.
`update_layout()` añade títulos. `st.plotly_chart()` presenta la figura dentro
de la web; en el notebook usamos `fig.show()`.

En la dispersión, `x` es odómetro e `y` precio. `mode="markers"` dibuja puntos,
no líneas. `go.Scattergl` usa WebGL para manejar muchos puntos. `opacity=0.35`
ayuda a ver dónde se superponen. Si el navegador no muestra puntos, comprueba
WebGL/aceleración de hardware; `go.Scatter` es una alternativa más lenta.

## 4. Preparar tus cuentas y repositorio

### Paso manual A — Revisar herramientas

Usaremos Windows y VS Code como ruta principal. Si trabajas con otro sistema
o ya utilizas Conda, indícalo antes de cambiar de entorno: podemos adaptar esta
etapa sin mantener dos entornos diferentes.

En una terminal de VS Code ejecuta:

```powershell
python --version
git --version
```

Esperamos una versión de Python 3.11 o 3.12 y una versión de Git. Si Python no
se reconoce, prueba `py --version`; si muestra una versión válida, podrás usar
`py -m venv vehicles_env` en el paso siguiente. Si falta Git, instala Git o usa
GitHub Desktop para clonar y sincronizar. No compartas claves ni contraseñas.

### Paso manual B — Crear un repositorio

1. Entra en `https://github.com/` con tu cuenta.
2. Selecciona **New repository**.
3. Nombre sugerido: `sprint-7-vehicles-dashboard`.
4. Selecciona **Public**, porque el revisor debe poder abrirlo.
5. Marca **Add a README file** y elige `.gitignore` de **Python**.
6. Crea el repositorio. No es necesario seleccionar una licencia para esta tarea.

### Paso manual C — Clonar y abrir en VS Code

1. Copia la URL HTTPS del repositorio desde **Code → HTTPS**.
2. En VS Code abre la paleta con `Ctrl+Shift+P`.
3. Busca **Git: Clone**, pega la URL y elige una carpeta de tu equipo.
4. Abre el repositorio clonado cuando VS Code lo ofrezca.
5. Extrae el ZIP entregado. Copia **el contenido** de `sprint7_vehicles` dentro
   del repositorio clonado, reemplazando el README inicial y combinando/reemplazando
   `.gitignore`. Conserva la carpeta `.git` que creó la clonación.
6. Verifica que `app.py`, `vehicles_us.csv` y `requirements.txt` queden en la
   raíz del repositorio; evita una carpeta extra entre ellos y la raíz.

La carpeta final tendrá `app.py`, los dos requirements, README, `.gitignore`,
`.streamlit/config.toml`, el CSV, esta guía y `notebooks/EDA.ipynb`.

## 5. Crear el entorno y ejecutar

En VS Code abre **Terminal → New Terminal** dentro de la raíz del repositorio.
Ejecuta los comandos por separado, comprobando que cada uno termine:

```powershell
python -m venv vehicles_env
```

`python` invoca Python; `-m venv` ejecuta su módulo de entornos; `vehicles_env`
es el nombre de la carpeta creada. Ese entorno aísla las librerías del proyecto.

```powershell
.\vehicles_env\Scripts\python.exe -m pip install -r requirements-dev.txt
```

La ruta apunta al Python del entorno, `-m pip` usa su instalador y `-r` lee
una lista de paquetes. `requirements-dev.txt` incluye las tres dependencias
de `requirements.txt` y añade `nbformat` e `ipykernel` para el notebook local.
No necesitamos cambiar políticas de PowerShell ni activar el entorno para
estos comandos. Render instalará solo las tres dependencias de la aplicación.

En macOS/Linux la ruta equivalente es `vehicles_env/bin/python`; el comando
de creación suele ser `python3 -m venv vehicles_env`.

### Configurar VS Code

1. Instala o habilita las extensiones **Python** y **Jupyter** de Microsoft.
2. `Ctrl+Shift+P` → **Python: Select Interpreter**.
3. Elige el Python de `vehicles_env`. Si no aparece, usa **Enter interpreter
   path** y busca `vehicles_env\Scripts\python.exe`.
4. Abre `notebooks/EDA.ipynb`; en **Select Kernel**, elige ese mismo entorno.
5. Lee las celdas Markdown y ejecuta las celdas de código en orden. Puedes usar
   **Run All**. Guarda con `Ctrl+S` para conservar las salidas.

El selector de intérprete y el kernel del notebook son configuraciones distintas.
Aunque el editor reconozca los imports, un kernel diferente puede generar
`ModuleNotFoundError`.

### Ejecutar la aplicación

```powershell
.\vehicles_env\Scripts\python.exe -m streamlit run app.py
```

`-m streamlit` ejecuta Streamlit con el Python del entorno. `run app.py` indica
el script de la aplicación. No uses `python app.py` para arrancar esta web.
Abre la URL local que imprima la terminal, normalmente `http://localhost:8501`.

Prueba cuatro estados: ninguna casilla, solo histograma, solo dispersión y ambas.
La interfaz debe mostrar el encabezado siempre y las figuras según tu selección.
Comprueba los conteos y mueve el cursor sobre los gráficos. Para parar, pulsa
`Ctrl+C` en la terminal.

## 6. Registrar cambios y enviarlos a GitHub

Puedes hacerlo en el panel **Source Control** de VS Code: revisar diferencias,
seleccionar archivos, escribir un mensaje, **Commit** y luego **Push/Sync**.

Si prefieres practicar la terminal:

```powershell
git status
git add app.py vehicles_us.csv requirements.txt requirements-dev.txt README.md .gitignore .streamlit/config.toml notebooks/EDA.ipynb GUIA_PASO_A_PASO.md VERIFICACION.md
git commit -m "Crear panel Streamlit con histograma y dispersion"
git push
```

`status` muestra cambios. `add` los prepara para el commit; no los publica.
`commit` crea una versión local con un mensaje. `push` envía esa versión a
GitHub. Revisa que `vehicles_env` no aparezca entre los archivos preparados.

Si Git pide identidad, configura tu nombre y correo de GitHub (o su correo
privado proporcionado por GitHub). Si pide autenticación, sigue el inicio de
sesión oficial de GitHub en el navegador. Un fallo de autenticación no se
soluciona modificando `app.py`.

Abre el repositorio en GitHub y comprueba que los archivos estén visibles.
No intentes hacer push a una URL de ejemplo; utiliza tu repositorio clonado.

## 7. Desplegar manualmente en Render

1. Entra en `https://render.com/` y vincula tu cuenta de GitHub.
2. Selecciona **New → Web Service**. Streamlit ejecuta Python en un servidor;
   corresponde a un servicio web, no a un sitio estático.
3. Autoriza y selecciona `sprint-7-vehicles-dashboard`.
4. Elige runtime **Python** y la rama que contiene tus archivos, normalmente
   `main`. Deja **Root Directory** vacío si están en la raíz.
5. En **Build Command** pega:

```bash
python -m pip install --upgrade pip && python -m pip install -r requirements.txt
```

La primera parte actualiza pip. `&&` ejecuta la siguiente parte solo si la
primera tuvo éxito. La segunda instala las dependencias del servicio.

6. En **Start Command** pega:

```bash
python -m streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true
```

| Parte | Propósito |
|---|---|
| `python -m streamlit run app.py` | Arranca el programa |
| `--server.address=0.0.0.0` | Escucha en las interfaces del servidor |
| `--server.port=$PORT` | Usa el puerto que entrega Render |
| `--server.headless=true` | Funciona sin intentar abrir un navegador en el servidor |

`$PORT` se interpreta en el entorno de Render. Pega este comando en su campo
Start Command; para tu equipo utiliza el comando local del apartado anterior.

7. Elige la instancia **Free** para esta práctica si está disponible para tu
   cuenta. Revisa el resumen antes de crear el servicio.
8. Crea el servicio y observa los logs del build y del arranque.
9. Cuando esté listo, abre la URL `onrender.com` que Render te asigne.
10. Comprueba las cuatro combinaciones de casillas también en la URL pública.

En el plan gratuito, el servicio puede dormirse tras 15 minutos sin tráfico
y tardar alrededor de un minuto en despertar. Una primera carga lenta no
significa por sí sola que el código falle. Confirma el estado y revisa logs.

Si el entorno de Python en Render difiere del local, puedes especificar allí
`PYTHON_VERSION` con la **versión completa que hayas comprobado** mediante
`python --version`, respetando las versiones soportadas por Render. No necesitas
inventar un número de versión ni modificar la variable del puerto.

## 8. Completar el README y entregar

1. En el README reemplaza **Pendiente de despliegue** por el enlace real.
2. Guarda y registra el cambio:

```powershell
git add README.md
git commit -m "Agregar enlace de la aplicacion en Render"
git push
```

3. Si Render no redepliega automáticamente cuando modificas código, utiliza
   **Manual Deploy → Deploy latest commit** o la opción equivalente visible.
4. Abre el repositorio sin iniciar sesión para comprobar que sea público.
5. Comprueba el enlace del README, el CSV y `notebooks/EDA.ipynb`.
6. Entrega el enlace del **repositorio GitHub** en TripleTen. El README permitirá
   al revisor acceder a la aplicación. El estado formal será pendiente de revisión
   hasta que el revisor lo apruebe.

## 9. Errores frecuentes y qué revisar

| Síntoma | Revisión |
|---|---|
| `ModuleNotFoundError` | Estás utilizando otro Python/kernel o no instalaste los requirements |
| Falta `vehicles_us.csv` | Verifica nombre, extensión y ubicación junto a `app.py` |
| PowerShell bloquea Activate.ps1 | Usa directamente el Python del entorno como en esta guía |
| Render no encuentra puerto | Revisa `--server.address=0.0.0.0` y `--server.port=$PORT` |
| Notebook muestra error de `nbformat` | Instala requirements-dev y selecciona el kernel correcto |
| La figura no aparece | Marca la casilla y revisa la terminal/logs; para Scattergl comprueba WebGL |
| Solo el README aparece en GitHub | Falta seleccionar archivos, commit o push |
| El revisor no abre el repositorio | Comprueba la visibilidad Public y la URL entregada |

## 10. Cómo explicar el proyecto en una entrevista

«Construí un panel con Streamlit para explorar anuncios de coches. Utilicé
Pandas para cargar los datos y Plotly para crear un histograma y una dispersión
interactivos. Mantuve el dataset original y excluí ausentes solamente de cada
gráfico. Organicé el entorno y las dependencias, registré cambios en Git y
publiqué el servicio en Render.»

Utiliza la frase sobre publicación **solo cuando ya hayas desplegado**.
Antes de eso: «La aplicación funciona localmente y el despliegue está pendiente».

Preguntas para comprobar que lo entendiste:

1. ¿Por qué un ausente de odómetro no debe sustituirse automáticamente por cero?
2. ¿Qué devuelve una casilla y cómo decide Python si dibujar una figura?
3. ¿Qué diferencia hay entre `fig.show()` y `st.plotly_chart(fig)`?
4. ¿Por qué enviar el entorno virtual a GitHub no sustituye requirements.txt?
5. ¿Cuál es la diferencia entre commit, push y deploy?

## Documentación verificada

- https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart
- https://plotly.com/python/histograms/
- https://render.com/docs/web-services
- https://render.com/docs/free

Los menús pueden cambiar; estas instrucciones se revisaron el 14 de octubre
de 2026. Usa las opciones equivalentes cuando cambie el texto de un botón.

## Anexo — Explicación de cada línea de app.py

La numeración coincide con el archivo entregado. Las líneas vacías separan
bloques y no ejecutan acciones.

| Línea | Código | Explicación |
|---:|---|---|
| 1 | `"""Panel interactivo de anuncios de venta de coches — Sprint 7."""` | Docstring: documenta el propósito del script; no dibuja contenido en la página. |
| 3 | `from pathlib import Path` | Importa Path, una clase de la biblioteca estándar para construir rutas. |
| 5 | `import pandas as pd` | Importa Pandas con el alias pd para leer y manejar tablas. |
| 6 | `import plotly.graph_objects as go` | Importa los objetos de gráficos de Plotly como go. |
| 7 | `import streamlit as st` | Importa Streamlit como st: sus funciones crean la interfaz. |
| 10 | `st.set_page_config(page_title="Anuncios de coches", layout="wide")` | Configura el texto de la pestaña del navegador y una página ancha. |
| 12 | `# Ubicar el CSV junto a este script, independientemente de la carpeta de inicio.` | Comentario para explicar la decisión de ruta; Python no lo ejecuta. |
| 13 | `data_path = Path(__file__).resolve().parent / "vehicles_us.csv"` | Parte de la ruta de app.py, resuelve su ubicación, toma su carpeta y añade el nombre del CSV. |
| 14 | `car_data = pd.read_csv(data_path)` | Lee el CSV y guarda el DataFrame en car_data. |
| 16 | `st.header("Explorador de anuncios de venta de coches")` | Dibuja el encabezado principal; satisface un requisito del proyecto. |
| 17 | `st.write(` | Comienza una llamada a st.write que escribirá una descripción. |
| 18 | `"Explora la distribución del odómetro y su relación con el precio anunciado. "` | Primera parte del mensaje para el usuario. |
| 19 | `"Selecciona una o ambas casillas para mostrar los gráficos."` | Segunda parte del mensaje; Python concatena automáticamente estos literales contiguos. |
| 20 | `)` | Cierra la llamada a st.write. |
| 21 | `st.caption(f"Base original: {len(car_data):,} anuncios. Los datos no se modifican.")` | Dibuja una nota; la f-string inserta el número de filas y :, añade separadores de miles. |
| 23 | `build_histogram = st.checkbox("Mostrar histograma del odómetro")` | Crea una casilla y guarda su estado booleano para el histograma. |
| 24 | `build_scatter = st.checkbox("Mostrar dispersión: odómetro y precio")` | Crea otra casilla independiente para la dispersión. |
| 26 | `if build_histogram:` | Solo ejecuta las líneas con sangría de este bloque si la primera casilla devuelve True. |
| 27 | `odometer_data = car_data["odometer"].dropna()` | Selecciona la Series odometer y crea otra Series sin ausentes; no modifica el DataFrame original. |
| 28 | `st.subheader("Distribución del odómetro")` | Añade un subtítulo al bloque del histograma. |
| 29 | `st.write(f"Anuncios con odómetro disponible: {len(odometer_data):,}.")` | Muestra cuántos anuncios entran al gráfico. |
| 30 | `fig_hist = go.Figure(` | Comienza la creación de una figura Plotly. |
| 31 | `data=[go.Histogram(x=odometer_data, nbinsx=50)]` | La lista data contiene una traza de histograma; x recibe valores y nbinsx un máximo deseado de intervalos. |
| 32 | `)` | Cierra la construcción de go.Figure y la asigna a fig_hist. |
| 33 | `fig_hist.update_layout(` | Comienza una actualización del diseño de esa figura. |
| 34 | `title="Distribución de las lecturas del odómetro",` | Configura el título del histograma. |
| 35 | `xaxis_title="Odómetro (unidad original del dataset)",` | Etiqueta el eje horizontal sin inventar una unidad. |
| 36 | `yaxis_title="Número de anuncios",` | Etiqueta el eje vertical como conteo de anuncios. |
| 37 | `)` | Cierra update_layout. |
| 38 | `st.plotly_chart(fig_hist)` | Presenta la figura dentro de Streamlit. El ancho se adapta por defecto en la versión actual. |
| 40 | `if build_scatter:` | Inicia un segundo if independiente: ambas casillas pueden ser True simultáneamente. |
| 41 | `scatter_data = car_data[["odometer", "price"]].dropna()` | Selecciona dos columnas como DataFrame y conserva solo filas con ambas disponibles. |
| 42 | `st.subheader("Relación entre odómetro y precio anunciado")` | Dibuja el subtítulo de la dispersión. |
| 43 | `st.write(f"Anuncios con ambos valores disponibles: {len(scatter_data):,}.")` | Muestra la cantidad de pares que se dibujarán. |
| 44 | `fig_scatter = go.Figure(` | Comienza otra figura independiente del histograma. |
| 45 | `data=[go.Scattergl(` | Inicia una traza Scattergl: dispersión con WebGL para muchos puntos. |
| 46 | `x=scatter_data["odometer"],` | Asigna el odómetro al eje X. |
| 47 | `y=scatter_data["price"],` | Asigna el precio anunciado al eje Y. |
| 48 | `mode="markers",` | Dibuja puntos en lugar de líneas conectadas. |
| 49 | `marker={"size": 5, "opacity": 0.35},` | Define el tamaño y transparencia de los puntos mediante un diccionario. |
| 50 | `)]` | Cierra la traza y la lista de trazas. |
| 51 | `)` | Cierra la figura y la guarda en fig_scatter. |
| 52 | `fig_scatter.update_layout(` | Comienza la configuración de títulos para esta figura. |
| 53 | `title="Odómetro frente al precio anunciado",` | Configura el título de la dispersión. |
| 54 | `xaxis_title="Odómetro (unidad original del dataset)",` | Etiqueta el eje X. |
| 55 | `yaxis_title="Precio anunciado (unidad original del dataset)",` | Etiqueta el eje Y, conservando la unidad original. |
| 56 | `)` | Cierra update_layout. |
| 57 | `st.plotly_chart(fig_scatter)` | Muestra la dispersión en la página. |
| 58 | `st.caption("Una asociación visual no demuestra causalidad ni equivale a un modelo de valoración.")` | Explica una limitación para interpretar el gráfico. |
| 60 | `st.caption(` | Fuera de los if, inicia una nota que aparece con cualquier combinación de casillas. |
| 61 | `"Los valores ausentes se excluyen únicamente del gráfico que los necesita. "` | Explica el tratamiento local de ausentes. |
| 62 | `"Los valores extremos se conservan. Las unidades requieren confirmación en el diccionario de datos."` | Explica que se conservan extremos y que las unidades deben confirmarse. |
| 63 | `)` | Cierra la nota final. |
