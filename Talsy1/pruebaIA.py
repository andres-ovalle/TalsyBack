from transformers import pipeline
import numpy as np
from back.services.Extract import PDFTextExtractor
print(np.__version__)

# Cargar pipeline de NER con un modelo preentrenado en español
ner_pipeline = pipeline("ner", model="mrm8488/bert-spanish-cased-finetuned-ner", grouped_entities=True)

# Texto de ejemplo
t = PDFTextExtractor()
print("Texto desde la clase de extracion: {t}")
text = t
# Procesar texto
results = ner_pipeline(text)

# Filtrar solo entidades tipo 'PER' (Personas)
for entity in results:
    if entity['entity_group'] == 'PER':
        print(f"Nombre encontrado: {entity['word']}")
