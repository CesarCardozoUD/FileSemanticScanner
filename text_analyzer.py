import pdfplumber
import unicodedata
import re

class RawTextAnalyzer:
    def __init__(self, search_values, texto_exacto, ignore_case):
        if isinstance(search_values, str):
            search_values = [search_values]

        if ignore_case:
            self.search_values = [v.lower() for v in search_values]
        else: 
            self.search_values = search_values

        self.texto_exacto = texto_exacto
        print(self.texto_exacto)
        self.ignore_case = ignore_case
        print(self.ignore_case)
    
    def limpiar_texto(self, texto):
        if self.ignore_case:
            texto = texto.lower()

        if not self.texto_exacto:
            texto = unicodedata.normalize("NFD", texto)
            texto = texto.encode("ascii", "ignore").decode("utf-8")

        return texto

    def extraer_texto_pdf(self, ruta_pdf):
        texto_total = ""
        try:
            with pdfplumber.open(ruta_pdf) as pdf:
                for pagina in pdf.pages:
                    texto = pagina.extract_text()
                    if texto:
                        texto_total += texto + "\n"
        except Exception as e:
            print(f"Error leyendo {ruta_pdf}: {e}")

        if self.texto_exacto:
            return texto_total
        else:
            return self.limpiar_texto(texto_total)
    
    def encontrar_valores(self, texto):
        resultados = []
        palabras = re.findall(r'\b\w+\b', texto)

        for palabra in palabras:
            for val in self.search_values:
                if self.texto_exacto:
                    if palabra == val:
                        resultados.append({
                            "buscado": val,
                            "coincidencia": palabra
                        })
                else:
                    if val in palabra:
                        resultados.append({
                            "buscado": val,
                            "coincidencia": palabra
                        })

        return resultados
    
    def procesar_pdfs_texto(self, lista_pdfs):
        resultados = {}
        for pdf in lista_pdfs:
            texto = self.extraer_texto_pdf(pdf)
            ciudades_encontradas = self.encontrar_valores(texto)

            if ciudades_encontradas:
                resultados[pdf] = ciudades_encontradas

        return resultados