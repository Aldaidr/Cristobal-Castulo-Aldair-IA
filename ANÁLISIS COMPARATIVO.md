# Análisis comparativo de respuestas generadas por sistemas de Inteligencia Artificial sobre el tema:

# ¿Todos deberíamos votar en México?

---

# Introducción

El desarrollo de los Modelos de Lenguaje de Gran Escala (LLM, Large Language Models) ha permitido que las inteligencias artificiales sean capaces de responder preguntas complejas, argumentar posiciones, resumir información e incluso debatir temas sociales, políticos y filosóficos.

Sin embargo, no todas las inteligencias artificiales funcionan exactamente igual. Algunas generan respuestas utilizando únicamente el conocimiento aprendido durante su entrenamiento, mientras que otras complementan sus respuestas mediante sistemas de recuperación de información (RAG, Retrieval Augmented Generation), utilizando documentos proporcionados por el usuario.

El presente trabajo tiene como finalidad comparar el comportamiento de tres sistemas distintos de inteligencia artificial al responder preguntas relacionadas con el sufragio universal en México.

Las tecnologías evaluadas fueron:

- ChatGPT
- Google Gemini
- AnythingLLM utilizando Llama 3.2 y un corpus propio.

Para realizar el experimento se construyó un corpus con comentarios positivos y negativos sobre el tema "¿Todos deberíamos votar en México?". Dicho corpus fue cargado dentro de AnythingLLM con el objetivo de observar cómo un sistema RAG modifica sus respuestas dependiendo de la información disponible.

Posteriormente se realizaron distintas preguntas relacionadas con el voto universal, la democracia, la representación política, el crimen organizado y los límites de la voluntad de la mayoría.

Finalmente se compararon las respuestas obtenidas, identificando diferencias en la profundidad argumentativa, objetividad, razonamiento y dependencia del contexto.

---
## Construcción del corpus

Como primera etapa del experimento se diseñó un corpus compuesto por documentos de texto con dos posturas distintas.

### Corpus positivo

El primer archivo contiene opiniones que apoyan el sufragio universal.

Entre las ideas principales se encuentran:

- Todos los ciudadanos deberían votar.
- El voto fortalece la democracia.
- La participación ciudadana mejora la representación política.
- El voto es un derecho fundamental.

Este documento fue almacenado dentro de AnythingLLM para observar cómo influye en las respuestas del modelo.
---

### Corpus negativo

Posteriormente se construyó un segundo corpus con opiniones críticas hacia el sufragio universal.

Algunos argumentos fueron:

- No todas las personas se informan antes de votar.
- El voto debería ejercerse con responsabilidad.
- La desinformación afecta la calidad de las decisiones.
- La educación cívica debería fortalecerse.

Este segundo documento permitió observar cómo el sistema RAG recupera información dependiendo de la postura contenida en la base documental.
---

## Comparación de las inteligencias artificiales

### ChatGPT

Las respuestas generadas por ChatGPT se caracterizaron por desarrollar argumentos completos, analizando el problema desde distintas perspectivas.

En lugar de responder únicamente "sí" o "no", el modelo explicó conceptos como:

- democracia
- representación política
- legitimidad
- participación ciudadana
- instituciones
- derechos fundamentales

Además, cuando se presentó un argumento generado por Gemini, ChatGPT realizó una refutación punto por punto, identificando fortalezas y limitaciones del razonamiento.

Un ejemplo importante fue el debate sobre si el sistema electoral mexicano representa confianza ciudadana o únicamente un pacto de no agresión.

ChatGPT argumentó que ambas situaciones pueden coexistir.

Es posible desconfiar de los políticos y al mismo tiempo confiar en el procedimiento electoral.

Esta respuesta muestra un razonamiento más cercano al análisis académico que a una simple generación de texto.

---

### Google Gemini

Gemini presentó respuestas con un enfoque principalmente institucional e histórico.

Por ejemplo, al analizar el sistema electoral mexicano explicó:

- el origen del IFE
- la creación del INE
- los fraudes electorales del pasado
- la fiscalización
- la cadena de custodia
- las medidas de seguridad implementadas durante las elecciones.

Una de las afirmaciones más interesantes fue que el sistema electoral mexicano funciona como un "pacto de no agresión administrado por una burocracia gigante".

El argumento sostiene que la ciudadanía no necesariamente confía en los actores políticos, sino en los mecanismos institucionales que impiden el fraude.

Aunque esta postura resulta sólida desde un punto de vista histórico, puede debatirse porque reduce la confianza democrática únicamente al funcionamiento de las instituciones.

Durante el análisis, ChatGPT respondió que la existencia de mecanismos de control no implica ausencia de confianza, sino que constituye una característica normal de cualquier democracia moderna.

---

### AnythingLLM utilizando Llama 3.2

A diferencia de ChatGPT y Gemini, AnythingLLM no responde utilizando únicamente el conocimiento aprendido durante el entrenamiento del modelo.

Su funcionamiento depende del sistema RAG.

Esto significa que antes de generar una respuesta busca información dentro del corpus proporcionado por el usuario.

Durante las pruebas se observó que el sistema respondió utilizando ideas casi idénticas a las almacenadas en los documentos positivos y negativos.

Por ejemplo, al preguntar:

"¿Todos deberíamos poder votar?"

El sistema respondió utilizando exactamente los argumentos presentes dentro del corpus positivo.

Posteriormente se realizaron preguntas más complejas relacionadas con:

- la dictadura de la mayoría
- el crimen organizado
- la educación política
- la responsabilidad ciudadana

En todos los casos se observó que las respuestas dependían directamente de la información disponible dentro del corpus.

Esto demuestra el funcionamiento típico de un sistema Retrieval Augmented Generation (RAG), donde el modelo no "inventa" información sino que recupera documentos relevantes antes de generar la respuesta.
---

## Debate entre ChatGPT y Gemini

Uno de los aspectos más interesantes del experimento fue comparar la capacidad de razonamiento entre ambos modelos.

Gemini sostuvo que el sistema electoral mexicano funciona principalmente porque existe una gran burocracia diseñada para impedir el fraude.

Según su postura, la ciudadanía no confía en los políticos, sino únicamente en las reglas que limitan su comportamiento.

ChatGPT respondió que dicha afirmación representa solamente una parte del fenómeno.

Se argumentó que:

- los mecanismos institucionales no sustituyen la confianza;
- la fortalecen;
- las democracias modernas utilizan controles precisamente para garantizar transparencia.

Asimismo, se explicó que millones de ciudadanos participan en las elecciones porque existe un nivel suficiente de confianza en el procedimiento electoral, aunque persista una fuerte desconfianza hacia los partidos políticos.

Desde una perspectiva académica puede concluirse que ambas posturas son parcialmente correctas.

Gemini ofrece una explicación histórica del origen del sistema.

ChatGPT amplía esa explicación incorporando teoría democrática y filosofía política.

---

## Comparación general

| Característica | ChatGPT | Gemini | AnythingLLM |
|----------------|----------|---------|-------------|
| Profundidad argumentativa | Muy alta | Alta | Media |
| Capacidad de debatir | Muy alta | Alta | Baja |
| Uso del contexto | Alto | Alto | Totalmente dependiente del corpus |
| Explicaciones históricas | Buenas | Muy buenas | Dependen del documento |
| Uso de conocimiento externo | Sí | Sí | No (RAG) |
| Flexibilidad para refutar | Muy alta | Media | Baja |

---

# Conclusión

El experimento permitió observar que modelos de inteligencia artificial distintos pueden generar respuestas significativamente diferentes aun cuando reciben exactamente la misma pregunta.

ChatGPT destacó por producir respuestas estructuradas, con argumentos complejos y capacidad para debatir ideas, identificar supuestos y construir refutaciones fundamentadas.

Gemini mostró un excelente desempeño al contextualizar históricamente los problemas políticos, especialmente aquellos relacionados con las instituciones democráticas mexicanas, aunque en algunos casos sus conclusiones resultaron más categóricas y menos abiertas al debate.

Por su parte, AnythingLLM demostró el funcionamiento práctico de un sistema RAG. Las respuestas obtenidas estuvieron directamente influenciadas por el corpus construido durante la práctica, comprobando que la calidad de un sistema basado en recuperación de información depende en gran medida de los documentos utilizados como fuente de conocimiento.

Finalmente, este ejercicio permitió comprender que una inteligencia artificial no solamente depende del modelo de lenguaje empleado, sino también del contexto, los documentos disponibles y la forma en que recupera la información antes de generar una respuesta. En consecuencia, la combinación de modelos de lenguaje con corpus especializados representa una herramienta poderosa para desarrollar asistentes inteligentes capaces de responder preguntas específicas con base en información previamente validada.