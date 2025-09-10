def _init():  # pragma: no cover
    try:
        if is_initialized():
            return
        else:
            raise NameError
    except NameError:
        global _global_dict
        _global_dict = {}


def is_initialized():
    try:
        _ = _global_dict
        return True
    except NameError:
        return False


def set_value(key, value):
    try:
        _global_dict[key] = value
    except NameError:
        _init()
        set_value(key, value)


def get_value(key, default_value=None):
    try:
        return _global_dict[key]
    except KeyError:
        return default_value
    except NameError:
        _init()
        return get_value(key, default_value)


def items() -> dict:
    return _global_dict


def get_sys_value(key, __default=None):
    return get_value("rb_system_json", {}).get(key)
