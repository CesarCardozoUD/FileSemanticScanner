import pdfplumber
from pathlib import Path


def es_pdf_con_texto(ruta_pdf, min_chars=50):
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            texto_total = ""

            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto

            return len(texto_total.strip()) > min_chars

    except Exception as e:
        print(f"Error con {ruta_pdf}: {e}")
        return False
    
def clasify_pdf(ruta_base):
    lista_docs_texto = []
    lista_docs_ocr = []

    print(f"RUTA -> {ruta_base}")

    for pdf in ruta_base.rglob("*.pdf"):
        ruta= f"{pdf}"
        if es_pdf_con_texto(pdf):
            lista_docs_texto.append(ruta)
        else:
            lista_docs_ocr.append(ruta)
    
    return lista_docs_texto, lista_docs_ocr

def process_path(new_ruta):
    ruta_base = Path(new_ruta)
    return clasify_pdf(ruta_base)