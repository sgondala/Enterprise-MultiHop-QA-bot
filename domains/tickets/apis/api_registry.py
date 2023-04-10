TICKET_FUNCTION_REGISTRY = {}


# Decorator to register functions
def register_ticket_api(func):
    TICKET_FUNCTION_REGISTRY[func.__name__] = {
        "function": func,
        "docstring": func.__doc__,
    }
    return func
