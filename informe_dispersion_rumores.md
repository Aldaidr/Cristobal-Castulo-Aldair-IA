<div align="center">

# **INSTITUTO TECNOLÓGICO DE MORELIA**

## **Ingeniería en Sistemas Computacionales**

---

# **Inteligencia Artificial Verano**

## **Dispersión de rumores**

---

### **Presenta:**
## **Cristóbal Cástulo Aldair**

### **Profesor:**
**JESÚS EDUARDO ALCARAZ CHÁVEZ**

### **Fecha:**
**21 de julio de 2026**

</div>

---

## Misión 0 

| Pregunta | Respuesta |
|---|---|
| ¿Qué es el origen del rumor? | Es la primera publicación conocida que afirma que el examen de IA fue filtrado en un PDF por WhatsApp. |
| ¿Qué es la dispersión? | Es la forma en que el rumor pasa desde la publicación original hacia otras cuentas. Incluye copias casi idénticas, comentarios. |
| ¿Por qué un coseno alto no basta para saber quién empezó? | Un coseno alto solo indica que dos textos utilizan palabras en proporciones parecidas. No muestra cuál apareció primero. |
| ¿Qué peligro hay si solo miras «quién tiene más seguidores»? | Una cuenta con muchos seguidores puede producir mayor alcance sin haber creado el rumor. Podría ser solamente.|

## Misión 1

### Datos por ventana

| Ventana (min) | Tweets | Usuarios únicos | Cuentas nuevas |
|---|---:|---:|---:|
| 0–10 | 0 | 0 | 0% |
| 10–20 | 2 | 2 | 0% |
| 20–30 | 1 | 1 | 0% |
| **30–40** | **6** | **6** | **67%** |
| 40–50 | 2 | 2 | 0% |
| 50–60 | 3 | 3 | 0% |

## tabla 1


| Pregunta | Respuesta |
|---|---|
| Ventana crítica | **30–40 minutos** |
| Tweets en esa ventana | **6** |
| `pct_cuentas_nuevas` | **0.67 = 67%** |
| Interpretación | La conversación alcanzó su mayor volumen entre los minutos 30 y 40, con 6 tweets de 6 usuarios. En esa ventana, el porcentaje de cuentas nuevas subió de 0% a 67%, aproximadamente 4 de los 6 usuarios. Es una pista de posible coordinación o automatización, pero no basta por sí sola para demostrar que sean bots. |

El máximo de la columna `tweets` es:

\[
\max(0,2,1,6,2,3)=6
\]

## Misión 2
Un resultado cercano a 1 indica vectores de términos muy parecidos. Se conservó el umbral solicitado de **0.90** para marcar pares casi clon.

### Entrega M2

| Tweet | Semilla más cercana | Coseno |
|---|---|---:|
| `tw_origen_luna` | Rumor del examen | 0.976 |
| `tw_bot_01` | Rumor del examen | 0.967 |
| `tw_bot_02` | Rumor del examen | 0.951 |
| `tw_bot_03` | Rumor del examen | 0.925 |
| `tw_bot_04` | Rumor del examen | 0.891 |
| `tw_bot_05` | Rumor del examen | 0.908 |
| `tw_amplifica_diego` | Rumor del examen | 0.814 |
| `tw_amplifica_vale` | Rumor del examen | 0.644 |
| `tw_comedor_sofia` | Rumor del comedor | 0.982 |
| `tw_comedor_eco` | Rumor del comedor | 0.906 |
| `tw_ruido_becas` | Ruido de becas | 0.993 |
| `tw_ruido_beca2` | Ruido de becas | 0.869 |
| `tw_desmiente_omar` | Desmentido | 0.982 |
| `tw_desmiente_rectoria` | Desmentido | 0.913 |

El umbral de 0.90 se usa para encontrar copias entre tweets, no para eliminar tweets de un tema. Por eso `tw_bot_04`, aunque obtiene 0.891, sigue teniendo como semilla más cercana el rumor del examen.

### Pares casi clon (≥ 0.90)

| Tweet 1 | Tweet 2 | Coseno |
|---|---|---:|
| `tw_origen_luna` | `tw_bot_01` | 0.948 |
| `tw_origen_luna` | `tw_bot_02` | 0.901 |
| `tw_bot_01` | `tw_bot_02` | 0.984 |
| `tw_bot_01` | `tw_bot_03` | 0.944 |
| `tw_bot_01` | `tw_bot_04` | 0.923 |
| `tw_bot_01` | `tw_bot_05` | 0.930 |
| `tw_bot_02` | `tw_bot_03` | 0.974 |
| `tw_bot_02` | `tw_bot_04` | 0.968 |
| `tw_bot_02` | `tw_bot_05` | 0.963 |
| `tw_bot_03` | `tw_bot_04` | 0.973 |
| `tw_bot_03` | `tw_bot_05` | 0.962 |
| `tw_bot_04` | `tw_bot_05` | 0.963 |
| `tw_amplifica_diego` | `tw_amplifica_vale` | 0.932 |

Los posibles bots forman un grupo de mensajes casi clonados. El par más parecido es `tw_bot_01`–`tw_bot_02`, con **0.984**. Diego y Vale también superan 0.90 entre sí, pero esto no los convierte automáticamente en bots; se deben revisar las características de sus cuentas.

### Tweets de otro tema

- **Comedor:** `tw_comedor_sofia` y `tw_comedor_eco`.
- **Becas:** `tw_ruido_becas` y `tw_ruido_beca2`.
- `tw_desmiente_omar` y `tw_desmiente_rectoria` se relacionan con el caso, pero son desmentidos y no publicaciones que impulsan el rumor.

## Misión 3

Para buscar el origen se conservaron las cuentas del rumor del examen detectadas en M2 y se compararon sus minutos. `@luna_mx` publicó en el minuto 12, antes que Diego (28), los posibles bots (31–37) y Vale (35). Además, su cuenta tiene 1200 días, mientras que las cuentas de copias tienen solo entre 1 y 4 días.

### Entrega M3

| Rol propuesto | Usuario | Minuto | Evidencia |
|---|---|---:|---|
| Origen del examen | `@luna_mx` | 12 | Es la publicación del examen con el menor minuto y pertenece a una cuenta antigua de 1200 días. |
| Amplificador humano | `@diego_campus` | 28 | Cita y comenta a Luna; su cuenta tiene 800 días y el texto se relaciona con el examen. |
| Amplificador humano | `@vale_ia` | 35 | Cita y comenta a Diego; su cuenta tiene 950 días y 1200 seguidores. |
| Red de copias | `@info_rapida_01`, `@alertas_edu_02`, `@noticias_ya_03`, `@flash_campus_04`, `@viral_edu_05` | 31–37 | Copian texto dentro de la ventana crítica y sus cuentas tienen entre 1 y 4 días. |
| Desmentido | `@omar_verifica` | 45 | Desmiente a Luna; después Rectoría refuerza ese desmentido en el minuto 52. |

### Cascada

En el CSV, `origen` es quien realiza la acción y `destino_influencia` es la cuenta sobre la que actúa. Las flechas siguientes muestran el flujo de influencia para que la cascada se lea desde la fuente hacia quien copia, comenta o responde:

```text
@luna_mx --copia_texto--> @info_rapida_01 --copia_texto--> @noticias_ya_03 --copia_texto--> @viral_edu_05
@luna_mx --copia_texto--> @alertas_edu_02 --copia_texto--> @flash_campus_04
@luna_mx --cita_comenta--> @diego_campus --cita_comenta--> @vale_ia
@luna_mx --desmiente--> @omar_verifica --refuerza_desmentido--> @rectoria_iti
@sofia_comedor --retweet--> @eco_comedor
```

La última cadena corresponde al rumor del comedor y se mantiene separada del rumor del examen.

### Pregunta

Tener más likes o seguidores mide popularidad o capacidad de alcance, pero no el orden de publicación. `@luna_mx` tiene 340 seguidores y publicó primero, en el minuto 12. En cambio, `@rectoria_iti` tiene 5000 seguidores, pero aparece en el minuto 52 para reforzar un desmentido. Los posibles bots también consiguieron entre 38 y 60 likes, aunque publicaron después de Luna. Por eso el origen se determina combinando tema, minuto y cascada, no solamente métricas de popularidad.

## Misión 4

Se utilizaron las siete variables solicitadas: `seguidores`, `cuenta_dias`, `tweets_por_hora`, `pct_retweet`, `hora_pico`, `sim_max_con_rumor` y `diversidad_lexica`.

Se aplicó `StandardScaler` porque las variables tienen escalas diferentes. Por ejemplo, `cuenta_dias` puede tener valores de miles, mientras que `pct_retweet` se encuentra entre 0 y 1. Sin escalado, las variables grandes dominarían el cálculo de distancia de k-NN.

### Evaluación de k con validación cruzada de 5 partes

| k | F1 macro promedio | Desviación estándar |
|---:|---:|---:|
| 3 | 1.000 | 0.000 |
| 5 | 1.000 | 0.000 |
| 7 | 1.000 | 0.000 |

Los tres valores empataron. Se eligió **k = 3** porque es el menor valor probado y conserva una clasificación local sin perder rendimiento en este dataset sintético.

### Entrega M4

| Cuenta | Predicción | ¿Cuadra con M2/M3? |
|---|---|---|
| `@info_rapida_01` | bot | Sí; su tweet pertenece al grupo casi clon y la cuenta tiene 3 días. |
| `@alertas_edu_02` | bot | Sí; copia a Luna y tiene 2 días. |
| `@noticias_ya_03` | bot | Sí; copia a `@info_rapida_01` y tiene 4 días. |
| `@flash_campus_04` | bot | Sí; copia a `@alertas_edu_02` y tiene 1 día. |
| `@viral_edu_05` | bot | Sí; copia a `@noticias_ya_03` y tiene 2 días. |
| `@luna_mx` | humano | Sí; es una cuenta antigua y candidata a origen. |
| `@diego_campus` | humano | Sí; amplifica mediante un comentario propio. |
| `@vale_ia` | humano | Sí; amplifica el comentario de Diego. |
| `@omar_verifica` | humano | Sí; publica el desmentido. |
| `@sofia_comedor` | humano | Sí; pertenece al otro rumor. |
| `@rectoria_iti` | humano | Sí; refuerza el desmentido oficial. |

### ¿Qué haría si existiera conflicto entre coseno y k-NN?

No tomaría una decisión usando un solo resultado. El coseno analiza el parecido del texto, mientras que k-NN clasifica la cuenta a partir de su comportamiento y sus características. Revisaría también el minuto, la antigüedad, la frecuencia de publicación, la diversidad léxica y los enlaces de la cascada. Una persona puede copiar un texto sin ser bot y un bot puede publicar textos distintos. Si la evidencia continuara en conflicto, mantendría la etiqueta como caso dudoso para revisión humana.

## Misión 5

Se entrenó `DecisionTreeClassifier(max_depth=4, random_state=42)`. Las reglas generadas fueron:

```text
|--- ya_desmintio <= 0.50
|   |--- sim_con_rumor <= 0.50
|   |   |--- clase: ignora
|   |--- sim_con_rumor > 0.50
|   |   |--- es_bot_knn <= 0.50
|   |   |   |--- seguidores_alto <= 0.50
|   |   |   |   |--- clase: amplifica_leve
|   |   |   |--- seguidores_alto > 0.50
|   |   |   |   |--- clase: amplifica_influencer
|   |   |--- es_bot_knn > 0.50
|   |   |   |--- clase: amplifica_en_masa
|--- ya_desmintio > 0.50
|   |--- clase: contrarresta
```

### Entrega M5

| Escenario | Acción predicha |
|---|---|
| `red_bots` | `amplifica_en_masa` |
| `diego` | `amplifica_influencer` |
| `vale` | `amplifica_influencer` |
| `omar` | `contrarresta` |
| `sofia_comedor` | `ignora` |

### Acción prioritaria para el campus

La acción prioritaria sería **mutear o limitar la red de bots**. El árbol establece que, cuando una cuenta tiene similitud con el rumor, no ha desmentido y k-NN la clasifica como bot, la acción esperada es `amplifica_en_masa`. El escenario `red_bots` cumple exactamente esa regla. Diego y Vale también amplifican, pero el árbol los clasifica como influencers humanos y no como una red automatizada. Omar debe conservarse y apoyarse porque su acción es `contrarresta`. Sofía no requiere intervención para este caso porque su escenario se clasifica como `ignora` al tratar otro rumor.

## Misión 6 

Se ajustó el modelo:
El ajuste obtuvo \(R^2=0.991\), lo que indica que el modelo explica aproximadamente el 99.1% de la variación del alcance en estos datos sintéticos.

### Coeficientes

| Coeficiente | Valor aproximado | Significado |
|---|---:|---|
| \(\beta_0\) | 19.860 | Alcance base estimado cuando minutos, bots y desmentidos valen cero. |
| \(\beta_{minutos}\) | 1.823 | Cada minuto adicional aumenta el alcance estimado en aproximadamente 1.823 cuentas, manteniendo lo demás constante. |
| \(\beta_{bots}\) | 14.359 | Cada bot activo aumenta el alcance estimado en aproximadamente 14.359 cuentas. |
| \(\beta_{desmentidos}\) | -17.375 | Cada desmentido activo reduce el alcance estimado en aproximadamente 17.375 cuentas. |

### Escenarios

| Escenario | Minutos | Bots | Desmentidos | Alcance predicho |
|---|---:|---:|---:|---:|
| A | 60 | 10 | 0 | **272.85** |
| B | 60 | 10 | 2 | **238.10** |
| C | 60 | 0 | 2 | **94.51** |

### ¿Qué escenario conviene más al campus y por qué?

El escenario C conviene más porque presenta el menor alcance estimado: aproximadamente 94.51 cuentas. Comparado con A, mantener dos desmentidos y eliminar los diez bots reduce el alcance predicho en aproximadamente 178.34 cuentas. El coeficiente positivo de bots confirma que estos aumentan la dispersión, mientras que el coeficiente negativo de los desmentidos muestra que ayudan a reducirla. Por eso conviene limitar la red automatizada y mantener activos los mensajes de verificación.

## Misión 7 — Informe final de dispersión

El análisis de los datos sintéticos señala a `@luna_mx` como candidata a originar el rumor del examen.  
Su publicación apareció en el minuto 12, antes que las demás publicaciones del mismo tema.  
Además, su cuenta tenía 1200 días, por lo que no presentaba el patrón de una cuenta recién creada.  
El rumor comenzó a amplificarse con el comentario de `@diego_campus` en el minuto 28.  
Después, `@vale_ia` retomó el comentario de Diego en el minuto 35.  
La mayor explosión ocurrió entre los minutos 30 y 40, con 6 tweets y 67% de cuentas nuevas.  
En esa ventana participaron cinco cuentas que publicaron textos casi clonados.  
Sus similitudes coseno fueron superiores a 0.90 en varios pares.  
El par `tw_bot_01`–`tw_bot_02` alcanzó una similitud de 0.984.  
La cascada muestra que estas cuentas copiaron a Luna o se copiaron entre ellas.  
Con k-NN y `k=3`, las cinco cuentas de esa red fueron clasificadas como bots.  
Luna, Diego, Vale, Omar, Sofía y Rectoría fueron clasificados como humanos.  
Los resultados coinciden con el análisis del texto, la antigüedad y la cascada.  
El árbol predice que la red de bots `amplifica_en_masa`.  
También predice que Diego y Vale amplifican como influencers y Omar contrarresta el rumor.  
Por ello, la intervención prioritaria es limitar o mutear la red de bots.  
La regresión apoya la decisión: cada bot agrega 14.359 cuentas al alcance estimado.  
Cada desmentido reduce el alcance en aproximadamente 17.375 cuentas.  



