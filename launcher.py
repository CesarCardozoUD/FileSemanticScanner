import tkinter as tk
from tkinter import filedialog
from orchestrator import exec
import json

class App:
    def __init__(self, root):
        self.root = root

        # :::::::: FRAME TK ::::::::
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        # :::::::: STATE VARS ::::::::
        self.match_case = tk.BooleanVar(value=False)
        self.match_whole = tk.BooleanVar(value=False)

        # :::::::: INPUT ::::::::
        self.entry = tk.Entry(frame, width=40)
        self.entry.grid(column=0, row=0, columnspan=2)

        # :::::::: TOOGLE (Match-Case) ::::::::
        self.chk_case = tk.Checkbutton(
            frame,
            text="Aa",
            variable=self.match_case
        )
        self.chk_case.grid(column=2, row=0, padx=5)

        # :::::::: TOOGLE (TEXTO COMPLETO) ::::::::
        self.chk_whole = tk.Checkbutton(
            frame,
            text="ab",
            variable=self.match_whole
        )
        self.chk_whole.grid(column=3, row=0, padx=5)
        
        # :::::::: FILE CHOOSER ::::::::
        self.btn_folder = tk.Button(frame, text="Seleccionar carpeta", command=self.seleccionar_carpeta)
        self.btn_folder.grid(column=0, row=1, columnspan=2, pady=5)

        # :::::::: EJECUTAR BTN ::::::::
        self.btn_exec = tk.Button(frame, text="Buscar", command=self.ejecutar)
        self.btn_exec.grid(column=2, row=1, columnspan=2 ,pady=10)

        # :::::::: OUTPUT ::::::::
        self.output = tk.Text(frame)
        self.output.grid(column=0, row=2, columnspan=4, rowspan=4)

        # :::::::: INIT ::::::::
        self.ruta = None

    def seleccionar_carpeta(self):
        self.ruta = filedialog.askdirectory()
        self.output.insert(tk.END, f"Carpeta: {self.ruta}\n")

    def ejecutar(self):
        self.output.delete(1.0, tk.END)
        self.output.see(tk.END)
        texto = self.entry.get()

        self.output.insert(tk.END, f"\nTexto: {texto}\n")
        self.output.insert(tk.END, f"Ruta: {self.ruta}\n")
        self.output.insert(tk.END, "::::::::::::: INICIANDO ESCANEO 🚀 :::::::::::::\n\n")

        response_json, exec_time = exec(self.match_whole.get(), self.match_case.get(), self.ruta, texto)
        pretty_json = json.dumps(response_json, indent=4, ensure_ascii=False)
        self.output.insert(tk.END, pretty_json)

        self.output.insert(tk.END, f"\n\n ::::::::::::: ESCANEO FINALIZADO EN {exec_time} ::::::::::::: \n\n")


root = tk.Tk()
app = App(root)
root.mainloop()
