# **Red neuronal para predecir si un alumno pasará de año**

Diseñar una red neuronal que permita predecir la probabilidad de que un alumno pase el año.

---

## **Entrada de datos**

La red neuronal recibe tres variables de entrada:

| Entrada | Descripción |
|---------|-------------|
| Promedio (%) | Promedio general del alumno |
| Asistencia (%) | Porcentaje de asistencia |
| Tareas (%) | Porcentaje de tareas entregadas |

Representación de la entrada:

```text
Promedio (%)
Asistencia (%)
Tareas (%)
```

---

## **Salida de datos**

La red neuronal genera una única salida:

```text
Probabilidad de que pase el año (%)
```

El cálculo de la probabilidad es independiente del grado escolar.

---

## **Representación del modelo**

```text
          Promedio (%)
                 │
                 │
        Asistencia (%)
                 │
                 │
          Tareas (%)
                 │
                 ▼
         ┌─────────────────┐
         │  Red Neuronal    │
         └─────────────────┘
                 │
                 ▼
Probabilidad de que pase el año (%)
```

---

## **Funcionamiento**

1. Se ingresan los porcentajes de promedio, asistencia y tareas.
2. La red neuronal procesa la información.
3. Se calcula la probabilidad de que el alumno pase el año.
4. Se muestra el resultado como porcentaje.

---

## **Ejemplo**

### **Entrada**

```text
Promedio: 85 %
Asistencia: 92 %
Tareas: 90 %
```

### **Salida**

```text
Probabilidad de que pase el año: 96 %
```

---

## **Conclusión**

La red neuronal utiliza como entradas el promedio, la asistencia y el porcentaje de tareas para estimar la probabilidad de que un alumno pase el año. La predicción funciona para cualquier grado escolar.