from functools import wraps
from typing import Any, Optional, Callable


def log(filename: Optional[str] = None) -> Any:
    """Декоратор логирует результаты выполнения функции
    - при успешном выполнении записывает "<name> OK
    - при любой ошибке пишет "<name> error: <exc>. Inputs <args>, <kwargs>"
    Логи записываются в файл, если указано название файла, в противном случае выводятся в консоль"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            try:
                func(*args, **kwargs)
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} OK")
                else:
                    print(f"{func.__name__} OK")
            except Exception as e:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            return func(*args, **kwargs)
        return wrapper

    return decorator
