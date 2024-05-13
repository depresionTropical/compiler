import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext


class Tabla(tk.Frame):
    def __init__(self, master, titulo, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.titulo = titulo
        
        # Crear la etiqueta para el título
        self.etiqueta_titulo = tk.Label(self, text=self.titulo)
        self.etiqueta_titulo.pack(pady=5)

        # Crear el área de texto
        self.text_area = scrolledtext.ScrolledText(self, width=40, height=10)
        self.text_area.pack(expand=True, fill='both')

    def cargar_texto(self, texto):
        self.text_area.delete(1.0, tk.END)  # Limpiar contenido anterior
        self.text_area.insert(tk.END, texto)