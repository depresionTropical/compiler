# /src/main_compiler.py
from lexer.lexer import tokenize
from symbol_table.symbol_table import SymbolTable
from error_table.error_table import ErrorTable

def first_pass(source_code: list[str], symbol_table=SymbolTable()):
    tokens = tokenize(source_code)
    print(tokens)
    return tokens

def second_pass(source_code, symbol_table, error_table=dict):
    for line_num, line in enumerate(source_code, start=1):
        for column_num, symbol in enumerate(line, start=1):
            if symbol in symbol_table:
                symbol_type = symbol_table[symbol]

                
                error_table[line_num]= {column_num, symbol, symbol_type, symbol_type}

    print("Tabla de Errores:")
    for error in error_table.error_table:
        print(error)

    return error_table


def main():
    with open("codigo_fuente.txt", "r") as file:
        source_code = file.read()

    symbol_table = SymbolTable()
    error_table = ErrorTable()

    first_pass(source_code, symbol_table)

    second_pass(source_code, error_table)

if __name__ == "__main__":
    main()
