
import spacy
import fitz  # PyMuPDF
import re
import json
import subprocess

class PDFTextExtractor:
    def __init__(self):
        """Cargar modelo NLP de spaCy."""
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Modelo 'en_core_web_sm' no encontrado. Instalando...")
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")

    def extract_text_from_pdf(self, pdf_path):
        """Lee el contenido del PDF y lo devuelve como texto."""
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page_num in range(doc.page_count):
                text += doc.load_page(page_num).get_text("text")
            doc.close()
            return text
        except Exception as e:
            print(f"Error al leer el PDF: {e}")
            return ""

    def clean_text(self, text):
        """Limpia el texto eliminando saltos de línea, espacios extra y caracteres especiales."""
        text = re.sub(r"[\r\n\t]+", " ", text)  # Eliminar saltos de línea y tabs
        text = re.sub(r"[♀♂]", " ", text)  # Eliminar caracteres especiales específicos
        text = re.sub(r"[^\w\s@.+-]", " ", text)  # Eliminar caracteres no alfanuméricos
        text = re.sub(r"\s+", " ", text).strip()  # Reemplazar múltiples espacios por uno solo
        text = re.sub(r"[^A-Za-z0-9áéíóúñüÁÉÍÓÚÑÜ\s@.\-]+", " ", text)
        text = re.sub(r"\s+", " ", text).strip()  # Limpiar espacios

        print("Texto limpio:", text)  # Imprimir texto limpio
        return text

    def extract_info_from_text(self, text):
        """Extrae la información más relevante de la hoja de vida."""
        doc = self.nlp(text)
        info = {
            "nombre": None,
            "correos": [],
            "teléfonos": [],
            "habilidades": [],
            "experiencia": [],
        }

        # 1. Extraer Nombre (asumiendo que es la primera entidad PERSON encontrada)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                info["nombre"] = ent.text
                break

        # 2. Extraer correos electrónicos
        info["correos"] = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text
        )

        # 3. Extraer números de teléfono
        info["teléfonos"] = re.findall(
            r"\+?\d{1,3}[\s-]?\(?\d{1,4}\)?[\s-]?\d{1,4}[\s-]?\d{1,4}", text
        )

        # 4. Extraer habilidades
        habilidades_comunes = ["Python", "Java", "SQL", "Machine Learning", "NLP", "Git"]
        info["habilidades"] = [
            habilidad for habilidad in habilidades_comunes if habilidad in text
        ]

        # 5. Extraer experiencia laboral
        for sent in doc.sents:
            if "experiencia" in sent.text.lower() or "trabajo" in sent.text.lower():
                info["experiencia"].append(sent.text)

        return info

    def extract_info_from_pdf(self, pdf_path):
        """Extrae la información del PDF y la devuelve en formato JSON."""
        text = self.extract_text_from_pdf(pdf_path)
        if not text:
            return json.dumps(
                {"error": "No se pudo extraer texto del PDF"}, indent=4, ensure_ascii=False
            )

        cleaned_text = self.clean_text(text)
        info = self.extract_info_from_text(cleaned_text)
        return json.dumps(info, indent=4, ensure_ascii=False)

    def extract_clean_text(self, pdf_path):
        """Devuelve el texto limpio extraído del PDF."""
        text = self.extract_text_from_pdf(pdf_path)
        return self.clean_text(text)


# Ejemplo de uso
if __name__ == "__main__":
    pdf_path = r"C:\Users\AreaMovil\Documents\Mauro\semestre10\Talsy1.0\back\Data\samples\HV-DanielOcampo.pdf"
    extractor = PDFTextExtractor()

    # Extraer y mostrar la información relevante en JSON
    json_info = extractor.extract_info_from_pdf(pdf_path)
    print(json_info)

    # Extraer solo el texto limpio
    clean_text = extractor.extract_clean_text(pdf_path)
    print("Texto limpio extraído:", clean_text)
