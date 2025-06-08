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
"""


def all_thing_is_obj(object: any) -> int:
    print(object)
    return 42


# from find_ft_type import all_thing_is_obj
# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))

