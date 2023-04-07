import random


def generate_equations(num_equations, min_num, max_num, num_terms=2):
    """
    This function generates a specified number of arithmetic equations with random operands and operators.

    Parameters:
        - num_equations (int): the number of equations to generate
        - min_num (int): the minimum value for the operands
        - max_num (int): the maximum value for the operands
        - num_terms (int): the number of terms in each equation (default is 2)

    Returns:
        - equations (list): a list of randomly generated equations
    """
    equations = []
    operators = ["+", "-", "×", "÷"]

    for i in range(num_equations):
        equation = str(random.randint(min_num, max_num))

        for j in range(num_terms - 1):
            operator = random.choice(operators)
            operand = str(random.randint(min_num, max_num))
            equation += " {} {}".format(operator, operand)

        equations.append(equation)

    return equations
