# /src/error_table/error_table.py
from symbol_table.lexer  import ope_re, eq_re
class ErrorTable:
    def __init__(self,source_code: list[list[str]],symbol_table: dict[str,str]):
        self.source_code = source_code
        self.symbol_table = symbol_table
        # self.error_table = dict(str,tuple(int,str,str))
        self.check_operation()

    def add_error(self, line, lex, messag):
        # Lógica para agregar un error a la tabla
        print(f"Adding error at line {line}, lex {lex}: {messag}")
        pass
    def check_operation(self):
        num_line = 0
        for line in self.source_code:
            num_line +=1
            # print(line)
            if line.count('=') > 0 and (line.count('+') >0 or line.count('-') > 0 or line.count('/') > 0) :
                # for lex in line:
                    # print(lex)
                self.check_error(line,num_line)

    def check_error(self,line:list[str],num_line:int):
        print(line)
        index_eq = line.index('=')
        index_op = line.index('+') if line.count('+') > 0 else line.index('-') if line.count('-') > 0 else line.index('/') if line.count('/') > 0 else -1
        token_result=line[index_eq-1]
        token_left=line[index_eq+1:index_op][0]
        token_right=line[index_op+1:-1][0]
        result= self.symbol_table.get(token_result)
        left = self.symbol_table.get(token_left)
        right = self.symbol_table.get(token_right)
        # print(f'{line[index_eq-1]}')
        # print(f'{line[index_eq+1:index_op]}')
        # print(f'{line[index_op+1:-1]}')

        # str
        if result == 'palabra' and (left != 'palabra' or right != 'palabra'):
            erro_token = token_left if left != 'palabra' else token_right
            self.add_error(num_line,erro_token,'Error de tipo incompatiblidad de palabra')
        # int
        if result == 'numero' and (left != 'numero' or right != 'numero'):
            erro_token = token_left if left != 'numero' else token_right
            # print(f'{line[index_eq-1]} : {result} {str(line[index_eq+1:index_op])} : {left} {str(line[index_op+1:-1])} : {right}')
            # print(erro_token)
            self.add_error(num_line,erro_token,'Error de tipo incompatiblidad de numero')
        # float
        if result == 'decimal' and (left != 'decimal' or right != 'decimal'):
            erro_token = token_left if left != 'decimal' else token_right
            self.add_error(num_line,erro_token,'Error de tipo incompatiblidad de decimal')

    def get_table(self):
        return self.error_table