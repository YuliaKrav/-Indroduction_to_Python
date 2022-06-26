# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

import operator

opening_parenthesis = "("

expression = "2 * (3 + 1) + 2 * 2="
expression = "10 / 2 - 7 + 2 * (3 + 2 + 5 - 1) / 3 ="
expression = "((5+   5) *(154-14))+8*(14+(19-13)) ="
OPERATORS = {'*': operator.mul, '/': operator.truediv,
             '+': operator.add, '-': operator.sub}
END_EXPRESSION = "="
OPEN_PARENTHESES = "("
CLOSE_PARENTHESES = ")"
OP_PLUS = '+'
OP_SUB = '-'
OP_MUL = '*'
OP_DIV = "/"


def delete_extra_spaces(string_original):
    return string_original.replace(" ", "")


def is_number(symbol):
    return "0" <= symbol <= "9"


def is_open_parentheses(symbol):
    return symbol == OPEN_PARENTHESES


def is_close_parentheses(symbol):
    return symbol == CLOSE_PARENTHESES


def is_math_operation(symbol):
    return symbol == OP_MUL or symbol == OP_DIV or symbol == OP_PLUS or symbol == OP_SUB


def get_number_string(expression_part_list):
    result_number_string = ""
    for i in range(len(expression_part_list)):
        if is_number(expression_part_list[i]):
            result_number_string += expression_part_list[i]
        else:
            return result_number_string


def priority_of_operation(symbol):
    if symbol == OP_MUL or symbol == OP_DIV:
        return 2
    if symbol == OP_PLUS or symbol == OP_SUB:
        return 1
    if symbol == OPEN_PARENTHESES:
        return 0


def evaluation_of_expression(expression_original):
    expression_list = list(delete_extra_spaces(expression_original))

    numbers_list = []
    operations_list = []

    def calculation_operation():
        number2 = numbers_list.pop()
        number1 = numbers_list.pop()
        return OPERATORS[operations_list.pop()](number1, number2)

    #print(OPERATORS['+']( 3, 4))
    current_position = 0
    while (expression_list[current_position] != END_EXPRESSION):
        if is_number(expression_list[current_position]):
            number_string = get_number_string(expression_list[current_position:])
            numbers_list.append(int(number_string))
            current_position += len(number_string) - 1

        elif is_open_parentheses(expression_list[current_position]):
            operations_list.append(expression_list[current_position])

        elif is_close_parentheses(expression_list[current_position]):
            while operations_list[-1] != OPEN_PARENTHESES:
                numbers_list.append(calculation_operation())
            else:
                operations_list.pop()
            
        elif is_math_operation(expression_list[current_position]):    
            current_operation = expression_list[current_position]
            current_priority = priority_of_operation(current_operation)

            while len(operations_list) > 0 and current_priority <= priority_of_operation(operations_list[-1]):
                numbers_list.append(calculation_operation())
            operations_list.append(current_operation)
        current_position += 1

    while len(operations_list) > 0:
        numbers_list.append(calculation_operation())

    return numbers_list[0]



print(f'{expression} {evaluation_of_expression(expression)}')
