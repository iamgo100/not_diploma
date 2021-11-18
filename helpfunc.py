from books import select_column

def checking_select(req, name):
    param = req[f'{name}-input']
    if not param:
        param = req[f'{name}-select']
    if 'Выберите' in param:
        param = ''
    return param

def add_options(options, con, cur, col):
    optinsList = list(set(select_column(con, cur, col)))
    for option in optinsList:
        options.append(option[0])