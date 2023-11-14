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
