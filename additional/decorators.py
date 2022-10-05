def response_to_approacher(name, approaching=True):
    def inner_response(func):
        def wrapper(*args, **kwargs):
            if approaching:
                print(f'A {name} is coming')
            else:
                print(f'A {name} is leaving')
            response = func(*args, **kwargs)
            return response

        return wrapper

    return inner_response


@response_to_approacher('Milkman', False)
def make_sound(sound):
    return (sound * 2)


returned_value = make_sound('woof')
print(returned_value)