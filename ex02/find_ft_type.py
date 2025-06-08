""""
Write a function that prints the object types and returns 42.

Why Type Hints Don’t Prevent Errors
Type hints are not enforced by the Python interpreter;
they are purely for static analysis by external tools like mypy.
    So, even with type hints, the code will still run with errors
unless a static type checker is used. Python won’t prevent you
from passing a string or floating-point number to the function at runtime.

ref
Type Hints in Python : https://www.geeksforgeeks.org/type-hints-in-python/
type and isinstance in Python : https://www.geeksforgeeks.org/type-isinstance-python/
"""


def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f'List : {type(object)}')
    elif isinstance(object, tuple):
        print(f'Tuple : {type(object)}')
    elif isinstance(object, set):
        print(f'Set : {type(object)}')
    elif isinstance(object, dict):
        print(f'Dict : {type(object)}')
    elif isinstance(object, str):
        print(f'Brian is in the kitchen : {type(object)}')
    else:
        print('Type not found')
    # print(object)
    return 42

