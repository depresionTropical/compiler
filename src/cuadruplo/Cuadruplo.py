from symbol_table.lexer import identifier
import re
class Cuadruplo:
    def __init__(self, operador, resultado, fuente1, fuente2):
        self.operador = operador
        self.resultado = resultado
        self.fuente1 = fuente1
        self.fuente2 = fuente2
    def __repr__(self) -> identifier:
        return f"{self.operador} {self.resultado} {self.fuente1} {self.fuente2}"
        pass


def expresion_a_cuadruplos(expresion):
    cuadruplos = []
    temp_count = 1

    # Función auxiliar para generar un nombre temporal único
    def generar_temp():
        nonlocal temp_count
        temp_name = f'T{temp_count}'
        temp_count += 1
        return temp_name

    # Separar la expresión en la variable de destino y la expresión misma
    variable_destino, expresion = expresion.split("=")
    variable_destino = variable_destino.strip()
    variable_destino =
    # Convertir la expresión en una lista de tokens
    tokens = expresion.split()
    print(f'tokens: {variable_destino}')
    pila_operandos = []
    pila_operadores = []

    for token in tokens:
        if token.isdigit() or token.isalpha() or re.match(identifier, token):
            pila_operandos.append(token)
        elif token in '+-*/':
            # Operadores de alta prioridad (*, /)
            if token in '*/':
                pila_operadores.append(token)
            # Operadores de baja prioridad (+, -)
            else:
                while pila_operadores and pila_operadores[-1] in '*/':
                    operador = pila_operadores.pop()
                    fuente2 = pila_operandos.pop()
                    fuente1 = pila_operandos.pop()
                    resultado = generar_temp()
                    cuadruplo = Cuadruplo(
                        operador, resultado, fuente1, fuente2)
                    pila_operandos.append(resultado)
                    cuadruplos.append(cuadruplo)
                pila_operadores.append(token)

    # Procesar los operadores restantes
    while pila_operadores:
        operador = pila_operadores.pop()
        fuente2 = pila_operandos.pop()
        fuente1 = pila_operandos.pop()
        resultado = generar_temp()
        cuadruplo = Cuadruplo(operador, resultado, fuente1, fuente2)
        pila_operandos.append(resultado)
        cuadruplos.append(cuadruplo)

    # Agregar un cuádruplo final para asignar el resultado a la variable de destino
    cuadruplo_asignacion = Cuadruplo(
        "=", variable_destino, pila_operandos.pop(), "")
    cuadruplos.append(cuadruplo_asignacion)

    return cuadruplos


# # Ejemplo de uso
# expresion = "z = a + b * c - d / f + a * b"
# print(f"Expresión: {expresion}")
# cuadruplos = expresion_a_cuadruplos(expresion)
# for cuadruplo in cuadruplos:
#     print(cuadruplo.operador, cuadruplo.resultado,
#           cuadruplo.fuente1, cuadruplo.fuente2)
