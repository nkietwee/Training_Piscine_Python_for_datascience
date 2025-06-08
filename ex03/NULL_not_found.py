# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f'Nothing: None {type(object)}')
        return 0
    elif isinstance(object, float):
        print(f'Cheese: nan {type(object)}')
        return 0
    elif isinstance(object, bool):
        print(f'Fake: False {type(object)}')
        return 0
    elif isinstance(object, int):
        print(f'Zero: 0  {type(object)}')
        return 0
    elif isinstance(object, str):
        print(f'Empty: {type(object)}')
        return 0
    else:
        print('Type not Found')
        return 1
