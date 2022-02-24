import datetime

import requests

def logger(log_path):

    def decorator(func):

        def foo(*args, **kwargs):
            date_time = datetime.datetime.now()
            func_name = func.__name__
            result = func(*args, **kwargs)

            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'Дата и время вызова функции: {date_time}\n'
                                     f'Имя функции: {func_name}\n'
                                     f'Аргументы функции: {args, kwargs}\n'
                                     f'Результат: {result}\n')
            return result

        return foo

    return decorator

@logger('file_logger_decorator')

def func(*args, **kwargs):

    url = ','.join(args)
    response = requests.get(url=url)

    if response.status_code != 200:
        print(f'- Ошибка в url')
    return response.status_code

if __name__ == '__main__':
    func('https://github.com/LyudmilaMos/Iter_gen_comments.git')