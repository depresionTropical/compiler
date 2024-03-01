# /src/error_table/error_table.py

class ErrorTable:
    def __init__(self):
        self.error_table = []

    def add_error(self, line, column, symbol, expected_type, found_type):

        error_entry = {
            "Token de error": symbol,
            "Línea": line,
            "Lexema": symbol,
            "Descripción": f"Tipo incorrecto. Se esperaba {expected_type} pero se encontró {found_type}."
        }
        self.error_table.append(error_entry)

