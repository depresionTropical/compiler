# /src/symbol_table/symbol_table.py

from symbol_table.lexer import match_token


class SymbolTable:
    def __init__(self, table: list[list[str]]):
        self.table_list = table
        self.token_dict= dict()
        self.tokenizer()

    def add_symbol(self, token:str, data_type:str):
        # Lógica para agregar un símbolo a la tabla
        # print(f"{token} : {data_type}")
        if not token in  self.token_dict.keys():
            # print(f"{token} : {data_type}: ")
            self.token_dict[token]=data_type
        

    def tokenizer(self):
        for line in range(len(self.table_list)):
            # print(line)
            data_type = None
            for word in range(len(self.table_list[line])):
                type_word = match_token(self.table_list[line][word])
                if word == 0 and ( type_word !=  '' ):
                    data_type = type_word
                    self.add_symbol(self.table_list[line][word],'')
                    continue
                if (data_type !=  None) and type_word == 'identifier':
                    self.add_symbol(self.table_list[line][word], data_type)
                if not type_word is None:
                    self.add_symbol(self.table_list[line][word],type_word)
                else:
                    self.add_symbol(self.table_list[line][word],'')

    def get_table(self):
        return self.token_dict
if __name__ == "__main__":
    source_code = [
        ["numero", "_A1", "=", "3", "+", "_A3", ";"],
        ["palabra", "_Bueno1", ";"],
        ["palabra", "_Malo1", ";"],
        ["decimal", "_NumeroDecimal1", ";"],
        ["palabra", "_oracion1", "=", "_Bueno1", "+", "_Malo1", ";"],
        ["_A2", "=", "_A1", "-", "_A3", ";"],
        ["decimal", "_A4", "=", "_A3", "/", "_A3", ";"],
        ["palabra", "_oracion2", "=", "_Malo1", "+", "_Bueno1", ";"],
    ]

    symbol_table = SymbolTable(source_code)
    print(symbol_table.token_dict)
    # print('Tokens: ')
    # print(symbol_table.table_list)
