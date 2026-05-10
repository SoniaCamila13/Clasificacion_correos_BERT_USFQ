
# Clasificación Automática de Correos Institucionales mediante BERT

## Descripción
Este proyecto implementa un prototipo de Inteligencia Artificial basado en modelos de lenguaje BERT para la clasificación automática de correos electrónicos institucionales del área de Registro de la Universidad San Francisco de Quito (USFQ).

El objetivo principal es optimizar el proceso de categorización de solicitudes estudiantiles y administrativas, reduciendo tiempos de respuesta, minimizando errores manuales y mejorando la eficiencia operativa del departamento.

El sistema utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) y aprendizaje profundo para identificar automáticamente la categoría correspondiente de cada correo electrónico recibido.

## Objetivos
Objetivo General
Desarrollar un modelo de clasificación automática de correos institucionales utilizando BERT para apoyar los procesos administrativos del área de Registro de la USFQ.

Objetivos Específicos
Preprocesar y limpiar correos electrónicos institucionales.
Implementar un modelo basado en BERT para clasificación de texto.
Evaluar el desempeño del modelo mediante métricas de clasificación.
Comparar resultados frente a modelos tradicionales de Machine Learning.
Generar un prototipo funcional y reproducible.

## Arquitectura General
Correos electrónicos
        ↓
Preprocesamiento de texto
        ↓
Tokenización
        ↓
Modelo BERT
        ↓
Clasificación automática
        ↓
Predicción de categoría

## Pipeline del Proyecto
1. Recolección de datos: Obtención y anonimización de correos institucionales.

2. Preprocesamiento
-Limpieza de texto
-Eliminación de caracteres especiales
-Conversión a minúsculas
-Tokenización

3. Entrenamiento: Fine-tuning del modelo BERT utilizando datos etiquetados.

4. Evaluación: Validación mediante métricas de clasificación.

5. Predicción: Clasificación automática de nuevos correos electrónicos.

## Tecnologías
| Tecnología       | Descripción                |
| ---------------- | -------------------------- |
| Python 3.11      | Lenguaje principal         |
| BERT             | Modelo de lenguaje         |
| Transformers     | Librería Hugging Face      |
| PyTorch          | Framework de Deep Learning |
| Pandas           | Manipulación de datos      |
| NumPy            | Operaciones numéricas      |
| Scikit-learn     | Métricas y validación      |
| Matplotlib       | Visualización              |
| Jupyter Notebook | Desarrollo experimental    |


## Resultados
F1-score: 0.96

## Autor
Camila Cruz
