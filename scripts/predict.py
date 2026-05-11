
from transformers import pipeline

# Cargar pipeline de clasificación
classifier = pipeline(
    "text-classification",
    model="bert-base-uncased"
)

print("=== Clasificación de Correos USFQ ===")

# Ingresar texto
texto = input("Ingrese el contenido del correo: ")

# Predicción
resultado = classifier(texto)

# Mostrar resultado
print("\nResultado:")
print(resultado)
