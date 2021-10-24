def func(n):
    string_value = str(n).lstrip().lower()

    if not string_value:
        return [n, 'empty string']

    if string_value in ['true']:
        return [n, 1]
    if string_value in ['false']:
        return [n, 'not positive']

    float_value = float(n)

    if float_value <= 0:
        return [n, 'not positive']

    if string_value == str(float_value):
        return [n, 'not integer']

    return [n, len(string_value.lstrip('0'))]


print(
    func(''), func(' '),
    '',
    func(True), func('True'),
    func(False), func('False'),
    '',
    func(0), func('0'),
    func(1), func('1'),
    func(0.0), func('0.0'),
    func(1.0), func('1.0'),
    '',
    func(42), func('42'),
    func(42.0), func('42.0'),
    func(42.1), func('42.1'),
    '',
    func(-42), func('-42'),
    func(-42.0), func('-42.0'),
    func(-42.1), func('-42.1'),
    '',
    func('001'),
    # func('000.1'),  # idk
    sep='\n'
)
