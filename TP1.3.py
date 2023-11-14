def evaluate_expression(expr):
    elements = []
    current_number = ''
    for char in expr:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                elements.append(current_number)
                current_number = ''
            if char != ' ':
                elements.append(char)
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