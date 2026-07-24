<div align="center">

# **INSTITUTO TECNOLÓGICO DE MORELIA**

## **Ingeniería en Sistemas Computacionales**

---

# **Inteligencia Artificial Verano**

## **Eigenfaces, Fisherfaces y LBPH**

---

### **Presenta:**
## **Cristóbal Cástulo Aldair**

### **Profesor:**
**JESÚS EDUARDO ALCARAZ CHÁVEZ**

### **Fecha:**
**21 de julio de 2026**

</div>

---

## Introducción

El reconocimiento facial es una de las aplicaciones más importantes de la visión por computadora y la inteligencia artificial. Su objetivo es identificar o verificar la identidad de una persona a partir de las características de su rostro.

OpenCV ofrece diferentes algoritmos para realizar esta tarea. Entre los más utilizados se encuentran Eigenfaces, Fisherfaces y Local Binary Patterns Histograms (LBPH). Cada uno utiliza una estrategia diferente para reconocer los rostros y presenta ventajas y desventajas dependiendo de las condiciones de iluminación, expresiones faciales y calidad de las imágenes.

En este trabajo se analizan estos tres algoritmos, se comparan sus características y se explica de forma general el funcionamiento del código utilizado para el reconocimiento facial.

---

# ¿Qué es Eigenfaces?

Eigenfaces es uno de los primeros algoritmos utilizados para el reconocimiento facial. Está basado en el método PCA (Principal Component Analysis), cuyo objetivo es reducir la cantidad de información de una imagen conservando únicamente las características más importantes.

Cada rostro es representado como un conjunto de componentes principales llamados *eigenfaces*, los cuales permiten comparar una imagen con las almacenadas durante el entrenamiento.

### Ventajas

- Entrenamiento rápido.
- Reduce considerablemente la cantidad de datos.
- Fácil de implementar.

### Desventajas

- Muy sensible a cambios de iluminación.
- Disminuye su precisión cuando existen diferentes expresiones faciales.
- Puede confundirse con rostros similares.

---

# ¿Qué es Fisherfaces?

Fisherfaces es una mejora sobre Eigenfaces. Este algoritmo utiliza primero PCA para reducir la dimensionalidad y posteriormente aplica LDA (Linear Discriminant Analysis), lo que permite separar mejor las características de cada persona.

Su principal objetivo es maximizar la diferencia entre personas distintas y minimizar las diferencias entre imágenes de una misma persona.

### Ventajas

- Mayor precisión que Eigenfaces.
- Mejor comportamiento ante cambios de iluminación.
- Tolera mejor diferentes expresiones faciales.

### Desventajas

- Requiere más imágenes durante el entrenamiento.
- El entrenamiento es más lento.
- Consume más recursos computacionales.

---

# ¿Qué es LBPH?

LBPH (Local Binary Patterns Histograms) es un algoritmo basado en texturas. En lugar de analizar toda la imagen como los métodos anteriores, estudia pequeños patrones presentes en cada región del rostro.

Posteriormente construye histogramas que representan dichas características y los utiliza para realizar la comparación entre rostros.

Es uno de los algoritmos más utilizados en aplicaciones reales debido a su buena precisión y facilidad de entrenamiento.

### Ventajas

- Funciona bien con cambios de iluminación.
- Tolera pequeñas variaciones de posición.
- Entrenamiento sencillo.
- Buena precisión con pocos recursos.

### Desventajas

- Puede disminuir su rendimiento cuando existen grandes cambios en la orientación del rostro.
- Generalmente necesita más tiempo durante la fase de reconocimiento que Eigenfaces.

---

# Comparativa entre Eigenfaces, Fisherfaces y LBPH

| Característica | Eigenfaces | Fisherfaces | LBPH |
|----------------|------------|-------------|------|
| Método | PCA | PCA + LDA | Local Binary Patterns |
| Precisión | Media | Alta | Alta |
| Iluminación | Muy sensible | Poco sensible | Muy poco sensible |
| Expresiones faciales | Sensible | Buena tolerancia | Buena tolerancia |
| Entrenamiento | Muy rápido | Medio | Rápido |
| Uso de memoria | Bajo | Medio | Medio |
| Aplicaciones reales | Poco frecuente | Frecuente | Muy frecuente |

---

# Funcionamiento general del código

El programa de reconocimiento facial sigue una serie de pasos para identificar correctamente a una persona.

## 1. Importación de librerías

Se importan librerías como OpenCV y NumPy, las cuales permiten trabajar con imágenes, matrices y algoritmos de reconocimiento facial.

---

## 2. Carga del conjunto de imágenes

El programa recorre todas las carpetas donde se encuentran almacenadas las imágenes de entrenamiento.

Cada carpeta representa una persona diferente.

---

## 3. Asignación de etiquetas

Cada persona recibe una etiqueta numérica (label).

Por ejemplo:

- Persona 1 → 0
- Persona 2 → 1
- Persona 3 → 2

Estas etiquetas son utilizadas por el algoritmo durante el entrenamiento.

---

## 4. Entrenamiento del modelo

Dependiendo del algoritmo seleccionado, el programa crea uno de los siguientes modelos:

```python
cv2.face.EigenFaceRecognizer_create()

cv2.face.FisherFaceRecognizer_create()

cv2.face.LBPHFaceRecognizer_create()
```

Posteriormente se ejecuta el entrenamiento utilizando todas las imágenes junto con sus respectivas etiquetas.

---

## 5. Captura de video

El programa activa la cámara mediante OpenCV y comienza a capturar imágenes en tiempo real.

---

## 6. Detección del rostro

Utilizando Haar Cascade, OpenCV detecta la ubicación del rostro dentro de cada imagen.

El rostro encontrado se convierte a escala de grises antes de enviarlo al algoritmo de reconocimiento.

---

## 7. Predicción

El modelo entrenado recibe la imagen del rostro mediante el método:

```python
modelo.predict()
```

Como resultado devuelve:

- La persona reconocida.
- Un valor de confianza.

Mientras menor sea el valor de confianza, mayor será la probabilidad de que el reconocimiento sea correcto.

---

## 8. Visualización

Finalmente el programa muestra:

- Un rectángulo alrededor del rostro.
- El nombre de la persona identificada.
- Un mensaje indicando si el rostro es desconocido cuando no existe coincidencia suficiente.

---

# Diferencias principales

Eigenfaces trabaja con la información global de la imagen utilizando PCA.

Fisherfaces mejora este procedimiento incorporando LDA para separar mejor las distintas clases de personas.

LBPH utiliza un enfoque diferente basado en patrones locales de textura, lo que le permite obtener mejores resultados cuando existen cambios de iluminación o pequeñas variaciones en el rostro.

---

# Conclusión

Los tres algoritmos permiten realizar reconocimiento facial utilizando OpenCV; sin embargo, presentan diferencias importantes en cuanto a precisión, velocidad y resistencia a las variaciones de las imágenes.

Eigenfaces es el algoritmo más sencillo y rápido, aunque es sensible a cambios de iluminación. Fisherfaces mejora la precisión al separar mejor las características de cada persona mediante LDA. Finalmente, LBPH destaca por su robustez y facilidad de implementación, siendo una de las opciones más utilizadas en aplicaciones reales debido a su buen desempeño incluso cuando las condiciones de captura no son ideales.