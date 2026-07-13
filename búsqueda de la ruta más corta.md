<div align="center">

# **INSTITUTO TECNOLÓGICO DE MORELIA**

## **Ingeniería en Sistemas Computacionales**

---

# **Inteligencia Artificial Verano**

## **búsqueda de la ruta más corta**

---

### **Presenta:**
## **Cristóbal Cástulo Aldair**

### **Profesor:**
**JESÚS EDUARDO ALCARAZ CHÁVEZ**

### **Fecha:**
**12 de julio de 2026**

</div>

---

# **1. Enunciado del problema**

Se tiene un tablero de **6 filas por 8 columnas**, formado por 48 casillas numeradas de izquierda a derecha y de arriba hacia abajo.

El agente inicia en la casilla:

```text
41
```

Y debe llegar a la casilla objetivo:

```text
48
```

Las casillas que contienen obstáculos son:

```text
11, 19, 20, 28, 29, 37, 38 y 46
```

Los costos de movimiento son:

| Movimiento | Costo |
|---|---:|
| Arriba | 10 |
| Abajo | 10 |
| Izquierda | 10 |
| Derecha | 10 |
| Diagonal | 14 |

---

# **2. Representación del tablero**

```text
┌────┬────┬────┬────┬────┬────┬────┬────┐
│  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│  9 │ 10 │ XX │ 12 │ 13 │ 14 │ 15 │ 16 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 17 │ 18 │ XX │ XX │ 21 │ 22 │ 23 │ 24 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 25 │ 26 │ 27 │ XX │ XX │ 30 │ 31 │ 32 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 33 │ 34 │ 35 │ 36 │ XX │ XX │ 39 │ 40 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 41 │ 42 │ 43 │ 44 │ 45 │ XX │ 47 │ 48 │
└────┴────┴────┴────┴────┴────┴────┴────┘
```

Donde:

```text
41 = estado inicial
48 = estado objetivo
XX = obstáculo
```

---

# **3. Elementos del algoritmo A\***

El algoritmo A* utiliza la siguiente fórmula:

```text
F(n) = G(n) + H(n)
```

Donde:

- `G(n)` es el costo real desde la casilla inicial hasta la casilla actual.
- `H(n)` es la estimación desde la casilla actual hasta la meta.
- `F(n)` es el costo total estimado.

El algoritmo selecciona de la lista abierta la casilla que tenga el menor valor de `F`.

---

# **4. Cálculo de la heurística**

Como se permiten movimientos horizontales, verticales y diagonales, se utiliza la distancia diagonal.

La fórmula es:

```text
H = 14 × mínimo(dx, dy) + 10 × (máximo(dx, dy) - mínimo(dx, dy))
```

Donde:

- `dx` es la diferencia de columnas.
- `dy` es la diferencia de filas.
- Cada diagonal cuesta 14.
- Cada movimiento recto cuesta 10.

---

## **4.1 Ejemplo de cálculo para la casilla 41**

La casilla 41 se encuentra en:

```text
Fila 6, columna 1
```

La casilla 48 se encuentra en:

```text
Fila 6, columna 8
```

La diferencia es:

```text
dx = 7 columnas
dy = 0 filas
```

Entonces:

```text
H(41) = 14 × 0 + 10 × (7 - 0)
H(41) = 70
```

Como es el estado inicial:

```text
G(41) = 0
```

Por lo tanto:

```text
F(41) = G(41) + H(41)
F(41) = 0 + 70
F(41) = 70
```

---

# **5. Lista abierta y lista cerrada**
En cada iteración se realiza lo siguiente:

```text
1. Seleccionar la casilla con menor F de la lista abierta.
2. Pasar esa casilla a la lista cerrada.
3. Analizar sus vecinos.
4. Calcular G, H y F.
5. Agregar los vecinos válidos a la lista abierta.
6. Recalcular G cuando se encuentre un camino más corto.
7. Repetir hasta alcanzar la casilla 48.
```

---

# **6. Desarrollo del algoritmo A\***

## **Iteración 1**

Casilla actual:

```text
41
```

Valores:

```text
G = 0
H = 70
F = 70
```

Vecinos disponibles:

- 33: arriba.
- 34: diagonal superior derecha.
- 42: derecha.

### **Cálculos**

#### Casilla 33

```text
G(33) = 0 + 10 = 10
H(33) = 74
F(33) = 10 + 74 = 84
```

#### Casilla 34

```text
G(34) = 0 + 14 = 14
H(34) = 64
F(34) = 14 + 64 = 78
```

#### Casilla 42

```text
G(42) = 0 + 10 = 10
H(42) = 60
F(42) = 10 + 60 = 70
```

### **Lista abierta**

```text
42: G=10, H=60, F=70
34: G=14, H=64, F=78
33: G=10, H=74, F=84
```

### **Lista cerrada**

```text
41
```

Se selecciona la casilla 42 porque tiene el menor valor de `F`.

---

## **Iteración 2**

Casilla actual:

```text
42
```

Vecinos nuevos:

- 35, mediante diagonal.
- 43, mediante movimiento hacia la derecha.

#### Casilla 35

```text
G(35) = G(42) + 14
G(35) = 10 + 14 = 24

H(35) = 54

F(35) = 24 + 54 = 78
```

#### Casilla 43

```text
G(43) = G(42) + 10
G(43) = 10 + 10 = 20

H(43) = 50

F(43) = 20 + 50 = 70
```

### **Lista abierta**

```text
43: G=20, H=50, F=70
34: G=14, H=64, F=78
35: G=24, H=54, F=78
33: G=10, H=74, F=84
```

### **Lista cerrada**

```text
41, 42
```

---

## **Iteración 3**

Casilla actual:

```text
43
```

Vecinos nuevos:

- 36, mediante diagonal.
- 44, mediante movimiento hacia la derecha.

#### Casilla 36

```text
G(36) = 20 + 14 = 34
H(36) = 44
F(36) = 34 + 44 = 78
```

#### Casilla 44

```text
G(44) = 20 + 10 = 30
H(44) = 40
F(44) = 30 + 40 = 70
```

### **Lista abierta**

```text
44: G=30, H=40, F=70
34: G=14, H=64, F=78
35: G=24, H=54, F=78
36: G=34, H=44, F=78
33: G=10, H=74, F=84
```

### **Lista cerrada**

```text
41, 42, 43
```

---

## **Iteración 4**

Casilla actual:

```text
44
```

El vecino válido nuevo es la casilla 45.

#### Casilla 45

```text
G(45) = 30 + 10 = 40
H(45) = 30
F(45) = 40 + 30 = 70
```

### **Lista abierta**

```text
45: G=40, H=30, F=70
34: G=14, H=64, F=78
35: G=24, H=54, F=78
36: G=34, H=44, F=78
33: G=10, H=74, F=84
```

### **Lista cerrada**

```text
41, 42, 43, 44
```

---

## **Iteración 5**

Casilla actual:

```text
45
```

Desde la casilla 45 no se puede continuar directamente hacia la meta porque:

```text
46 es un obstáculo
```

Tampoco se puede realizar una diagonal hacia 38 porque:

```text
38 es un obstáculo
```

La casilla 45 se convierte en un camino sin salida.

### **Lista abierta**

```text
34: G=14, H=64, F=78
35: G=24, H=54, F=78
36: G=34, H=44, F=78
33: G=10, H=74, F=84
```

### **Lista cerrada**

```text
41, 42, 43, 44, 45
```

---

## **Iteración 6**

Se analiza la casilla 36.

```text
G(36) = 34
H(36) = 44
F(36) = 78
```

No puede avanzar hacia la derecha debido a los obstáculos 37 y 29.

### **Lista cerrada**

```text
41, 42, 43, 44, 45, 36
```

---

## **Iteración 7**

Se analiza la casilla 35.

```text
G(35) = 24
H(35) = 54
F(35) = 78
```

Vecinos nuevos:

- Casilla 26.
- Casilla 27.

#### Casilla 26 mediante diagonal

```text
G(26) = 24 + 14 = 38
H(26) = 68
F(26) = 38 + 68 = 106
```

#### Casilla 27 mediante movimiento vertical

```text
G(27) = 24 + 10 = 34
H(27) = 58
F(27) = 34 + 58 = 92
```

### **Lista abierta**

```text
34: G=14, H=64, F=78
33: G=10, H=74, F=84
27: G=34, H=58, F=92
26: G=38, H=68, F=106
```

### **Lista cerrada**

```text
41, 42, 43, 44, 45, 36, 35
```

---

## **Iteración 8: primer recálculo**

Se analiza la casilla 34.

```text
G(34) = 14
H(34) = 64
F(34) = 78
```

Desde 34 se puede llegar a las casillas 25, 26 y 27.

#### Casilla 25

```text
G(25) = 14 + 14 = 28
H(25) = 78
F(25) = 28 + 78 = 106
```

#### Recálculo de la casilla 26

Anteriormente:

```text
G anterior(26) = 38
```

Nuevo camino desde 34:

```text
G nuevo(26) = 14 + 10 = 24
```

Como:

```text
24 < 38
```

Se reemplaza el valor anterior.

```text
G(26) = 24
H(26) = 68
F(26) = 24 + 68 = 92
Padre de 26 = 34
```

#### Recálculo de la casilla 27

Anteriormente:

```text
G anterior(27) = 34
```

Nuevo camino:

```text
G nuevo(27) = 14 + 14 = 28
```

Como:

```text
28 < 34
```

Se actualiza:

```text
G(27) = 28
H(27) = 58
F(27) = 28 + 58 = 86
Padre de 27 = 34
```

### **Lista abierta**

```text
33: G=10, H=74, F=84
27: G=28, H=58, F=86
26: G=24, H=68, F=92
25: G=28, H=78, F=106
```

### **Lista cerrada**

```text
41, 42, 43, 44, 45, 36, 35, 34
```

---

## **Iteración 9: segundo recálculo**

Se analiza la casilla 33.

```text
G(33) = 10
H(33) = 74
F(33) = 84
```

Desde la casilla 33 se puede llegar a 25 con movimiento vertical.

Anteriormente:

```text
G anterior(25) = 28
```

Nuevo camino:

```text
G nuevo(25) = 10 + 10 = 20
```

Como:

```text
20 < 28
```

Se actualiza la casilla 25:

```text
G(25) = 20
H(25) = 78
F(25) = 98
Padre de 25 = 33
```

### **Lista abierta**

```text
27: G=28, H=58, F=86
26: G=24, H=68, F=92
25: G=20, H=78, F=98
```

### **Lista cerrada**

```text
41, 42, 43, 44, 45, 36, 35, 34, 33
```

---

## **Iteración 10**

Se analiza la casilla 27.

```text
G(27) = 28
H(27) = 58
F(27) = 86
```

La casilla no genera un camino mejor debido a los obstáculos:

```text
19, 20 y 28
```

### **Lista cerrada**

```text
41, 42, 43, 44, 45, 36, 35, 34, 33, 27
```

---

## **Iteración 11**

Se analiza la casilla 26.

```text
G(26) = 24
H(26) = 68
F(26) = 92
```

Vecinos nuevos:

- Casilla 17.
- Casilla 18.

#### Casilla 17

```text
G(17) = 24 + 14 = 38
H(17) = 82
F(17) = 38 + 82 = 120
```

#### Casilla 18

```text
G(18) = 24 + 10 = 34
H(18) = 72
F(18) = 34 + 72 = 106
```

### **Lista abierta**

```text
25: G=20, H=78, F=98
18: G=34, H=72, F=106
17: G=38, H=82, F=120
```

---

## **Iteración 12: tercer recálculo**

Se analiza la casilla 25.

```text
G(25) = 20
H(25) = 78
F(25) = 98
```

Desde la casilla 25 se puede llegar a 17 mediante movimiento vertical.

Anteriormente:

```text
G anterior(17) = 38
```

Nuevo camino:

```text
G nuevo(17) = 20 + 10 = 30
```

Como:

```text
30 < 38
```

Se actualiza:

```text
G(17) = 30
H(17) = 82
F(17) = 112
Padre de 17 = 25
```

---

## **Iteración 13**

Se analiza la casilla 18.

```text
G(18) = 34
H(18) = 72
F(18) = 106
```

Vecinos nuevos:

- Casilla 9.
- Casilla 10.

#### Casilla 9

```text
G(9) = 34 + 14 = 48
H(9) = 86
F(9) = 134
```

#### Casilla 10

```text
G(10) = 34 + 10 = 44
H(10) = 76
F(10) = 120
```

---

## **Iteración 14: cuarto recálculo**

Se analiza la casilla 17.

Desde 17 se puede llegar a 9 con movimiento vertical.

Anteriormente:

```text
G anterior(9) = 48
```

Nuevo camino:

```text
G nuevo(9) = 30 + 10 = 40
```

Como:

```text
40 < 48
```

Se actualiza:

```text
G(9) = 40
H(9) = 86
F(9) = 126
Padre de 9 = 17
```

---

## **Iteración 15**

Se analiza la casilla 10.

```text
G(10) = 44
H(10) = 76
F(10) = 120
```

Vecinos nuevos:

- Casilla 1.
- Casilla 2.

#### Casilla 1

```text
G(1) = 44 + 14 = 58
H(1) = 90
F(1) = 148
```

#### Casilla 2

```text
G(2) = 44 + 10 = 54
H(2) = 80
F(2) = 134
```

---

## **Iteración 16: quinto recálculo**

Se analiza la casilla 9.

Desde 9 se puede llegar a 1 con movimiento vertical.

Anteriormente:

```text
G anterior(1) = 58
```

Nuevo camino:

```text
G nuevo(1) = 40 + 10 = 50
```

Como:

```text
50 < 58
```

Se actualiza:

```text
G(1) = 50
H(1) = 90
F(1) = 140
Padre de 1 = 9
```

---

## **Iteración 17**

Se analiza la casilla 2.

```text
G(2) = 54
H(2) = 80
F(2) = 134
```

Se genera la casilla 3.

```text
G(3) = 54 + 10 = 64
H(3) = 70
F(3) = 134
```

---

## **Iteración 18**

Se analiza la casilla 3.

Se genera la casilla 4.

```text
G(4) = 64 + 10 = 74
H(4) = 66
F(4) = 140
```

---

## **Iteración 19**

Se analiza la casilla 4.

Vecinos nuevos:

- Casilla 5.
- Casilla 12.
- Casilla 13.

#### Casilla 5

```text
G(5) = 74 + 10 = 84
H(5) = 62
F(5) = 146
```

#### Casilla 12

```text
G(12) = 74 + 10 = 84
H(12) = 56
F(12) = 140
```

#### Casilla 13

```text
G(13) = 74 + 14 = 88
H(13) = 52
F(13) = 140
```

Se selecciona la casilla 13 porque tiene menor `H` entre las casillas con el mismo valor de `F`.

---

## **Iteración 20**

Se analiza la casilla 13.

Vecinos principales:

- Casilla 21.
- Casilla 22.

#### Casilla 21

```text
G(21) = 88 + 10 = 98
H(21) = 42
F(21) = 140
```

#### Casilla 22

```text
G(22) = 88 + 14 = 102
H(22) = 38
F(22) = 140
```

Se selecciona la casilla 22 porque tiene menor `H`.

---

## **Iteración 21**

Se analiza la casilla 22.

Vecinos nuevos:

- 23.
- 30.
- 31.

#### Casilla 23

```text
G(23) = 102 + 10 = 112
H(23) = 34
F(23) = 146
```

#### Casilla 30

```text
G(30) = 102 + 10 = 112
H(30) = 28
F(30) = 140
```

#### Casilla 31

```text
G(31) = 102 + 14 = 116
H(31) = 24
F(31) = 140
```

Se selecciona la casilla 31.

---

## **Iteración 22**

Se analiza la casilla 31.

Vecinos principales:

- Casilla 39.
- Casilla 40.

#### Casilla 39

```text
G(39) = 116 + 10 = 126
H(39) = 14
F(39) = 140
```

#### Casilla 40

```text
G(40) = 116 + 14 = 130
H(40) = 10
F(40) = 140
```

Se selecciona la casilla 40 porque tiene menor `H`.

---

## **Iteración 23**

Se analiza la casilla 40.

Desde la casilla 40 se puede llegar directamente a la meta 48 mediante movimiento vertical.

#### Casilla 48

```text
G(48) = 130 + 10 = 140
H(48) = 0
F(48) = 140
```

También puede encontrarse la casilla 47, pero su valor es mayor.

#### Casilla 47

```text
G(47) = 130 + 14 = 144
H(47) = 10
F(47) = 154
```

La casilla 48 tiene el menor valor de `F`, por lo que se selecciona.

---

# **7. Lista cerrada final**

El orden de expansión de las casillas es:

```text
41, 42, 43, 44, 45, 36, 35, 34, 33, 27, 26, 25,
18, 17, 10, 9, 2, 3, 4, 13, 22, 31, 40, 48
```

La casilla 48 es el estado objetivo, por lo que el algoritmo termina.

---

# **8. Recálculos realizados**

Durante la ejecución del algoritmo se encontraron caminos más cortos hacia algunas casillas.

| Casilla | G anterior | G nuevo | Casilla de procedencia |
|---:|---:|---:|---:|
| 26 | 38 | 24 | 34 |
| 27 | 34 | 28 | 34 |
| 25 | 28 | 20 | 33 |
| 17 | 38 | 30 | 25 |
| 9 | 48 | 40 | 17 |
| 1 | 58 | 50 | 9 |

Un recálculo ocurre cuando:

```text
G nuevo < G anterior
```

Cuando esto sucede, se reemplaza el valor de `G`, se calcula nuevamente `F` y se modifica el padre de la casilla.

---

# **9. Reconstrucción de la ruta**

Para reconstruir la ruta se comienza desde la casilla 48 y se siguen sus padres hasta llegar a 41.

```text
48 ← 40 ← 31 ← 22 ← 13 ← 4 ← 3 ← 2 ← 10 ← 18 ← 26 ← 34 ← 41
```

Al invertir el orden se obtiene la ruta correcta:

```text
41 → 34 → 26 → 18 → 10 → 2 → 3 → 4 → 13 → 22 → 31 → 40 → 48
```

---

# **10. Ruta final en el tablero**

```text
┌────┬────┬────┬────┬────┬────┬────┬────┐
│  1 │  2*│  3*│  4*│  5 │  6 │  7 │  8 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│  9 │ 10*│ XX │ 12 │ 13*│ 14 │ 15 │ 16 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 17 │ 18*│ XX │ XX │ 21 │ 22*│ 23 │ 24 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 25 │ 26*│ 27 │ XX │ XX │ 30 │ 31*│ 32 │
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 33 │ 34*│ 35 │ 36 │ XX │ XX │ 39 │ 40*│
├────┼────┼────┼────┼────┼────┼────┼────┤
│ 41*│ 42 │ 43 │ 44 │ 45 │ XX │ 47 │ 48*│
└────┴────┴────┴────┴────┴────┴────┴────┘
```

Donde:

```text
* = casilla perteneciente a la ruta final
XX = obstáculo
```

---

# **11. Cálculo del costo total**

La ruta es:

```text
41 → 34 → 26 → 18 → 10 → 2 → 3 → 4 → 13 → 22 → 31 → 40 → 48
```

Movimientos realizados:

| Movimiento | Tipo | Costo |
|---|---|---:|
| 41 → 34 | Diagonal | 14 |
| 34 → 26 | Vertical | 10 |
| 26 → 18 | Vertical | 10 |
| 18 → 10 | Vertical | 10 |
| 10 → 2 | Vertical | 10 |
| 2 → 3 | Horizontal | 10 |
| 3 → 4 | Horizontal | 10 |
| 4 → 13 | Diagonal | 14 |
| 13 → 22 | Diagonal | 14 |
| 22 → 31 | Diagonal | 14 |
| 31 → 40 | Diagonal | 14 |
| 40 → 48 | Vertical | 10 |

El costo total es:

```text
14 + 10 + 10 + 10 + 10 + 10 + 10 + 14 + 14 + 14 + 14 + 10
```

```text
Costo total = 140
```

---

# **12. Tabla de valores de la ruta final**

| Casilla | G | H | F | Padre |
|---:|---:|---:|---:|---:|
| 41 | 0 | 70 | 70 | Inicio |
| 34 | 14 | 64 | 78 | 41 |
| 26 | 24 | 68 | 92 | 34 |
| 18 | 34 | 72 | 106 | 26 |
| 10 | 44 | 76 | 120 | 18 |
| 2 | 54 | 80 | 134 | 10 |
| 3 | 64 | 70 | 134 | 2 |
| 4 | 74 | 66 | 140 | 3 |
| 13 | 88 | 52 | 140 | 4 |
| 22 | 102 | 38 | 140 | 13 |
| 31 | 116 | 24 | 140 | 22 |
| 40 | 130 | 10 | 140 | 31 |
| 48 | 140 | 0 | 140 | 40 |

---

# **13. Restricción de no recortar esquinas**

En este ejercicio no se permite atravesar diagonalmente entre obstáculos.

Por ejemplo, desde la casilla 45 no se puede avanzar diagonalmente hacia la parte superior derecha porque las casillas cercanas contienen obstáculos:

```text
37 = obstáculo
38 = obstáculo
46 = obstáculo
```

Una diagonal solamente se considera válida cuando las dos casillas laterales necesarias están libres.

Esto evita que el agente atraviese esquinas de paredes u obstáculos.

---

# **15. Resultado final**

La ruta óptima encontrada por el algoritmo A* es:

```text
41 → 34 → 26 → 18 → 10 → 2 → 3 → 4 → 13 → 22 → 31 → 40 → 48
```

El costo total es:

```text
140
```

La lista cerrada final es:

```text
41, 42, 43, 44, 45, 36, 35, 34, 33, 27, 26, 25,
18, 17, 10, 9, 2, 3, 4, 13, 22, 31, 40, 48
```

Los principales recálculos fueron:

```text
26: G = 38 → 24
27: G = 34 → 28
25: G = 28 → 20
17: G = 38 → 30
9:  G = 48 → 40
1:  G = 58 → 50
```

---
