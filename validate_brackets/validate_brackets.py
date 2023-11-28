def is_open_bracket(ch):
    return ch in '({['


def brackets_match(open, close):
    return open == '(' and close == ')' or \
        open == '[' and close == ']' or \
        open == '{' and close == '}'


def is_close_bracket(ch):
    return ch in ')}]'


def validate_brackets(string):
    open_brackets = []

    for ch in string:
        if is_open_bracket(ch):
            open_brackets.append(ch)
        elif is_close_bracket(ch):
            if len(open_brackets) != 0:
                if brackets_match(open_brackets[-1], ch):
                    open_brackets.pop(-1)
                else:
                    return False
            else:
                return False
    if len(open_brackets) == 0:
        return True
    else:
        return False
