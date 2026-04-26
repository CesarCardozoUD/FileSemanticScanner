import datetime
import math
from files_utils import process_path
from text_analyzer import RawTextAnalyzer


def exec(texto_exacto, ignore_case, path, search_values):
    ini = datetime.datetime.now()
    params = {
        "root": path,
        "Aa": ignore_case,
        "ab": texto_exacto,
        "text_to_search": search_values
    }

    print("PARAMS: ", params)

    ignore_case = not ignore_case
    pdf_txt, pdf_ocr = process_path(path)
    analyzer = RawTextAnalyzer(search_values, texto_exacto, ignore_case)
    rs = analyzer.procesar_pdfs_texto(pdf_txt)

    end = datetime.datetime.now()
    secs = (end-ini).total_seconds()
    mins = math.floor(secs/60)
    secs = math.ceil(secs - (mins * 60))
    exec_time = f"{mins} Minutos y {secs} Segundos"

    return rs, exec_time