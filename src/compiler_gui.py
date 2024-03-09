# /src/gui/compiler_gui.py
# import sys
# sys.path.append('/home/hugo/Documents/Tec/compiler/src/main_compiler.py')

import tkinter as tk
from tkinter import filedialog
from main_compiler import first_pass, second_pass
<<<<<<< HEAD
from symbol_table.symbol_table import SymbolTable
from error_table.error_table import ErrorTable
import csv

=======
import csv
>>>>>>> 9075cede4c03c7f348fc47074cd584fa20767f22

class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compileradar GUI")

        self.select_file_button = tk.Button(root, text="Seleccionar Archivo", command=self.select_file)
        self.select_file_button.pack(pady=10)

        self.compile_button = tk.Button(root, text="Compilar", command=self.compile)
        self.compile_button.pack(pady=10)

        self.file_path = None

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=[("Archivos de Texto", "*.txt")])
        if file_path:
            self.file_path = file_path
            print(f"Archivo seleccionado: {self.file_path}")

<<<<<<< HEAD
    def save_symbol_table_to_csv(self, symbol_table: SymbolTable, file_name):
        csv_data = []
        for lexema, tipo in symbol_table.get_table().items():
            csv_data.append({
                'Lexema': lexema,
                'Tipo': tipo
            })

        csv_file_path = f"{file_name}_symbol_table.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ['Lexema', 'Tipo']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(csv_data)

        print(f"Tabla de Símbolos guardada en {csv_file_path}")

    def save_error_table_to_csv(self, error_table: ErrorTable, file_name):
        
        csv_file_path = f"{file_name}_error_table.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ['Token de error', 'Línea', 'Lexema', 'Descripción']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(error_table.get_table())

        print(f"Tabla de Errores guardada en {csv_file_path}")

    
=======
    def save_tokens_to_csv(self, table:dict, type, file_name):
        csv_data = []
        if type == 'compiler':
            for token, token_type in table.items():
                csv_data.append({
                    'Token': token,
                    'Tipo': token_type
                })
        elif type == 'error':
            for error in table:
                csv_data.append({
                    'Token de error': error['Token de error'],
                    'Línea': error['Línea'],
                    'Lexema': error['Lexema'],
                    'Descripción': error['Descripción']
                })

        csv_file_path = f"{file_name}_{type}.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            if csv_data:  
                fieldnames = csv_data[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(csv_data)

        print(f"Tokens guardados en {csv_file_path}")
>>>>>>> 9075cede4c03c7f348fc47074cd584fa20767f22

    def compile(self):
        if self.file_path:
            with open(self.file_path, "r") as file:
                source_code = [line.split() for line in file.readlines()]

            symbol_table = first_pass(source_code)
<<<<<<< HEAD
            self.save_symbol_table_to_csv(symbol_table, file_name=self.file_path)

            error_table = second_pass(source_code, symbol_table.get_table())
            self.save_error_table_to_csv(error_table, file_name=self.file_path)
            # Aquí puedes hacer algo con las tablas generadas
            # print("Tabla de Símbolos:", symbol_table.symbol_table)
            # print("Tabla de Errores:", error_table.error_table)
        else:
=======
            self.save_tokens_to_csv(table=symbol_table,type='compiler',file_name=self.file_path)
            error_table = second_pass(source_code = source_code, symbol_table = symbol_table)
            
            self.save_tokens_to_csv(table=error_table,type='error',file_name=self.file_path)
           
>>>>>>> 9075cede4c03c7f348fc47074cd584fa20767f22
            print("Por favor, selecciona un archivo antes de compilar")

def main():
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
