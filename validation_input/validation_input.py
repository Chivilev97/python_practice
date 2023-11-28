import string


def validate_name(name):
    return len(name) >= 2


def validate_zip(zip_code):
    for c in zip_code:
        if c not in '1234567890':
            return False
    return zip_code != ''


def validate_id(employee_id):
    if len(employee_id) != 7 or \
            employee_id[0] not in string.ascii_uppercase or \
            employee_id[1] not in string.ascii_uppercase or \
            employee_id[2] != '-':
        return False
    for c in employee_id[3:]:
        if c not in string.digits:
            return False
    return True


def validate_input(name, last_name, zip_code, employee_id):
    return {'name': validate_name(name),
            'last_name': validate_name(last_name),
            'zip_code': validate_zip(zip_code),
            'employee_id': validate_id(employee_id)}


def print_validation_result(result):
    errors = []

    if not result['name']:
        errors.append(f'"{name}" не валидное имя. Слишком короткое')
    if not result['last_name']:
        errors.append(f'"{last_name}" не валидная фамилия. Слишком короткая')
    if not result['zip_code']:
        errors.append('Этот индекс должен быть числом')
    if not result['employee_id']:
        errors.append(f'"{employee_id}" не валидный код сотрудника')
    if len(errors) == 0:
        print('Ошибок не найдено')
    else:
        print('\n'.join(errors))


if __name__ == '__main__':
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    zip_code = input('Введите индекс: ')
    employee_id = input('Введите код сотрудника: ')
    result = validate_input(name, last_name, zip_code, employee_id)
    print_validation_result(result)
