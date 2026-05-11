
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

## Resultados
F1-score: 0.96

## Dataset
# 📊 Dataset

El dataset utilizado en este proyecto fue construido a partir de correos electrónicos reales extraídos del buzón institucional del área de Registro de la Universidad San Francisco de Quito (USFQ).

Los datos corresponden a solicitudes administrativas reales recibidas durante aproximadamente un año de operación institucional.

## Procesamiento del dataset

El conjunto de datos fue sometido a múltiples procesos de depuración y preparación, incluyendo:

- Limpieza de texto
- Eliminación de ruido y correos irrelevantes
- Filtrado de respuestas automáticas
- Normalización de contenido
- Anonimización de información sensible mediante técnicas NER utilizando SpaCy

El dataset final utilizado para entrenamiento estuvo compuesto por aproximadamente 25,400 correos electrónicos anonimizados.
Por motivos de privacidad y confidencialidad institucional, el dataset original no se encuentra disponible públicamente.

## Categorías de clasificación

El modelo fue entrenado para clasificar correos electrónicos en las siguientes categorías:

- Certificados
- Registro y Retiro de Materias
- Proceso de Graduación
- Otros Trámites

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

## Ejecución del Proyecto

## 1. Clonar el repositorio

1. ```bash
git clone https://github.com/SoniaCamila13/Clasificacion_correos_BERT_USFQ.git
2. cd Clasificacion_correos_BERT_USFQ
3. pip install -r requirements.txt
4. Ejecutar notebooks
5. Ejecutar predicción
python scripts/predict.py

Los notebooks pueden abrirse y ejecutarse utilizando:
-Jupyter Notebook
-Google Colab

El script permite ingresar texto manualmente y ejecutar una predicción utilizando el pipeline de clasificación.

## Estructura del Repositorio

---

# 📂 Estructura del Repositorio
```plaintext
Clasificacion_correos_BERT_USFQ/
│
├── data/
│   └── README_dataset.md
│
├── docs/
│
├── notebooks/
│   ├── 01_preprocesamiento_y_anonimizacion.ipynb
│   ├── 02_modelo_baseline.ipynb
│   ├── 03_entrenamiento_BERT.ipynb
│   ├── 04_experimentacion_y_tuning.ipynb
│   └── 05_evaluacion_final.ipynb
│
├── results/
│
├── scripts/
│   └── predict.py
│
├── README.md
└── requirements.txt

## Descripción de Carpetas
| Carpeta      | Contenido                               |
| ------------ | --------------------------------------- |
| `data/`      | Información y documentación del dataset |
| `docs/`      | Documentación adicional y anexos        |
| `notebooks/` | Desarrollo experimental y entrenamiento |
| `results/`   | Resultados, métricas y gráficas         |
| `scripts/`   | Scripts ejecutables del prototipo       |


## Autor
Camila Cruz
