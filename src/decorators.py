import os

def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename:
                with open(filename, "a") as file:
                    try: func(*args, **kwargs)
                    except ValueError as e:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                file.write(f'{func.__name__} OK')
            else:
                try: func(*args, **kwargs)
                except ValueError as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                print(f'{func.__name__} OK')
        return wrapper
    return decorator



