from functools import wraps

def log(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f'{func.__name__} OK')
                else:
                    print(f'{func.__name__} OK')
            except Exception as e:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                else:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
        return wrapper
    return decorator

# if __name__ == "__main__":
#     @log(filename="mylog.txt")
#     def my_function(x, y):
#         return x + y
#
#
#     my_function("f", 2)