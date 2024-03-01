# /src/main_compiler.py
from lexer.lexer import tokenize
from symbol_table.symbol_table import SymbolTable
from error_table.error_table import ErrorTable

def first_pass(source_code, symbol_table):
    # Realizar la primera pasada para construir la tabla de símbolos
    tokens = tokenize(source_code)
    for token in tokens:
        symbol_table.add_symbol(token.name, token.value)

def second_pass(source_code, error_table):
    # Realizar la segunda pasada para construir la tabla de errores
    # Implementar la lógica según los requerimientos específicos
    pass

def main():
    # Leer el código fuente desde un archivo u otra fuente
    with open("codigo_fuente.txt", "r") as file:
        source_code = file.read()

    # Inicializar la tabla de símbolos y la tabla de errores
    symbol_table = SymbolTable()
    error_table = ErrorTable()

    # Realizar la primera pasada
    first_pass(source_code, symbol_table)

    # Realizar la segunda pasada
    second_pass(source_code, error_table)

if __name__ == "__main__":
    main()
