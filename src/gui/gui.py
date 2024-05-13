import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from gui.table import Tabla

class Window:
    def __init__(self, ventana=None, title="Compilador"):
        if ventana is None:
            ventana = tk.Tk()
        
        
        self.ventana = ventana
        self.ventana.title(title)
        self.ventana.geometry("800x600")  # Tamaño de la ventana

        # Configurar el comportamiento de expansión y llenado de la ventana
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(0, weight=3)  # Proporción 30/70
        self.ventana.grid_columnconfigure(1, weight=7)  # Proporción 30/70
        self.ventana.grid_columnconfigure(2, weight=1)  # Para el botón "Optimizar"

        # Botones
        self.boton_cargar = tk.Button(ventana, text="Cargar Texto", command=self.cargar_texto)
        self.boton_cargar.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.boton_compilar = tk.Button(ventana, text="Compilar", command=self.compilar)
        self.boton_compilar.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.boton_optimizar = tk.Button(ventana, text="Optimizar", command=self.optimizar)
        self.boton_optimizar.grid(row=0, column=2, padx=10, pady=10, sticky='n')



        # Área de texto
        self.text_area = scrolledtext.ScrolledText(ventana, width=80, height=10)
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Área para tabla de símbolos
        self.area_simbolos = Tabla(ventana, titulo="Tabla de Símbolos")
        self.area_simbolos.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # Área para tabla de errores
        self.area_errores = Tabla(ventana, titulo="Tabla de Errores")
        self.area_errores.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        # Área para tabla de cuádruplos
        self.area_cuadruplos = tk.Label(ventana, text="Tabla de Cuádruplos", relief='ridge', width=80, height=10)
        self.area_cuadruplos.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')




    def cargar_texto(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'r') as f:
                texto = f.read()
                self.text_area.delete(1.0, tk.END)  # Limpiamos el contenido anterior
                self.text_area.insert(tk.END, texto)

    def compilar(self):
        # print(self.venta.getGeometry())
        pass
    

    def optimizar(self):
        # Función para optimizar el código
        new_window = Window(title="Optimización")
        pass

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    mi_ventana = Window(ventana_principal)
    ventana_principal.mainloop()
