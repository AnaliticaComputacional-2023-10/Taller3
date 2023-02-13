# Taller 3

### Tableros en Dash

##### Analítica Computacional para la Toma de Decisiones

---

|     Nombres      |      Apellidos       |     Login     |  Codigo   |
| :--------------: | :------------------: | :-----------: | :-------: |
|     Santiago     | Gonzalez Montealegre | s.gonzalez35  | 202012274 |
| Juliana Carolina |  Cardenas Barragan   | jc.cardenasb1 | 202011683 |

---

---

## Un primer tablero en Dash

---

### 1.

¿Cómo se crea el objeto `app` en _Dash_?

   <br>

**R/**

Importamos la librería _Dash_ y posteriormente creamos un nuevo objeto de tipo Dash que pertenece a dicha librería. Dentro de los parámetros necesarios se encuentra `name=__name__` que es el valor que hace fácil para Dash encontrar ciertos elementos estáticos necesarios [1](https://www.angela1c.com/projects/dash/plotly_intro/)

```py
import dash

app = dash.Dash(name=__name__)

# Agregar parametros como hojas de estilo
app = dash.Dash(name=__name__, external_stylesheets=['url'])
```

---

### 2.

Describa el conjunto de datos del Dataframe

<br>

**R/**

```py
df = pd.DataFrame(
  {
    "Fiebre": ["Moderada", "Leve", "Alta", "Moderada", "Leve", "Alta"],
    "Casos": [4, 1, 2, 2, 4, 5],
    "Diagnóstico": ["Positivo", "Positivo", "Positivo", "Negativo", "Negativo", "Negativo"]
  }
)
```

|  Fiebre  | Casos | Diagnóstico |
| :------: | :---: | :---------: |
| Moderada |   4   |  Positivo   |
|   Leve   |   1   |  Positivo   |
|   Alta   |   2   |  Positivo   |
| Moderada |   2   |  Negativo   |
|   Leve   |   4   |  Negativo   |
|   Alta   |   5   |  Negativo   |

Los datos corresponden a un registro con tres columnas, Fiebre, Casos y Diagnóstico. Estos datos muestran el número de casos Positivos o Negativos según los síntomas de fiebre presentados por los pacientes.

---

### 3.

Ejecute la aplicación e incluya un pantallazo del código en ejecución y la aplicación siendo ejecutada en el navegador

<br>

**R/**
![Imagen Ejecución](image/Taller3-Solucion/1_3.png)

---

### 4.

Considerando la aplicación describa qué hace el comando

```py
fig = px.bar(
  data_frame=df,
  x="Fiebre",
  y="Casos",
  color="Diagnóstico",
  barmode="group"
)
```

<br>

**R/**

Se crea en una variable un objeto que posteriormente será agregado a la aplicación. Este objeto es creado con la librería `plotly.express` y es un objeto para crear un gráfico de barras.

**Parámetros**

- `data_frame`: Recibe valores de tipo pandas DataFrame donde están registrados los datos que se van a graficar.
- `x`: El nombre de la columna del DataFrame recibido en `data_frame` cuyos valores serán usados para colocar marcas a lo largo del eje x del gráfico.
- `y`: El nombre de la columna del DataFrame recibido en `data_frame` cuyos valores serán usados para colocar marcas a lo largo del eje y del gráfico.
- `color`: El nombre de la columna del DataFrame recibido en `data_frame` cuyos valores serán usados para asignar colores a las marcas. Generalmente se usa para variables categóricas que distingan los datos.
- `barmode`: Un `str` que puede recibir los valores `'relative'`, `'overlay'`, `'group'`.
  - `'relative'`: las barras para las categorías son apiladas o _stacked_ una encima de la otra.  
    ![Relative](image/Taller3-Solucion/1_4_Relative.png)
  - `'overlay'`: las barras son dibujadas una encima de la otra, se solapan.
    ![Overlay](image/Taller3-Solucion/1_4_Overlay.png)
  - `'group'`: las barras son dibujadas al lado de la otra para distinguir las categorías.
    ![Group](image/Taller3-Solucion/1_4_Group.png)

---

### 5.

- Describa que hace el siguiente código

  ```py
  dcc.Graph(
     id='example-graph',
     figure=fig
  ),
  ```

   <br>

  **R/**

  Esto permite añadir a la aplicación la gráfica que creamos anteriormente.

  - `id`: este parámetro permite identificar de forma particular este elemento, en caso de que sea necesario añadirle estilo personalizado o ser referenciado por otro objeto del HTML.
  - `figure`: este parámetro permite agreagar la variable en la que se creó la figura o gráfico a mostrar.

  <br>

- Describa que hace el siguiente código

  ```py
  html.Div(
     className="Columnas",
     children=[
        html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
     ],
  )
  ```

  <br>

  **R/**

  Esto permite añadir una lista desordenada `Ul` la cual tiene como subcontenido los nombres de las columnas del DataFrame creados como elementos de la lista `Li`. Toda esta lista se encuentra dentro de un contenedor `Div` que permite agrupar los elementos html.

  - `children`: en este parámetro se ubican todos los subelementos del objeto siendo creado

  Un gráfico que representa este código se meustra a continuación

  ![Contenedor](image/Taller3-Solucion/1_5_Contenedor.png)

---

### 6.

Realice cambios en los datos para obtener una nueva versión del tablero con datos de su elección.

<br>

**R/**

Los nuevos datos a utilizar son:

```py
df = pd.DataFrame(
    {
        "Votos": [5, 9, 4, 9, 2, 3, 4, 9, 5],
        "Candidato": ["Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández", "Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández", "Federico Gutierrez", "Gustavo Petro", "Rodolfo Hernández"],
        "Departamento": ["Cundinamarca", "Cundinamarca", "Cundinamarca", "Meta", "Meta", "Meta", "Guaviare", "Guaviare", "Guaviare"],
    }
)
```

| Votos |     Candidato      | Departamento |
| :---: | :----------------: | :----------: |
|   5   | Federico Gutierrez | Cundinamarca |
|   8   |   Gustavo Petro    | Cundinamarca |
|   4   | Rodolfo Hernández  | Cundinamarca |
|   9   | Federico Gutierrez |     Meta     |
|   2   |   Gustavo Petro    |     Meta     |
|   3   | Rodolfo Hernández  |     Meta     |
|   4   | Federico Gutierrez |   Guaviare   |
|   9   |   Gustavo Petro    |   Guaviare   |
|   5   | Rodolfo Hernández  |   Guaviare   |

Y la aplicación con los nuevos datos es de la siguiente forma:

![Nuevo Dashboard](image/Taller3-Solucion/1_6_Nuevo.png)

---

---

## Callbacks

---

### 1.

Describa el layout de la aplicación del archivo `app2.py`

<br>

**R/**

El layout es un elemento Div contenedor que posee a cuatro subelementos

- _H6_: Este elemento permite colocar un encabezado de nivel 6 (Existen 6 niveles de encabezados, siendo 1 el más grande o importante)

- _Div_: Este es otro elemento contenedor con dos subelementos:

  - _Texto_: No ha una etiqueta particular, sino que solo se escribe el texto que se desea mostrar. En este caso `Input: `
  - _Input_: Un elemento que permite al usuario introducir un texto particular en la app. Es importante definir un id para que el valor introducido por el usuario pueda ser usado por otros elementos.
    ```py
    # https://dash.plotly.com/basic-callbacks
    dcc.Input(
      id='my-input', # el id para identificar por otros elementos el objeto
      value='valor inicial', # el valor inicial a mostrar en el input
      type='text' # el tipo de input, puede ser
      # "text", "number", "password", "email", "search", "tel", "url", "range", "hidden"
    )
    ```

- _Br_: Es un elemento HTML que permite insertar saltos de línea
- _Div_: El último elemento es otro div el cual no tiene subelementos ni texto inicial, sin embargo, se le asigna un id para poder ser modificado proximamente por otro elemento.

El layout se puede ver de la siguiente forma elemento por elemento:
![Layout](image/Taller3-Solucion/2_1_Layout.png)

Ya ejecutada la aplicación se observa:

![App](image/Taller3-Solucion/2_1_App.png)

---

### 2.

Describa qué hace la función `update_output_div`

```py
@app.callback(
    [Output(component_id='my-output', component_property='children')],
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return f'Output: {input_value}'
```

<br>

**R/**

Cada vez que una propiedad input cambie, la función que encierre el decorator `@app.callback` será llamada automáticamente, en este caso `update_output_div`. La función recibe como parámetro el nuevo valor de la propiedad input. Finalmente _Dash_ actualiza la propiedad del componente output con lo que haya retornado la función.
Apenas se ejecuta la aplicación se ejecuta la función como si hubiera un cambio en el input, por esta razón así el output esté vacío al configurar el layout cuando se ejecuta la aplicación se le asigna un valor al output.

---

### 3.

Describa qué hace el decorador `app.callback`

```py
@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
```

<br>

**R/**

con este decorador le estamos diciendo a _Dash_ que llame esta función cuando cambie el valor del input asociado por medio del `component_id='my-input'` (el Input en el Div para nuestra aplicación) y actualice el componente output asociado con el `component_id='my-output'` (el Div vacío en nuestra aplicación).

---

### 4.

Modifique la aplicación agregando texto personalizado.

<br>

**R/**

Se plantearon las siguientes modificaciones:

- Una página que permita registrar un usuario con un username y una password

- La aplicación inicial y el mensaje default:

  ![Mod 1](image/Taller3-Solucion/2_4_Mod1.png)

- El mensaje tras llenar solamente el username

  ![Mod 2](image/Taller3-Solucion/2_4_Mod2.png)

- El mensaje tras llenar ambos campos, username y password:

  ![Mod 3](image/Taller3-Solucion/2_4_Mod3.png)
