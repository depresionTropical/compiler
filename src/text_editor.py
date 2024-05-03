import tkinter as tk
from tkinter import ttk
import csv
from cuadruplo.Cuadruplo import expresion_a_cuadruplos

class VisorTexto:
    def __init__(self, ventana_padre, file_path):
        self.ventana_padre = ventana_padre
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Visor de texto")

        # Crear el área de texto
        self.texto = tk.Text(self.ventana, state='normal')
        self.texto.pack(expand=True, fill="both",)

        # Crear un widget Treeview para mostrar los datos de la expresión
        self.tabla_expresion = ttk.Treeview(self.ventana)
        self.tabla_expresion["columns"] = ("#1", "#2", "#3","#4")  # Definir tres columnas
        self.tabla_expresion.heading("#0", text="Índice")  # Encabezado de la columna índice
        self.tabla_expresion.heading("#1", text="Operador")  # Encabezado de la columna operador
        self.tabla_expresion.heading("#2", text="Resultado")  # Encabezado de la columna operador
        self.tabla_expresion.heading("#3", text="Dato Fuente 1")  # Encabezado de la columna dato objeto
        self.tabla_expresion.heading("#4", text="Dato Fuente 2")  # Encabezado de la columna dato fuente
        self.tabla_expresion.pack()

        # Agregar eventos para resaltar la línea actual y moverse con las flechas
        self.ventana.bind("<Motion>", self.resaltar_linea)
        self.ventana.bind("<Up>", self.mover_arriba)
        self.ventana.bind("<Down>", self.mover_abajo)

        # Agregar evento para mostrar contenido seleccionado al presionar F4
        self.ventana.bind("<F4>", self.on_f4)

        # Cargar el contenido del archivo al iniciar la aplicación
        self.cargar_archivo(file_path)
        # Mostrar las tablas adicionales si existen
        self.mostrar_tablas_adicionales(file_path)

    def cargar_archivo(self, ruta):
        try:
            with open(ruta, "r") as archivo:
                contenido = archivo.read()
                self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
                self.texto.insert(tk.END, contenido)  # Insertar el nuevo contenido
                # Después de cargar el contenido del archivo, establecer el área de texto como de solo lectura
        except FileNotFoundError:
            self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
            self.texto.insert(tk.END, "El archivo no se encontró.")
        except Exception as e:
            self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
            self.texto.insert(tk.END, f"Error al cargar el archivo: {str(e)}")

    # def mostrar_contenido_seleccionado(self):
    #     # Obtener la línea seleccionada
    #     linea_seleccionada = int(self.texto.index(tk.INSERT).split(".")[0])
    #     # Obtener el contenido de la línea seleccionada
    #     contenido_seleccionado = self.texto.get(f"{linea_seleccionada}.0", f"{linea_seleccionada + 1}.0")
    #     # Actualizar el contenido en el widget Label
    #     self.contenido_label.config(text=f"Línea {linea_seleccionada}: {contenido_seleccionado.strip()}")
        

    def resaltar_linea(self, event=None):
        # Desmarcar todas las líneas
        self.texto.tag_remove("resaltado", "1.0", "end")
        # Obtener la línea seleccionada
        linea = int(self.texto.index(tk.INSERT).split(".")[0])
        # Resaltar la línea
        self.texto.tag_add("resaltado", f"{linea}.0", f"{linea + 1}.0")
        self.texto.tag_config("resaltado", background="yellow")

    def on_f4(self, event=None):
        # Obtener la línea seleccionada
        linea_seleccionada = int(self.texto.index(tk.INSERT).split(".")[0])
        # Obtener el contenido de la línea seleccionada
        contenido_seleccionado = self.texto.get(f"{linea_seleccionada}.0", f"{linea_seleccionada + 1}.0")
        expresion = expresion_a_cuadruplos(contenido_seleccionado)

        # Limpiar la tabla antes de agregar los nuevos datos
        self.tabla_expresion.delete(*self.tabla_expresion.get_children())

        # Agregar los elementos de la expresión a la tabla
        for idx, cuadruplo in enumerate(expresion, start=1):
            self.tabla_expresion.insert("", tk.END, text=f"{idx}", values=(cuadruplo.operador, cuadruplo.resultado, cuadruplo.fuente1, cuadruplo.fuente2))

        
        
        print(expresion)
    def mover_arriba(self, event):
        # Obtener la línea actual
        linea, columna = map(int, self.texto.index(tk.INSERT).split('.'))
        # Mover hacia arriba si no estamos en la primera línea
        if linea > 1:
            nueva_linea = linea - 1
            self.texto.mark_set(tk.INSERT, f"{nueva_linea}.{columna}")
            self.resaltar_linea()

    def mover_abajo(self, event):
        # Obtener la línea actual
        linea, columna = map(int, self.texto.index(tk.INSERT).split('.'))
        # Mover hacia abajo si no estamos en la última línea
        if linea < int(self.texto.index('end-1c').split('.')[0]):
            nueva_linea = linea + 1
            self.texto.mark_set(tk.INSERT, f"{nueva_linea}.{columna}")
            self.resaltar_linea()
    def cargar_archivo(self, ruta):
        try:
            with open(ruta, "r") as archivo:
                contenido = archivo.read()
                self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
                self.texto.insert(tk.END, contenido)  # Insertar el nuevo contenido
        except FileNotFoundError:
            self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
            self.texto.insert(tk.END, "El archivo no se encontró.")
        except Exception as e:
            self.texto.delete("1.0", tk.END)  # Limpiar el contenido anterior
            self.texto.insert(tk.END, f"Error al cargar el archivo: {str(e)}")

    def mostrar_tablas_adicionales(self, file_path):
        prefix = "/home/hugo/Documents/Tec/compiler/example/"
        file_name = file_path.split("/")[-1].split(".")[0]

        symbol_table_file = f"{prefix}{file_name}.txt_symbol_table.csv"
        error_table_file = f"{prefix}{file_name}.txt_error_table.csv"
        print(symbol_table_file, error_table_file)
        try:
            symbol_table_data = self.cargar_csv(symbol_table_file)
            if symbol_table_data:
                self.mostrar_tabla("Tabla de Símbolos", symbol_table_data)

            error_table_data = self.cargar_csv(error_table_file)
            if error_table_data:
                self.mostrar_tabla("Tabla de Errores", error_table_data)
        except FileNotFoundError:
            print("No se encontraron archivos de tablas adicionales.")

    def cargar_csv(self, file_path):
        data = []
        with open(file_path, "r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
        return data

    def mostrar_tabla(self, title, data):
        # Crear una nueva ventana secundaria para mostrar la tabla
        ventana_tabla = tk.Toplevel(self.ventana)
        ventana_tabla.title(title)

        # Crear un frame para la tabla
        tabla_frame = tk.Frame(ventana_tabla)
        tabla_frame.pack(fill="both", expand=True)

        # Crear la tabla con un Treeview
        tabla = ttk.Treeview(tabla_frame)
        tabla.pack(fill="both", expand=True)

        # Obtener las cabeceras de las columnas desde la primera fila de datos
        cabeceras = data[0]
        data_sin_cabeceras = data[1:]  # Excluir la primera fila de datos (cabeceras)

        # Configurar las columnas
        if cabeceras:
            tabla["columns"] = cabeceras
            for columna in cabeceras:
                tabla.heading(columna, text=columna)

        # Insertar los datos en la tabla (excluyendo las cabeceras)
        for row in data_sin_cabeceras:
            tabla.insert("", "end", values=row)





if __name__ == "__main__":
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")

    # Crear un botón para abrir otra ventana
    boton_otra_ventana = tk.Button(ventana_principal, text="Abrir Otra Ventana", command=lambda: OtraVentana(ventana_principal))
    boton_otra_ventana.pack()

    # Ejecutar la ventana principal
    ventana_principal.mainloop()
