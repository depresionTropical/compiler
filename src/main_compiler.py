# /src/main_compiler.py

from symbol_table.symbol_table import SymbolTable
from error_table.error_table import ErrorTable

def first_pass(source_code: list[str]):
    # Realizar la primera pasada para construir la tabla de símbolos
    symbol_table = SymbolTable(source_code)
    
    return symbol_table
def second_pass(source_code: list[list[str]],symbol_table: dict[str,str]):
    error_table = ErrorTable()
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
