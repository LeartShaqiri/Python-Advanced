from typing import Optional, Any, List, Union

def get_name(name: Optional [str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print (get_name())


from typing import Union

def get_age(age: Union[int, str]) -> Union[int, str]:
    if isinstance(age, int):
        return age
    elif isinstance(age, str):
        return "Please enter a number, not text."



def get_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value} "

    print(get_value(1))


def get_data(data: Any) :
    return data

print(get_data("hihi")) 


def get_go(go:List[int]) -> int:
    return sum (go )

print(get_go([1,2,3]))
