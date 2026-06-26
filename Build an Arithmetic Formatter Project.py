def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    linea1 = []
    linea2 = []
    linea_guiones = []
    linea_respuestas = []

    for problems in problems:
        operations = problems.split()
        op1, operador, op2 = operations[0], operations[1], operations[2]

        if operador not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (op1.isdigit() and op2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        ancho = max(len(op1), len(op2)) + 2

        linea1.append(op1.rjust(ancho))
        linea2.append(operador + op2.rjust(ancho - 1))
        linea_guiones.append("-" * ancho)

        if show_answers:
            resultado = str(int(op1) + int(op2) if operador == '+' else int(op1) - int(op2))
            linea_respuestas.append(resultado.rjust(ancho))

    resultado_final = (
        "    ".join(linea1) + "\n" +
        "    ".join(linea2) + "\n" +
        "    ".join(linea_guiones)
    )

    if show_answers:
        resultado_final += "\n" + "    ".join(linea_respuestas)

    return resultado_final

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
