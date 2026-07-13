<div align="center">

# **INSTITUTO TECNOLÓGICO DE MORELIA**

## **Ingeniería en Sistemas Computacionales**

---

# **Inteligencia Artificial Verano**

## **Reporte Dino Crash**

---

### **Presenta:**
## **Cristóbal Cástulo Aldair**

### **Profesor:**
**JESÚS EDUARDO ALCARAZ CHÁVEZ**

### **Fecha:**
**13 de julio de 2026**

</div>

---
# ¿Qué dataset necesitamos?

### ¿Morirá en el siguiente frame?

- **Variable objetivo (Y):** `died_next_frame`
- **Tipo:** Binaria.
- **Valores posibles:**
  - `0`: el dinosaurio no morirá en el siguiente frame.
  - `1`: el dinosaurio morirá en el siguiente frame.

La columna `died` del frame no es suficiente para responder P1, porque únicamente indica si el dinosaurio ya murió en ese frame. Para predecir el siguiente frame se necesita desplazar esa información una posición y construir `died_next_frame`.

#### Variables de entrada (X)

| Variable | Tipo | Justificación |
|---|---|---|
| `speed` | Numérica | Una velocidad mayor reduce el tiempo disponible para reaccionar. |
| `obstacle_type` | Categórica | El riesgo cambia según sea cactus pequeño, cactus grande o pájaro. |
| `dist_obstacle` | Numérica | Una distancia pequeña aumenta el riesgo de colisión. |
| `jump` | Binaria | Permite saber si el dinosaurio ya está saltando. |
| `dino_height` | Numérica | Ayuda a saber si el dinosaurio se encuentra en el suelo o en el aire. |
| `crouch` | Binaria | Permite identificar si el dinosaurio está agachado frente a un pájaro. |
| `obstacle_height` | Numérica | Ayuda a determinar si el salto o la posición del dinosaurio son suficientes. |

#### Granularidad

Una fila debe representar **un frame de una partida**, porque la pregunta busca predecir lo que ocurrirá inmediatamente en el siguiente frame.

Registrar solamente cada salto o una fila por partida eliminaría información sobre la posición exacta del obstáculo y del dinosaurio antes de la muerte.

#### Tamaño mínimo razonable

Se pedirían como mínimo:

- **100 partidas completas**.
- Aproximadamente **24 000 frames**, tomando como referencia 12 000 frames en 50 partidas.

Esto permitiría tener cerca de 100 casos positivos de muerte, ya que normalmente existe una muerte por partida. Aun así, seguiría siendo una clase desbalanceada.

#### Riesgo si el dataset está mal definido

Si se utiliza `died` como variable objetivo sin desplazarla al siguiente frame, el modelo aprendería a detectar que el dinosaurio ya murió, pero no a predecir la muerte futura.

---

### ¿Cuántos puntos alcanzará esta partida al morir?

- **Variable objetivo (Y):** `final_score`
- **Tipo:** Numérica continua o entera.
- **Significado:** Puntuación total alcanzada al finalizar la partida.

#### Variables de entrada (X)

| Variable | Tipo | Justificación |
|---|---|---|
| `initial_speed` | Numérica | La velocidad inicial influye en la dificultad de la partida. |
| `player_reaction_time` | Numérica | Un menor tiempo de reacción puede permitir alcanzar puntuaciones mayores. |
| `jump_success_rate` | Numérica | Resume qué proporción de obstáculos fue superada correctamente. |
| `cactus_small_count` | Entera | Indica cuántos cactus pequeños aparecieron. |
| `cactus_large_count` | Entera | Indica cuántos cactus grandes aparecieron. |
| `bird_count` | Entera | Los pájaros pueden aumentar la dificultad. |
| `average_obstacle_distance` | Numérica | Obstáculos más cercanos entre sí pueden disminuir la puntuación final. |
| `player_experience` | Categórica | Permite diferenciar jugadores principiantes, intermedios y expertos. |

#### Granularidad

Una fila debe representar **una partida completa**.

No debe utilizarse una fila por frame porque el objetivo es un único valor final por sesión. Repetir `final_score` en todos los frames de una misma partida produciría redundancia y riesgo de fuga de información.

#### Tamaño mínimo razonable

Se solicitarían al menos:

- **200 partidas completas**.
- Partidas jugadas por diferentes personas.
- Partidas con puntuaciones bajas, medias y altas.

Esto permitiría observar variación suficiente en la puntuación final.

#### Riesgo si el dataset está mal definido

Si se incluye como entrada la puntuación obtenida cerca del final de la partida, el modelo podría predecir fácilmente el resultado porque ya tendría información casi equivalente al objetivo.

---

### ¿Qué tipo de obstáculo viene próximo?

- **Variable objetivo (Y):** `next_obstacle_type`
- **Tipo:** Categórica multiclase.
- **Clases posibles:**
  - `none`
  - `cactus_small`
  - `cactus_large`
  - `bird`

#### Variables de entrada (X)

| Variable | Tipo | Justificación |
|---|---|---|
| `current_obstacle_type` | Categórica | Puede existir un patrón entre el obstáculo actual y el siguiente. |
| `speed` | Numérica | La velocidad puede relacionarse con el nivel de dificultad y la aparición de obstáculos. |
| `score` | Numérica | La puntuación representa el avance de la partida. |
| `time_ms` | Entera | Permite identificar en qué momento de la sesión aparece el obstáculo. |
| `previous_obstacle_type` | Categórica | Permite estudiar secuencias de obstáculos. |
| `previous_obstacle_distance` | Numérica | Ayuda a estudiar el espacio entre obstáculos consecutivos. |
| `frame_since_last_obstacle` | Entera | Mide cuánto tiempo ha pasado desde el último obstáculo. |

#### Granularidad

Una fila debe representar **un evento de aparición de obstáculo** o el frame en el que se identifica un nuevo obstáculo.

Utilizar todos los frames produciría muchas filas con `none`, causando un desbalance innecesario.

#### Tamaño mínimo razonable

Se solicitarían:

- **100 partidas completas**.
- Al menos varios cientos de ejemplos de cada tipo de obstáculo.
- Partidas de distintas duraciones y velocidades.

#### Riesgo si el dataset está mal definido

Si la cámara o el juego ya muestra parcialmente el siguiente obstáculo dentro de las variables de entrada, el modelo recibiría información del futuro y produciría resultados artificialmente altos.

---

## 2. Diccionario y muestra

### Diccionario de datos propuesto

| Columna | Tipo sugerido | Descripción |
|---|---|---|
| `session_id` | Entero | Identificador único de la partida. |
| `frame` | Entero | Número del frame dentro de la partida. |
| `time_ms` | Entero | Tiempo transcurrido desde el inicio de la partida. |
| `score` | Entero | Puntuación visible en el frame. |
| `speed` | Numérico | Velocidad actual del escenario. |
| `obstacle_type` | Categórica | Tipo de obstáculo actual. |
| `dist_obstacle` | Numérico | Distancia al siguiente obstáculo en píxeles. |
| `jump` | Binaria | Indica si el dinosaurio está saltando. |
| `died` | Binaria | Indica si el dinosaurio murió en el frame actual. |
| `died_next_frame` | Binaria | Indica si morirá en el siguiente frame. |
| `dino_height` | Numérico | Altura del dinosaurio respecto al suelo. |
| `crouch` | Binaria | Indica si está agachado. |
| `obstacle_height` | Numérico | Altura del obstáculo detectado. |

### Patrón observado en la fila donde `died = 1`

En la fila del frame 82 se observa:

- `speed = 6.8`
- `obstacle_type = cactus_small`
- `dist_obstacle = 12`
- `jump = 0`
- `died = 1`

El patrón indica que el dinosaurio se encontraba muy cerca del cactus, no estaba saltando y murió. La combinación de distancia pequeña y ausencia de salto parece estar relacionada con la muerte.

### ¿Es `score` una buena variable para predecir muerte en el siguiente frame?

No parece ser una variable suficiente por sí sola.

La puntuación representa cuánto ha avanzado la partida, pero no describe directamente la posición del obstáculo ni la acción del dinosaurio. Dos frames pueden tener el mismo `score`, pero uno puede tener un obstáculo a 150 píxeles y otro a 12 píxeles.

Además, `score` puede estar fuertemente relacionada con `time_ms`, por lo que ambas variables pueden aportar información redundante.

### Columnas críticas faltantes para P1

Faltan variables como:

- Altura actual del dinosaurio.
- Estado de agachado.
- Altura del obstáculo.
- Velocidad vertical del salto.
- Tiempo de reacción del jugador.
- Distancia horizontal exacta entre el dinosaurio y el obstáculo.

Sin estas columnas, dos situaciones diferentes podrían parecer iguales en la tabla.

### ¿La columna `died` sirve para P1?

Tal como está definida, `died` solamente describe el final de la partida.

Para P1 debe crearse `died_next_frame`, tomando el valor de `died` del frame siguiente.

Ejemplo:

| Frame | `died` | `died_next_frame` |
|---:|---:|---:|
| 80 | 0 | 0 |
| 81 | 0 | 1 |
| 82 | 1 | No aplica |

El frame 81 es el que debe marcarse como positivo para predecir la muerte del siguiente frame.

---

# Preguntas que todo EDA debe responder

## 3. Checklist EDA

### ¿Cuántas observaciones hay?

El resumen indica:

- **50 partidas**.
- Aproximadamente **12 000 frames**.

Aunque 12 000 filas parece una cantidad grande, para P1 solamente existirían aproximadamente 50 ejemplos positivos de muerte, porque cada partida termina una sola vez.

Por lo tanto, el tamaño efectivo de la clase positiva es pequeño y no justificaría inicialmente una red neuronal profunda.

---

### ¿La clase objetivo está balanceada?

Para P1 existen:

- Total de frames: 12 000.
- Frames con muerte: 50.
- Frames sin muerte: 11 950.

Porcentaje de muertes:

\[
\frac{50}{12000}\times100 = 0.4167\%
\]

Porcentaje de no-muertes:

\[
\frac{11950}{12000}\times100 = 99.5833\%
\]

La clase está extremadamente desbalanceada.

Un modelo que siempre predijera `0`, es decir, que nunca habrá muerte, tendría aproximadamente 99.58% de accuracy, aunque sería inútil para detectar accidentes.

Por ello se deberían utilizar métricas como:

- Precision.
- Recall.
- F1-score.
- Matriz de confusión.

---

### ¿Cuál es la distribución de `speed`?

El resumen muestra:

- Media: 8.5.
- Mediana: 8.2.
- Mínimo: 6.0.
- Máximo: 13.0.

La velocidad aumenta con el tiempo de la partida, por lo que no mantiene una distribución constante.

Esto significa que los frames del inicio y del final tienen diferente nivel de dificultad. Un modelo global podría funcionar bien en velocidades bajas y fallar en velocidades altas.

---

## Independencia de las observaciones

Los frames de una misma partida no son independientes.

Por ejemplo, los frames 80, 81 y 82:

- Pertenecen a la misma sesión.
- Tienen velocidades casi iguales.
- Muestran el mismo obstáculo acercándose.
- Ocurren con pocos milisegundos de diferencia.

Si el frame 80 se coloca en entrenamiento y el frame 81 en prueba, el modelo prácticamente estaría siendo evaluado con una observación que ya vio.

La separación correcta debe hacerse por `session_id`:

- Partidas completas para entrenamiento.
- Partidas completas diferentes para prueba.

No se deben mezclar frames de una misma sesión entre ambos conjuntos.

---

## Ejemplo de fuga de información

### Fuga usando `score`

Para predecir la muerte en el siguiente frame, podría ocurrir que el valor de `score` dejara de aumentar exactamente en el frame previo a la muerte.

Si esa información solamente se conoce después de observar el siguiente frame, utilizarla permitiría al modelo conocer indirectamente el resultado futuro.

### Fuga usando `time_ms`

Si todas las partidas del dataset terminan cerca de un tiempo específico, el modelo podría aprender que al llegar a ese valor de `time_ms` ocurre la muerte.

Ejemplo:

| `time_ms` | `died_next_frame` |
|---:|---:|
| 4480 | 1 |
| 4496 | 1 |
| 4512 | 1 |

El modelo no aprendería a reconocer el obstáculo, sino a memorizar aproximadamente cuándo suelen terminar las partidas.

---

## 4. Interpretación de los resúmenes

### ¿P1 está desbalanceado?

Sí.

Solo existen 50 frames positivos entre aproximadamente 12 000 observaciones.

La proporción positiva es de aproximadamente 0.42%, mientras que la negativa es de 99.58%.

Esto hace que la accuracy sea una métrica engañosa.

---

### Métricas recomendadas

Para P1 se utilizarían principalmente:

- **Recall:** mide cuántas muertes reales fueron detectadas.
- **Precision:** mide cuántas predicciones de muerte fueron correctas.
- **F1-score:** combina precision y recall.
- **Matriz de confusión:** permite observar falsos positivos y falsos negativos.

La accuracy no debe utilizarse como única métrica.

---

### ¿`dist_obstacle` parece útil como predictor?

Sí.

El resumen indica que las muertes suelen ocurrir cuando:

\[
dist\_obstacle < 20
\]

Además, en la muestra:

- Frame 82.
- `dist_obstacle = 12`.
- `jump = 0`.
- `died = 1`.

También aparece otra muerte con:

- `dist_obstacle = 22`.
- `jump = 0`.
- `died = 1`.

Esto indica que una distancia pequeña combinada con la ausencia de salto puede ser un predictor importante.

No obstante, la distancia por sí sola no es suficiente, porque el riesgo también depende de la velocidad, el tipo de obstáculo y la posición del dinosaurio.

---

### Distribución de `score`

El `score` presenta:

- Media: 28.
- Mediana: 18.
- Mínimo: 0.
- Máximo: 120.
- Cola larga hacia la derecha.

La media es mayor que la mediana porque existen pocas partidas o frames con puntuaciones muy altas.

Para P2 esto sugiere que:

- Una regresión lineal simple podría verse afectada por valores altos.
- Podría considerarse una transformación como `log(1 + score)`.
- También podría utilizarse un árbol regresor, porque no exige una relación completamente lineal.

Para P1, `score` no debe considerarse automáticamente un buen predictor, porque puede actuar como sustituto de `time_ms`.

---

### Distribución de tipos de obstáculo

| Tipo | Porcentaje aproximado |
|---|---:|
| `none` | 54% |
| `cactus_small` | 20% |
| `cactus_large` | 15% |
| `bird` | 11% |

Para P3 las clases no están completamente balanceadas.

La clase `none` representa más de la mitad de los frames. Si el objetivo es predecir el próximo obstáculo, sería preferible trabajar con eventos de aparición de obstáculos en lugar de todos los frames.

---

# Del EDA a la elección del modelo

## 5. Elección de modelo

| Escenario | Fila de la guía aplicable | Modelo propuesto | Dos condiciones que debe cumplir el dataset |
|---|---|---|---|
| P1 | Y binaria muy desbalanceada | Regresión logística con `class_weight` o Random Forest con ponderación de clases | Separación por sesión y suficientes ejemplos positivos de muerte |
| P2 | Y numérica | Árbol regresor o regresión lineal después de revisar relaciones | Una fila por partida y puntuaciones finales suficientemente variadas |
| P3 | Y categórica multiclase | Árbol de decisión o regresión logística multinomial | Suficientes ejemplos de cada obstáculo y ausencia de información futura |

---

### Modelo para P1

Se propone comenzar con una **regresión logística con ponderación de clases**.

Razones:

- La variable objetivo es binaria.
- El dataset es tabular.
- Existe un desbalance extremo.
- Es un modelo interpretable.
- Permite observar qué variables aumentan o disminuyen el riesgo.

También podría probarse un Random Forest como comparación si existen relaciones no lineales entre distancia, velocidad, salto y tipo de obstáculo.

No se recomienda inicialmente una red neuronal profunda porque existen pocos ejemplos positivos.

---

### Modelo para P2

Se propone un **árbol regresor**.

Razones:

- La variable objetivo es numérica.
- Puede existir una relación no lineal entre velocidad, experiencia, obstáculos y puntuación final.
- La distribución de `score` presenta una cola larga.

También podría probarse una regresión lineal como modelo base, siempre que el EDA muestre relaciones aproximadamente lineales o se transforme la variable objetivo.

---

### Modelo para P3

Se propone un **árbol de decisión** o una **regresión logística multinomial**.

Razones:

- La variable objetivo tiene varias categorías.
- Existen variables numéricas y categóricas.
- Un árbol puede capturar reglas como combinaciones de velocidad, puntuación y obstáculo anterior.

No se recomienda usar regresión lineal asignando números como:

- `1 = cactus_small`
- `2 = cactus_large`
- `3 = bird`

Esos números crearían un orden y una distancia artificial entre las categorías.

---

## 6. Cuándo no usar un modelo

### Escenario donde un árbol profundo parecería buena idea, pero el EDA lo desaconsejaría

Un árbol profundo podría parecer adecuado porque puede aprender combinaciones como:

- Distancia pequeña.
- Velocidad alta.
- Dinosaurio sin saltar.
- Obstáculo grande.

Sin embargo, el EDA muestra que solo existen alrededor de 50 muertes.

Un árbol profundo podría memorizar los casos positivos específicos de entrenamiento y producir overfitting. Tendría buen rendimiento aparente en entrenamiento, pero fallaría en partidas nuevas.

En este caso sería preferible:

- Recolectar más partidas.
- Limitar la profundidad.
- Utilizar validación por sesión.
- Comparar con un modelo más simple.

---

### Escenario donde una red neuronal tendría sentido

Una red neuronal tendría sentido si se utilizaran directamente secuencias de imágenes o secuencias largas de frames.

Para justificarla, el EDA tendría que mostrar:

- Miles de partidas completas.
- Gran cantidad de ejemplos de muerte.
- Secuencias temporales suficientemente largas.
- Variaciones en velocidad, resolución, jugadores y obstáculos.
- Dependencia temporal que no pueda resumirse adecuadamente con variables tabulares.
- Separación de entrenamiento y prueba por sesión.

En ese caso podrían considerarse modelos como LSTM o GRU para secuencias, siempre que hubiera suficientes sesiones.

---

### P1 mediante reglas fijas

Una regla posible sería:

```text
Si dist_obstacle < X y jump = 0, entonces muerte.