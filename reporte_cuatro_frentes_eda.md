# Operación Cuatro Frentes
## Misión 1 --- Semáforo Académico

-   **Pregunta de negocio:** Determinar el nivel de riesgo académico de
    cada alumno.
-   **Tipo propuesto:** Clasificar (multiclase). **Justificación:** La variable objetivo riesgo está formada por tres categorías (verde, amarillo y rojo), las cuales representan distintos niveles de riesgo académico y no valores numéricos continuos. El propósito del modelo es asignar a cada alumno a una de estas categorías con base en sus características académicas, por lo que corresponde a un problema de clasificación multiclase y no de predicción numérica.
-   **Y:** riesgo.
-   **X candidatas:** asistencia_pct, tareas_entregadas,
    promedio_parciales, horas_plataforma, reprobadas_previas, turno.
-   **Hallazgos EDA:**
    -   Menor asistencia y menor promedio se asocian con mayor riesgo.
    -   Más materias reprobadas se relacionan con riesgo rojo.
    -   Distribución: verde 40%, amarillo 35%, rojo 25%; el balance es
        aceptable.
    -   Evitar fuga de información: no usar la calificación final como
        X.
-   **Métricas:** Accuracy, Precision, Recall, F1-score.
-   **Modelo propuesto:** Random Forest.

## Misión 2 --- Alerta de Churn

-   **Pregunta de negocio:** Identificar qué alumnos abandonarán la
    materia.
-   **Tipo propuesto:** Clasificar (binaria). **Justificación:** La variable objetivo abandona únicamente puede tomar dos valores posibles (0 = permanece y 1 = abandona). El objetivo es determinar a cuál de estos dos grupos pertenece cada estudiante antes de que ocurra el abandono, por lo que se trata de un problema de clasificación binaria, ya que el resultado esperado es una categoría y no un valor continuo.
-   **Y:** abandona.
-   **X candidatas:** dias_sin_login, foros_participados,
    avance_contenido_pct, calif_actividad_1, beca, trabaja.
-   **Hallazgos EDA:**
    -   Distribución: 430 (86%) permanecen y 70 (14%) abandonan; existe
        desbalance.
    -   Valores NA en calif_actividad_1; imputar y crear indicador.
    -   Muchos días sin login y poco avance se asocian con abandono.
    -   Evitar fuga: no usar fecha de baja ni nota final.
-   **Métricas:** Recall, Precision, F1-score, AUC-ROC.
-   **Modelo propuesto:** Random Forest.

## Misión 3 --- Pronóstico de Puntaje

-   **Pregunta de negocio:** Estimar la calificación final del alumno.
-   **Tipo propuesto:** Predecir (regresión). **Justificación:** Justificación: La variable objetivo calificacion_final corresponde a un valor numérico continuo dentro de una escala de 0 a 100. El propósito del modelo es estimar el valor exacto o aproximado de la calificación que obtendrá el estudiante, por lo que el problema corresponde a una regresión, ya que la salida esperada es un número y no una categoría.
-   **Y:** calificacion_final.
-   **X candidatas:** promedio_tareas, examen_1, examen_2,
    asistencia_pct, horas_estudio_sem.
-   **Hallazgos EDA:**
    -   examen_1 y examen_2 muestran fuerte relación con Y.
    -   Hay outliers (\>100) que deben revisarse.
    -   horas_estudio_sem presenta cola derecha.
-   **Métricas:** MAE y RMSE.
-   **Modelo propuesto:** Regresión Lineal.

## Misión 4 --- Tiempo de Estudio

-   **Pregunta de negocio:** Estimar cuántas horas adicionales necesita
    un alumno.
-   **Tipo propuesto:** Predecir (regresión). **Justificación:La variable objetivo horas_adicionales representa una cantidad numérica continua que indica el tiempo estimado que un estudiante necesita para dominar un tema. Debido a que el objetivo consiste en estimar un número de horas y no clasificar al alumno en una categoría, el problema corresponde a una regresión, donde el modelo debe predecir un valor continuo.** 
-   **Y:** horas_adicionales.
-   **X candidatas:** pretest_score, tema_dificultad, videos_vistos,
    ejercicios_correctos_pct, dispositivo.
-   **Hallazgos EDA:**
    -   A mayor dificultad, mayor número de horas.
    -   Solo 3% supera 40 horas; revisar antes de eliminar.
    -   Revisar correlación entre pretest_score y
        ejercicios_correctos_pct.
-   **Métricas:** MAE y RMSE.
-   **Modelo propuesto:** Random Forest Regressor.

## Síntesis (máx. 8 líneas)

  Misión   Tipo
  -------- --------------------------
  M1       Clasificación multiclase
  M2       Clasificación binaria
  M3       Regresión
  M4       Regresión

Pista utilizada: si Y es una categoría → clasificación; si Y es un valor
numérico continuo → regresión.

**Frase final:** El tipo de problema se deduce de la pregunta y de Y
porque una variable objetivo categórica requiere clasificación y una
variable objetivo numérica requiere regresión.