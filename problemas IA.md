<div align="center">

# **INSTITUTO TECNOLÓGICO DE MORELIA**

## **Ingeniería en Sistemas Computacionales**

---

# **Inteligencia Artificial Verano**

## **Problemas clásicos de búsqueda y optimización**

---

### **Presenta:**
## **Cristóbal Cástulo Aldair**

### **Profesor:**
**JESÚS EDUARDO ALCARAZ CHÁVEZ**

### **Fecha:**
**12 de julio de 2026**

</div>

---

# **Introducción**

En este reporte se resuelven tres problemas clásicos relacionados con la Inteligencia Artificial, la búsqueda de soluciones, la representación de estados y la optimización.

Los problemas son:

1. El problema de los maridos celosos.
2. El puente y la linterna.
3. Flavio Josefo y el círculo de la muerte.

Cada problema se representa mediante:

- Estado inicial.
- Estado objetivo.
- Restricciones.
- Operadores o movimientos permitidos.
- Secuencia de solución.
- Relación con la Inteligencia Artificial.

---

# **1. El problema de los maridos celosos**

Tres parejas deben cruzar un río utilizando un bote con capacidad máxima para dos personas.

Cada pareja está formada por un marido y su esposa.

Para representar a las personas se usaran las siguientes abreviaciones:

| Pareja | Marido | Esposa |
|---|---|---|
| Pareja 1 | M1 | E1 |
| Pareja 2 | M2 | E2 |
| Pareja 3 | M3 | E3 |

La restricción principal es:

> Ninguna mujer puede permanecer en presencia de otro marido, a menos que su propio marido también esté presente.

Esta restricción debe cumplirse en:

- La orilla izquierda.
- La orilla derecha.
- El bote.

El objetivo es encontrar una secuencia mínima de viajes para que las seis personas crucen el río sin violar la restricción.

---

## **1.2 Estado inicial**

Al comienzo, las tres parejas y el bote se encuentran en la orilla izquierda.

```text
Orilla izquierda: M1, E1, M2, E2, M3, E3
Orilla derecha: vacío
Bote: izquierda
```

---

## **1.3 Estado objetivo**

El objetivo se alcanza cuando todas las personas se encuentran en la orilla derecha.

```text
Orilla izquierda: vacío
Orilla derecha: M1, E1, M2, E2, M3, E3
Bote: derecha
```

---

## **1.4 Representación de un estado**

Un estado puede representarse mediante tres elementos:

```text
Estado = (Personas en la izquierda, Personas en la derecha, Posición del bote)
```

ejemplo:

```text
({M1, E1, M2, E2}, {M3, E3}, izquierda)
```

Este estado indica que:

- M1, E1, M2 y E2 están en la orilla izquierda.
- M3 y E3 están en la orilla derecha.
- El bote está en la orilla izquierda.

---

## **1.5 Restricciones del problema**

Para que un estado sea válido debe cumplir las siguientes condiciones:

1. El bote debe transportar una o dos personas.
2. El bote no puede cruzar vacío.
3. Una esposa puede estar con otros maridos únicamente si su propio marido está presente.
4. Dos o más esposas pueden permanecer juntas sin ningún marido.
5. Dos o más maridos pueden permanecer juntos sin ninguna esposa.
6. Un marido puede viajar con su propia esposa.
7. El bote debe cambiar de orilla después de cada viaje.
8. Ninguna persona puede cruzar sin utilizar el bote.

---

## **1.6 Operadores**

Los operadores son las acciones que permiten cambiar de un estado a otro.

Los principales operadores son:

```text
Cruzar una persona hacia la derecha.
Cruzar dos personas hacia la derecha.
Regresar una persona hacia la izquierda.
Regresar dos personas hacia la izquierda.
```

Después de cada movimiento se debe comprobar que ninguna esposa quede con otro marido sin la presencia de su propio esposo.

---

## **1.7 Solución mínima**

La solución puede realizarse en un total de **11 viajes**.

---

### **Estado inicial**

```text
Izquierda: M1, E1, M2, E2, M3, E3
Derecha: vacío
Bote: izquierda
```

---

### **Viaje 1: cruzan E1 y E2**

```text
E1, E2 →
```

Estado resultante:

```text
Izquierda: M1, M2, M3, E3
Derecha: E1, E2
Bote: derecha
```

El estado es válido porque E3 permanece con su marido M3 y E1 y E2 están solas en la otra orilla.

---

### **Viaje 2: regresa E1**

```text
← E1
```

Estado resultante:

```text
Izquierda: M1, E1, M2, M3, E3
Derecha: E2
Bote: izquierda
```

El estado continúa siendo válido.

---

### **Viaje 3: cruzan E1 y E3**

```text
E1, E3 →
```

Estado resultante:

```text
Izquierda: M1, M2, M3
Derecha: E1, E2, E3
Bote: derecha
```

Todos los maridos están en una orilla y todas las esposas se encuentran en la otra.

---

### **Viaje 4: regresa E1**

```text
← E1
```

Estado resultante:

```text
Izquierda: M1, E1, M2, M3
Derecha: E2, E3
Bote: izquierda
```

---

### **Viaje 5: cruzan M2 y M3**

```text
M2, M3 →
```

Estado resultante:

```text
Izquierda: M1, E1
Derecha: M2, E2, M3, E3
Bote: derecha
```

El estado es válido porque E2 está con M2 y E3 está con M3.

---

### **Viaje 6: regresan M2 y E2**

```text
← M2, E2
```

Estado resultante:

```text
Izquierda: M1, E1, M2, E2
Derecha: M3, E3
Bote: izquierda
```

En cada orilla se encuentran parejas completas.

---

### **Viaje 7: cruzan M1 y M2**

```text
M1, M2 →
```

Estado resultante:

```text
Izquierda: E1, E2
Derecha: M1, M2, M3, E3
Bote: derecha
```

E3 puede estar con los otros maridos porque su esposo M3 está presente.

---

### **Viaje 8: regresa E3**

```text
← E3
```

Estado resultante:

```text
Izquierda: E1, E2, E3
Derecha: M1, M2, M3
Bote: izquierda
```

---

### **Viaje 9: cruzan E1 y E2**

```text
E1, E2 →
```

Estado resultante:

```text
Izquierda: E3
Derecha: M1, E1, M2, E2, M3
Bote: derecha
```

E1 se encuentra con M1 y E2 se encuentra con M2.

---

### **Viaje 10: regresa M3**

```text
← M3
```

Estado resultante:

```text
Izquierda: M3, E3
Derecha: M1, E1, M2, E2
Bote: izquierda
```

---

### **Viaje 11: cruzan M3 y E3**

```text
M3, E3 →
```

Estado final:

```text
Izquierda: vacío
Derecha: M1, E1, M2, E2, M3, E3
Bote: derecha
```

Las tres parejas han cruzado correctamente.

---

## **1.8 Tabla de movimientos**

| Viaje | Personas | Dirección | Orilla izquierda después del viaje | Orilla derecha después del viaje |
|---:|---|:---:|---|---|
| 1 | E1 y E2 | → | M1, M2, M3, E3 | E1, E2 |
| 2 | E1 | ← | M1, E1, M2, M3, E3 | E2 |
| 3 | E1 y E3 | → | M1, M2, M3 | E1, E2, E3 |
| 4 | E1 | ← | M1, E1, M2, M3 | E2, E3 |
| 5 | M2 y M3 | → | M1, E1 | M2, E2, M3, E3 |
| 6 | M2 y E2 | ← | M1, E1, M2, E2 | M3, E3 |
| 7 | M1 y M2 | → | E1, E2 | M1, M2, M3, E3 |
| 8 | E3 | ← | E1, E2, E3 | M1, M2, M3 |
| 9 | E1 y E2 | → | E3 | M1, E1, M2, E2, M3 |
| 10 | M3 | ← | M3, E3 | M1, E1, M2, E2 |
| 11 | M3 y E3 | → | Vacío | M1, E1, M2, E2, M3, E3 |

---

## **1.9 Árbol simplificado de la solución**

```text
Estado inicial
│
└── E1, E2 →
    │
    └── E1 ←
        │
        └── E1, E3 →
            │
            └── E1 ←
                │
                └── M2, M3 →
                    │
                    └── M2, E2 ←
                        │
                        └── M1, M2 →
                            │
                            └── E3 ←
                                │
                                └── E1, E2 →
                                    │
                                    └── M3 ←
                                        │
                                        └── M3, E3 →
                                            │
                                            └── Estado objetivo
```

---

## **1.10 Relación con la Inteligencia Artificial**

El problema de los maridos celosos puede representarse como un espacio de estados.

Cada nodo representa una distribución válida de personas entre las dos orillas y cada conexión representa un viaje del bote.

Para resolverlo se puede utilizar la búsqueda en anchura o **Breadth-First Search**, debido a que todos los viajes pueden considerarse con el mismo costo.

La búsqueda en anchura permite encontrar una solución con el menor número de viajes.

Los elementos del problema son:

```text
Estado inicial: todas las personas en la orilla izquierda.
Estado objetivo: todas las personas en la orilla derecha.
Operadores: viajes de una o dos personas.
Restricciones: reglas relacionadas con las esposas y los maridos.
Costo: un punto por cada viaje.
```

---

# **2. El puente y la linterna**
Cuatro personas deben cruzar un puente durante la noche.

El puente presenta las siguientes condiciones:

- Solo pueden cruzar una o dos personas al mismo tiempo.
- Para cruzar deben llevar una linterna.
- La linterna debe regresar cuando todavía queden personas en el lado inicial.
- Cuando cruzan dos personas, avanzan a la velocidad de la persona más lenta.

Los tiempos individuales son:

| Persona | Tiempo necesario |
|---|---:|
| A | 1 minuto |
| B | 2 minutos |
| C | 5 minutos |
| D | 10 minutos |

El objetivo es que todas las personas crucen el puente en exactamente **17 minutos**.

---

## **2.2 Estado inicial**

```text
Lado izquierdo: A, B, C, D
Lado derecho: vacío
Linterna: lado izquierdo
Tiempo acumulado: 0 minutos
```

---

## **2.3 Estado objetivo**

```text
Lado izquierdo: vacío
Lado derecho: A, B, C, D
Linterna: lado derecho
Tiempo acumulado: 17 minutos
```

---

## **2.4 Representación de un estado**

Un estado puede representarse de la siguiente forma:

```text
Estado = (Personas en la izquierda, Personas en la derecha, Posición de la linterna, Tiempo acumulado)
```

Ejemplo:

```text
({A, C, D}, {B}, izquierda, 3 minutos)
```

Esto significa que:

- A, C y D están en el lado izquierdo.
- B está en el lado derecho.
- La linterna está en el lado izquierdo.
- Han transcurrido 3 minutos.

---

## **2.5 Restricciones**

1. El puente soporta como máximo a dos personas.
2. No se puede cruzar sin la linterna.
3. La linterna debe estar en el mismo lado que las personas que realizarán el siguiente movimiento.
4. Cuando cruzan dos personas, el costo del movimiento es el tiempo de la persona más lenta.
5. Una persona puede regresar sola con la linterna.
6. El objetivo consiste en minimizar el tiempo total.

---

## **2.6 Operadores**

Los operadores posibles son:

```text
Cruzar una persona con la linterna.
Cruzar dos personas con la linterna.
Regresar una persona con la linterna.
Regresar dos personas con la linterna.
```

El costo de cada operador depende de la persona más lenta que participa en el movimiento.

Por ejemplo:

```text
A y C cruzan = 5 minutos
B y D cruzan = 10 minutos
A regresa = 1 minuto
B regresa = 2 minutos
```

---

## **2.7 Estrategia de solución**

Para obtener el tiempo mínimo, A y B, que son las personas más rápidas, ayudan a transportar la linterna.

Las personas más lentas, C y D, cruzan juntas. Esto evita que D y C tengan que cruzar por separado acompañadas por A.

---

## **2.8 Secuencia de solución**

### **Movimiento 1: cruzan A y B**

```text
A, B →
```

El tiempo del movimiento es determinado por B.

```text
Costo del movimiento: 2 minutos
Tiempo acumulado: 2 minutos
```

Estado resultante:

```text
Izquierda: C, D
Derecha: A, B
Linterna: derecha
```

---

### **Movimiento 2: regresa A**

```text
← A
```

```text
Costo del movimiento: 1 minuto
Tiempo acumulado: 3 minutos
```

Estado resultante:

```text
Izquierda: A, C, D
Derecha: B
Linterna: izquierda
```

---

### **Movimiento 3: cruzan C y D**

```text
C, D →
```

El tiempo del movimiento es determinado por D.

```text
Costo del movimiento: 10 minutos
Tiempo acumulado: 13 minutos
```

Estado resultante:

```text
Izquierda: A
Derecha: B, C, D
Linterna: derecha
```

---

### **Movimiento 4: regresa B**

```text
← B
```

```text
Costo del movimiento: 2 minutos
Tiempo acumulado: 15 minutos
```

Estado resultante:

```text
Izquierda: A, B
Derecha: C, D
Linterna: izquierda
```

---

### **Movimiento 5: cruzan A y B**

```text
A, B →
```

```text
Costo del movimiento: 2 minutos
Tiempo acumulado: 17 minutos
```

Estado final:

```text
Izquierda: vacío
Derecha: A, B, C, D
Linterna: derecha
```

Todas las personas han cruzado el puente.

---

## **2.9 Tabla de movimientos**

| Movimiento | Acción | Costo del movimiento | Tiempo acumulado |
|---:|---|---:|---:|
| 1 | A y B cruzan | 2 minutos | 2 minutos |
| 2 | A regresa | 1 minuto | 3 minutos |
| 3 | C y D cruzan | 10 minutos | 13 minutos |
| 4 | B regresa | 2 minutos | 15 minutos |
| 5 | A y B cruzan | 2 minutos | 17 minutos |

---

## **2.10 Cálculo total**

```text
2 + 1 + 10 + 2 + 2 = 17 minutos
```

Por lo tanto:

```text
Tiempo total = 17 minutos
```

---

## **2.11 Comparación con una solución no óptima**

Una posible estrategia sería que A acompañara individualmente a cada persona.

```text
A y D cruzan = 10 minutos
A regresa = 1 minuto
A y C cruzan = 5 minutos
A regresa = 1 minuto
A y B cruzan = 2 minutos
```

El tiempo total sería:

```text
10 + 1 + 5 + 1 + 2 = 19 minutos
```

Esta estrategia tarda 19 minutos, por lo que no cumple con el objetivo de 17 minutos.

La diferencia se debe a que C y D cruzan por separado.

En la solución óptima, C y D cruzan juntos y el costo de ese movimiento sigue siendo de 10 minutos.

---

## **2.12 Árbol simplificado de la solución**

```text
Estado inicial
│
└── A, B →
    │
    └── A ←
        │
        └── C, D →
            │
            └── B ←
                │
                └── A, B →
                    │
                    └── Estado objetivo: 17 minutos
```

---

## **2.13 Relación con la Inteligencia Artificial**

Este problema puede representarse como una búsqueda con costos diferentes.

Cada nodo representa:

- Las personas que están en cada lado.
- La ubicación de la linterna.
- El tiempo acumulado.

Cada movimiento tiene un costo diferente.

Por esta razón, uno de los algoritmos apropiados es la **búsqueda de costo uniforme**, ya que este algoritmo selecciona primero el estado que tiene el menor costo acumulado.

También puede utilizarse el algoritmo A*, utilizando una función:

```text
f(n) = g(n) + h(n)
```

Donde:

- `g(n)` representa el tiempo acumulado.
- `h(n)` representa una estimación del tiempo mínimo necesario para terminar.
- `f(n)` representa el costo total estimado.

---

# **3. Flavio Josefo y el círculo de la muerte**
Flavio Josefo relata que, durante el sitio de Yodfat, se encontraba junto con otros 40 hombres.

En total eran 41 personas.

Al encontrarse rodeados, decidieron colocarse en círculo y eliminar periódicamente a una persona siguiendo un conteo.

Josefo calculó la posición en la que debía colocarse para ser el último sobreviviente.

Este planteamiento es conocido actualmente como el **problema de Josefo**.

---

## **3.2 Enunciado matemático**

Se tienen `n` personas colocadas en un círculo.

Las personas están numeradas de:

```text
1, 2, 3, ..., n
```

Se comienza a contar circularmente y se elimina cada `k`-ésima persona que continúa viva.

Después de una eliminación, el conteo continúa desde la siguiente persona viva.

El proceso se repite hasta que solamente queda una persona.

El objetivo es calcular:

```text
J(n, k)
```

Donde:

- `n` es el número total de personas.
- `k` es el intervalo de eliminación.
- `J(n, k)` es la posición inicial del sobreviviente.

---

## **3.3 Estado inicial**

Para el caso de Josefo:

```text
Número de personas: 41
Intervalo de eliminación: 3
Personas vivas: 1, 2, 3, ..., 41
```

---

## **3.4 Estado objetivo**

```text
Personas vivas: una sola persona
Objetivo: identificar su posición inicial
```

---

## **3.5 Representación del problema**

El círculo puede representarse como una lista circular.

Ejemplo con cinco personas:

```text
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

Cuando se elimina una persona, el conteo continúa desde la siguiente persona viva.

---

## **3.6 Solución mediante simulación**

Supóngase el siguiente caso:

```text
n = 5
k = 3
```

Las personas iniciales son:

```text
1, 2, 3, 4, 5
```

---

### **Primera eliminación**

Se comienza a contar:

```text
1, 2, 3
```

Se elimina a la persona 3.

```text
Personas restantes: 1, 2, 4, 5
```

El siguiente conteo comienza en la persona 4.

---

### **Segunda eliminación**

Se cuentan:

```text
4, 5, 1
```

Se elimina a la persona 1.

```text
Personas restantes: 2, 4, 5
```

El siguiente conteo comienza en la persona 2.

---

### **Tercera eliminación**

Se cuentan:

```text
2, 4, 5
```

Se elimina a la persona 5.

```text
Personas restantes: 2, 4
```

El siguiente conteo comienza en la persona 2.

---

### **Cuarta eliminación**

Se cuentan circularmente:

```text
2, 4, 2
```

Se elimina a la persona 2.

```text
Sobreviviente: 4
```

Por lo tanto:

```text
J(5, 3) = 4
```

---

## **3.7 Fórmula de recurrencia**

Para resolver el problema de manera eficiente se utiliza una fórmula recurrente.

Cuando las posiciones comienzan desde cero:

```text
J(1, k) = 0
```

Para más de una persona:

```text
J(n, k) = (J(n - 1, k) + k) mod n
```

La fórmula devuelve una posición utilizando índices desde cero.

Para convertir el resultado a posiciones numeradas desde uno se utiliza:

```text
Posición segura = J(n, k) + 1
```

---

## **3.8 Cálculo del ejemplo n = 5 y k = 3**

```text
J(1, 3) = 0
```

```text
J(2, 3) = (J(1, 3) + 3) mod 2
J(2, 3) = (0 + 3) mod 2
J(2, 3) = 1
```

```text
J(3, 3) = (J(2, 3) + 3) mod 3
J(3, 3) = (1 + 3) mod 3
J(3, 3) = 1
```

```text
J(4, 3) = (J(3, 3) + 3) mod 4
J(4, 3) = (1 + 3) mod 4
J(4, 3) = 0
```

```text
J(5, 3) = (J(4, 3) + 3) mod 5
J(5, 3) = (0 + 3) mod 5
J(5, 3) = 3
```

Como el resultado utiliza índices desde cero, se suma uno:

```text
3 + 1 = 4
```

Por lo tanto:

```text
J(5, 3) = 4
```

---

## **3.9 Solución para las 41 personas**

Para el problema de Flavio Josefo se utilizan los siguientes valores:

```text
n = 41
k = 3
```

Se aplica la fórmula:

```text
J(n, k) = (J(n - 1, k) + k) mod n
```

Tabla de resultados:

| Número de personas | Posición con índice desde 0 | Posición desde 1 |
|---:|---:|---:|
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 1 | 2 |
| 4 | 0 | 1 |
| 5 | 3 | 4 |
| 6 | 0 | 1 |
| 7 | 3 | 4 |
| 8 | 6 | 7 |
| 9 | 0 | 1 |
| 10 | 3 | 4 |
| 11 | 6 | 7 |
| 12 | 9 | 10 |
| 13 | 12 | 13 |
| 14 | 1 | 2 |
| 15 | 4 | 5 |
| 16 | 7 | 8 |
| 17 | 10 | 11 |
| 18 | 13 | 14 |
| 19 | 16 | 17 |
| 20 | 19 | 20 |
| 21 | 1 | 2 |
| 22 | 4 | 5 |
| 23 | 7 | 8 |
| 24 | 10 | 11 |
| 25 | 13 | 14 |
| 26 | 16 | 17 |
| 27 | 19 | 20 |
| 28 | 22 | 23 |
| 29 | 25 | 26 |
| 30 | 28 | 29 |
| 31 | 0 | 1 |
| 32 | 3 | 4 |
| 33 | 6 | 7 |
| 34 | 9 | 10 |
| 35 | 12 | 13 |
| 36 | 15 | 16 |
| 37 | 18 | 19 |
| 38 | 21 | 22 |
| 39 | 24 | 25 |
| 40 | 27 | 28 |
| 41 | 30 | 31 |

El resultado con numeración desde cero es:

```text
J(41, 3) = 30
```

Para convertirlo a numeración desde uno:

```text
30 + 1 = 31
```

Por lo tanto, la posición segura es:

```text
Posición segura = 31
```

Josefo debía colocarse inicialmente en la posición número **31**.

---

## **3.10 Pseudocódigo iterativo**

```text
FUNCIÓN Josefo(n, k)

    posicion ← 0

    PARA personas ← 2 HASTA n HACER

        posicion ← (posicion + k) MOD personas

    FIN PARA

    RETORNAR posicion + 1

FIN FUNCIÓN
```

---

## **3.11 Ejecución del pseudocódigo**

Para calcular:

```text
Josefo(41, 3)
```

Se comienza con:

```text
posicion = 0
```

Después se actualiza la posición para cada tamaño del círculo:

```text
posicion = (posicion + 3) mod personas
```

El ciclo se ejecuta desde:

```text
personas = 2
```

Hasta:

```text
personas = 41
```

El resultado final es:

```text
posicion = 30
```

Al sumar uno:

```text
30 + 1 = 31
```

---

## **3.12 Pseudocódigo mediante simulación**

Otra forma de resolver el problema consiste en simular las eliminaciones utilizando una lista.

```text
FUNCIÓN JosefoSimulacion(n, k)

    personas ← lista con números desde 1 hasta n
    indice ← 0

    MIENTRAS tamaño(personas) > 1 HACER

        indice ← (indice + k - 1) MOD tamaño(personas)

        eliminar personas[indice]

    FIN MIENTRAS

    RETORNAR personas[0]

FIN FUNCIÓN
```

Esta solución elimina físicamente a cada persona de la lista hasta que solamente queda una.

---

## **3.13 Complejidad del algoritmo**

### **Solución iterativa con recurrencia**

El algoritmo realiza un ciclo desde 2 hasta `n`.

Su complejidad temporal es:

```text
O(n)
```

Su complejidad espacial es:

```text
O(1)
```

Esto se debe a que solamente almacena una variable para la posición.

---

### **Solución mediante simulación**

La simulación utiliza una lista con todas las personas.

Dependiendo de la estructura de datos utilizada, eliminar elementos puede requerir recorrer o reorganizar la lista.

Su complejidad puede aproximarse a:

```text
O(n²)
```

Su complejidad espacial es:

```text
O(n)
```

La solución mediante recurrencia es más eficiente porque no necesita almacenar a todas las personas.

---

## **3.14 Relación con la Inteligencia Artificial**

El problema de Josefo se relaciona con la Inteligencia Artificial y el diseño de algoritmos porque requiere:

- Representar un problema mediante estados.
- Simular acciones repetitivas.
- Analizar patrones.
- Diseñar algoritmos.
- Comparar soluciones.
- Reducir el uso de memoria.
- Mejorar la eficiencia computacional.

En una simulación, cada estado representa a las personas que continúan vivas.

Por ejemplo:

```text
Estado inicial: {1, 2, 3, 4, 5}
```

Después de eliminar a la persona 3:

```text
Estado 1: {1, 2, 4, 5}
```

Después de eliminar a la persona 1:

```text
Estado 2: {2, 4, 5}
```

El estado objetivo es aquel en el que queda una sola persona.

---

# **4. Comparación de los tres problemas**

| Problema | Tipo de problema | Estado objetivo | Método recomendado |
|---|---|---|---|
| Maridos celosos | Búsqueda con restricciones | Todas las parejas en la orilla derecha | Búsqueda en anchura |
| Puente y linterna | Búsqueda con costos | Todos cruzan en 17 minutos | Búsqueda de costo uniforme o A* |
| Flavio Josefo | Recurrencia y simulación | Encontrar al último sobreviviente | Algoritmo iterativo |

---

# **5. Elementos de un problema de búsqueda**

Los ejercicios anteriores pueden analizarse mediante los principales elementos utilizados en Inteligencia Artificial.

---

## **5.1 Estado inicial**

Es la situación desde la cual comienza el problema.

| Problema | Estado inicial |
|---|---|
| Maridos celosos | Las tres parejas están en la orilla izquierda |
| Puente y linterna | Las cuatro personas y la linterna están en el lado izquierdo |
| Flavio Josefo | Las `n` personas continúan vivas dentro del círculo |

---

## **5.2 Estado objetivo**

Es la situación que se desea alcanzar.

| Problema | Estado objetivo |
|---|---|
| Maridos celosos | Las tres parejas están en la orilla derecha |
| Puente y linterna | Las cuatro personas cruzaron en 17 minutos |
| Flavio Josefo | Solamente queda una persona viva |

---

## **5.3 Operadores**

Los operadores son las acciones que permiten avanzar de un estado a otro.

| Problema | Operadores |
|---|---|
| Maridos celosos | Cruzar o regresar una o dos personas en el bote |
| Puente y linterna | Cruzar o regresar con la linterna |
| Flavio Josefo | Contar y eliminar a cada `k`-ésima persona |

---

## **5.4 Restricciones**

Las restricciones determinan qué estados y acciones son válidos.

| Problema | Restricciones |
|---|---|
| Maridos celosos | Ninguna esposa puede estar con otro marido sin que esté presente el suyo |
| Puente y linterna | Solo cruzan dos personas y siempre deben llevar la linterna |
| Flavio Josefo | Solamente se cuentan las personas que continúan vivas |

---

## **5.5 Función de costo**

La función de costo permite medir qué tan costosa es una solución.

### **Maridos celosos**

Cada viaje tiene un costo de uno.

```text
Costo total = número de viajes
```

La solución presentada tiene:

```text
Costo total = 11 viajes
```

### **Puente y linterna**

Cada movimiento tiene como costo el tiempo de la persona más lenta.

```text
Costo total = suma de los tiempos de todos los movimientos
```

La solución presentada tiene:

```text
Costo total = 17 minutos
```

### **Flavio Josefo**

El objetivo principal no es minimizar viajes o tiempo, sino calcular la posición segura.

Sin embargo, se puede comparar el costo computacional de los algoritmos.

```text
Recurrencia iterativa: O(n)
Simulación con lista: O(n²)
```

---

# **6. Algoritmos de Inteligencia Artificial aplicables**

## **6.1 Búsqueda en anchura**

La búsqueda en anchura explora primero los estados que están más cerca del estado inicial.

Es apropiada para el problema de los maridos celosos porque cada viaje tiene el mismo costo.

Su funcionamiento general es:

```text
1. Agregar el estado inicial a una cola.
2. Extraer el primer estado de la cola.
3. Comprobar si es el estado objetivo.
4. Generar todos los estados siguientes válidos.
5. Agregar los estados no visitados a la cola.
6. Repetir hasta encontrar el objetivo.
```

---

## **6.2 Búsqueda de costo uniforme**

La búsqueda de costo uniforme expande primero el estado con el menor costo acumulado.

Es apropiada para el problema del puente y la linterna porque cada movimiento puede tener un costo diferente.

Por ejemplo:

```text
A regresa = 1 minuto
B regresa = 2 minutos
C cruza = 5 minutos
D cruza = 10 minutos
```

---

## **6.3 Algoritmo A***

El algoritmo A* utiliza la función:

```text
f(n) = g(n) + h(n)
```

Donde:

- `g(n)` es el costo real desde el estado inicial.
- `h(n)` es una estimación del costo restante.
- `f(n)` es el costo total estimado.

A* puede aplicarse al problema del puente y la linterna si se utiliza una heurística que estime el tiempo mínimo necesario para que las personas restantes crucen.

---

## **6.4 Algoritmos iterativos**

El problema de Josefo no necesita explorar todos los estados cuando se utiliza la fórmula recurrente.

El algoritmo puede calcular directamente la posición segura mediante:

```text
posicion = (posicion + k) mod personas
```

Esto reduce el uso de memoria y mejora el tiempo de ejecución.

---

# **Conclusión**

Los tres problemas analizados permiten observar diferentes formas de representar y resolver problemas relacionados con la Inteligencia Artificial.

En el problema de los maridos celosos es necesario explorar diferentes estados y comprobar las restricciones después de cada viaje. La solución presentada permite que las seis personas crucen el río en un total de 11 viajes.

En el problema del puente y la linterna se debe encontrar una secuencia que reduzca el tiempo total. La mejor estrategia consiste en utilizar a las dos personas más rápidas para transportar la linterna y permitir que las dos personas más lentas crucen juntas. El tiempo total obtenido es de 17 minutos.

En el problema de Flavio Josefo se puede realizar una simulación completa de las eliminaciones, pero la fórmula recurrente permite obtener el resultado de forma más eficiente. Para 41 personas y un intervalo de eliminación de 3, la posición segura es la número 31.

Estos ejercicios muestran la importancia de definir correctamente los estados, operadores, restricciones, costos y objetivos antes de seleccionar un algoritmo.

También demuestran que no todos los problemas se resuelven de la misma manera. Algunos requieren búsqueda, otros optimización y otros pueden resolverse mediante fórmulas matemáticas y algoritmos iterativos.

---

# **Resultados finales**

| Número | Problema | Resultado |
|---:|---|---|
| 1 | Maridos celosos | Las tres parejas cruzan en 11 viajes |
| 2 | Puente y linterna | Las cuatro personas cruzan en 17 minutos |
| 3 | Flavio Josefo | Para `n = 41` y `k = 3`, la posición segura es 31 |

---