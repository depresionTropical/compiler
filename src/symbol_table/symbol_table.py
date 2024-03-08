# /src/symbol_table/symbol_table.py
import pandas as pd
from lexer.lexer import match_token


class SymbolTable:
    def __init__(self, table: list[list[str]]):
        self.table_df = pd.DataFrame()
        self.table_list = table
        self.token_list = dict()
        self.tokenizer()

    def add_symbol(self, name, value):
        # Lógica para agregar un símbolo a la tabla
        print(f"Adding symbol {name} with value {value} to the symbol table")
        pass

    def tokenizer(self):
        for line in range(len(self.table_list)):
            # print(line)
            for word in range(len(self.table_list[line])):
                type_word = match_token(self.table_list[line][word])
                if word == 0 and (type_word == 'palabra' or type_word == 'numero' or type_word == 'decimal'):
                    print(f'{self.table_list[line][word]} : {type_word}')

        pass


if __name__ == "__main__":
    source_code = [
        ["numero", "_A1", "=", "_A2", "+", "_A3", ";"],
        ["palabra", "_Bueno1", ";"],
        ["palabra", "_Malo1", ";"],
        ["decimal", "_NumeroDecimal1", ";"],
        ["palabra", "_oracion1", "=", "_Bueno1", "+", "_Malo1", ";"],
        ["_A2", "=", "_A1", "-", "_A3", ";"],
        ["decimal", "_A4", "=", "_A3", "/", "_A3", ";"],
        ["palabra", "_oracion2", "=", "_Malo1", "+", "_Bueno1", ";"],
    ]

    symbol_table = SymbolTable(source_code)
    # print('Tokens: ')
    # print(symbol_table.table_list)
