def evaluate_expression(expr):
    elements = []
    current_number = ''
    for char in expr:
        if char.isdigit():
            current_number += char
        elif char in ('+', '-', '*', '/'):
            if current_number:
                elements.append(current_number)
                current_number = ''
            elements.append(char)
        elif char != ' ':
            return f"Caractère non valide : '{char}'"
    if current_number:
        elements.append(current_number)

    i = 0
    while i < len(elements):
        
        if elements[i] in ('*', '/'):
            operator = elements[i]
            left_operand = float(elements[i - 1])
            right_operand = float(elements[i + 1])

            if operator == '*':
                elements[i - 1:i + 2] = [str(left_operand * right_operand)]
            else:
                if right_operand != 0:
                    elements[i - 1:i + 2] = [str(left_operand / right_operand)]
                else:
                    return "Division par zéro impossible"
        else:
            i += 1
            
    result = float(elements[0])
    i = 1
    while i < len(elements):
        operator = elements[i]
        operand = float(elements[i + 1])

        if operator == '+':
            result += operand
        else:
            result -= operand
        i += 2

    return result


operation = input("Entrez une expression mathématique (ex. 11+48-69*5) : ")
resultat = evaluate_expression(operation)
print(f"Résultat : {resultat}")

