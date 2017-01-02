# utility functions for repeated use across other base classes

def list_type_check(check_object_list, check_class, error=False):
    """Utility function checks that all items in a list are a defined type
    """
    type_check = all([
        isinstance(obj, check_class) for obj in check_object_list
    ])
    if type_check:
        return True
    elif error:
        type_name = check_class.__name__
        message_base = "Expect list to only contain {} objects"
        error_message = message_base.format(type_name)
        raise TypeError(error_message)
    else:
        return False

