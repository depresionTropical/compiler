import tkinter as tk

def cargar_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            contenido = archivo.read()
            texto.insert("1.0", contenido)
    except FileNotFoundError:
        texto.insert("1.0", "El archivo no se encontró.")
    except Exception as e:
        texto.insert("1.0", f"Error al cargar el archivo: {str(e)}")
    # Deshabilitar el área de texto después de cargar el archivo
    texto.config(state="disabled")

def mostrar_contenido_seleccionado():
    # Obtener la línea seleccionada
    linea_seleccionada = int(texto.index(tk.INSERT).split(".")[0])
    # Obtener el contenido de la línea seleccionada
    contenido_seleccionado = texto.get(f"{linea_seleccionada}.0", f"{linea_seleccionada + 1}.0")
    # Crear y mostrar la nueva ventana con la información
    ventana_contenido_seleccionado = tk.Toplevel(ventana)
    ventana_contenido_seleccionado.title("Contenido Seleccionado")
    etiqueta_linea = tk.Label(ventana_contenido_seleccionado, text=f"Seleccionaste la fila número {linea_seleccionada}")
    etiqueta_linea.pack()
    etiqueta_contenido = tk.Label(ventana_contenido_seleccionado, text=f"Contenido: {contenido_seleccionado}")
    etiqueta_contenido.pack()

def resaltar_linea(event=None):
    # Desmarcar todas las líneas
    texto.tag_remove("resaltado", "1.0", "end")
    # Obtener la línea seleccionada
    linea = int(texto.index(tk.INSERT).split(".")[0])
    # Resaltar la línea
    texto.tag_add("resaltado", f"{linea}.0", f"{linea + 1}.0")
    texto.tag_config("resaltado", background="yellow")

def mover_arriba(event):
    # Obtener la línea actual
    linea, columna = map(int, texto.index(tk.INSERT).split('.'))
    # Mover hacia arriba si no estamos en la primera línea
    if linea > 1:
        # Desvincular eventos de flechas temporalmente
        ventana.unbind("<Up>")
        ventana.unbind("<Down>")
        nueva_linea = linea - 1
        texto.mark_set(tk.INSERT, f"{nueva_linea}.{columna}")
        resaltar_linea()
        # Volver a vincular eventos de flechas
        ventana.bind("<Up>", mover_arriba)
        ventana.bind("<Down>", mover_abajo)

def mover_abajo(event):
    # Obtener la línea actual
    linea, columna = map(int, texto.index(tk.INSERT).split('.'))
    # Mover hacia abajo si no estamos en la última línea
    if linea < int(texto.index('end-1c').split('.')[0]):
        # Desvincular eventos de flechas temporalmente
        ventana.unbind("<Up>")
        ventana.unbind("<Down>")
        nueva_linea = linea + 1
        texto.mark_set(tk.INSERT, f"{nueva_linea}.{columna}")
        resaltar_linea()
        # Volver a vincular eventos de flechas
        ventana.bind("<Up>", mover_arriba)
        ventana.bind("<Down>", mover_abajo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Visor de texto")

# Crear el área de texto y cargar el archivo
texto = tk.Text(ventana)
texto.pack(expand=True, fill="both")
cargar_archivo("src/main.txt")  

# Agregar evento para resaltar la línea actual
ventana.bind("<Motion>", resaltar_linea)

# Agregar eventos para moverse con las flechas
ventana.bind("<Up>", mover_arriba)
ventana.bind("<Down>", mover_abajo)

# Agregar evento para mostrar contenido seleccionado al presionar F4
ventana.bind("<F4>", lambda event: mostrar_contenido_seleccionado())

# Ejecutar la ventana principal
ventana.mainloop()
