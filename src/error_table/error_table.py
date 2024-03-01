# /src/error_table/error_table.py

class ErrorTable:
    def __init__(self):
        self.error_table = []

    def add_error(self, line, column, message):
        # Lógica para agregar un error a la tabla
        print(f"Adding error at line {line}, column {column}: {message}")
        pass

    # Otras funciones relacionadas con la tabla de errores
