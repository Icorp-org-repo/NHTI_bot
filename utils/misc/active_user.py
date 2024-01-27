def ban_user(key=None):
    """
    Decorator for configuring rate limit and key in different function.
    :param limit:
    :param key:
    :return:
    """
    def decorator(func):
        if key:
            setattr(func, 'throttling_key', key)
        return func
    return decorator
