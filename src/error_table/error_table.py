# /src/error_table/error_table.py
from symbol_table.lexer  import ope_re, eq_re
class ErrorTable:
    def __init__(self,source_code: list[list[str]],symbol_table: dict[str,str]):
        self.source_code = source_code
        self.symbol_table = symbol_table
        self.error_table = dict(str,tuple(int,str,str))
        self.check_errors()

    def add_error(self, line, column, message):
        # Lógica para agregar un error a la tabla
        print(f"Adding error at line {line}, column {column}: {message}")
        pass
    def check_errors(self):
        num_line = 1
        for line in self.source_code:
            num_column +=1
            if line.count('=') > 1 and (line.count('+') > 1 or line.count('-') > 1 or line.count('/') > 1) :
                self.add_error(num_line,num_column,'Multiple assignment')


    def get_table(self):
        return self.error_table