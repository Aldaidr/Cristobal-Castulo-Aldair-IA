# **EDA para identificar Bochos y Cybertrucks**

## **Objetivo**

Crear un EDA para identificar y diferenciar vehículos tipo **Volkswagen Sedán (Bocho)** y **Tesla Cybertruck** mediante imágenes capturadas por una cámara.

---

## **Introducción**

En este proyecto se busca realizar un análisis para comprender cómo se pueden capturar y analizar imágenes de vehículos mediante una cámara. Antes de crear un modelo de clasificación, es necesario estudiar las condiciones de captura, la calidad de las imágenes, la iluminación, el ángulo del vehículo y las características del dataset.

---

## **Dataset**

| imagen | tipo de vehículo | vista | color | iluminación | identificado |
|---------|------------------|--------|--------|--------------|---------------|
| img001.jpg | Bocho | Frontal | Azul | Día | Sí |
| img002.jpg | Cybertruck | Lateral | Gris | Día | Sí |
| img003.jpg | Bocho | Trasera | Blanco | Noche | Sí |
| img004.jpg | Cybertruck | Frontal | Plata | Sombra | Sí |
| img005.jpg | Bocho | Lateral | Rojo | Día | Sí |

---

## **Variables del dataset**

- Imagen.
- Tipo de vehículo.
- Vista (frontal, lateral o trasera).
- Color.
- Iluminación.
- Resultado de la identificación.

---

## **Preguntas del EDA**

- ¿La iluminación afecta la identificación del vehículo?
- ¿Qué vista permite identificar mejor un Bocho?
- ¿Qué vista permite identificar mejor un Cybertruck?
- ¿El color influye en la clasificación?
- ¿Existen imágenes difíciles de clasificar?
- ¿Cuál es el porcentaje de aciertos del modelo?

---

# **EDA para identificar rostros de personas mediante una cámara**

## **Objetivo**

EDA para identificar rostros de personas con la ayuda de una cámara.

---

## **Introducción**
Antes de crear un modelo de reconocimiento facial, es necesario estudiar las condiciones de captura, la calidad de las imágenes, la iluminación, la posición del rostro y las características del dataset.

---

## **Dataset**

| nombre | video | parpadea | lentes | persona autorizada | acceso |
|---------|--------|-----------|---------|--------------------|---------|
| Juan | Sí | No | No | Sí | Permitido |
| María | Sí | Sí | Sí | Sí | Permitido |
| Alberto | Sí | No | No | No | Denegado |

---

## **Variables del dataset**

- Nombre de la persona.
- Video capturado.
- Parpadeo.
- Uso de lentes.
- Persona autorizada.
- Acceso permitido o denegado.

---

## **Preguntas del EDA**

- ¿El uso de lentes afecta el reconocimiento facial?
- ¿El parpadeo influye en la identificación?
- ¿La iluminación modifica la precisión del reconocimiento?
- ¿Qué posiciones del rostro generan mayor número de errores?
- ¿Cuántas personas autorizadas existen en la base de datos?
- ¿Cuántos accesos fueron permitidos y cuántos fueron denegados?