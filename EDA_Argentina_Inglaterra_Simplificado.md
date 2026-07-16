# Predicción Argentina vs Inglaterra

## Objetivo

Analizar datos para predecir qué selección tiene mayor probabilidad de ganar un partido entre Argentina e Inglaterra.

---

## Problema

> ¿Qué selección tiene mayor probabilidad de ganar un partido entre Argentina e Inglaterra?

### Variable objetivo

`resultado_partido`

Variable categórica con dos posibles resultados:

- Argentina
- Inglaterra

---

## Variables de entrada

Se utilizarán únicamente cuatro variables:

| Variable | Tipo | Descripción |
|---|---|---|
| ranking_equipo | Numérica | Posición del equipo en el ranking FIFA. |
| victorias_ultimos_5 | Entera | Victorias obtenidas en los últimos cinco partidos. |
| goles_favor_promedio | Numérica | Promedio de goles anotados recientemente. |
| goles_contra_promedio | Numérica | Promedio de goles recibidos recientemente. |

---

## Ejemplo del dataset

| ranking_equipo | victorias_ultimos_5 | goles_favor_promedio | goles_contra_promedio | resultado_partido |
|---:|---:|---:|---:|---|
| 1 | 4 | 2.2 | 0.8 | Argentina |
| 4 | 3 | 1.8 | 1.0 | Inglaterra |
| 1 | 5 | 2.5 | 0.6 | Argentina |
| 4 | 2 | 1.4 | 1.3 | Inglaterra |

---

## Preguntas del EDA

1. ¿Existen valores faltantes?
2. ¿Las variables tienen valores atípicos?
3. ¿Cuál variable parece influir más en el resultado?
4. ¿Las clases están balanceadas entre Argentina e Inglaterra?

---

## Tipo de problema

Es un problema de **clasificación binaria**, ya que solo existen dos posibles resultados: Argentina o Inglaterra.

---

