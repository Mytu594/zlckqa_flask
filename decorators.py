from flask import g,redirect,url_for
from functools import wraps


def login_required(func):
    # @wraps这个装饰器一定不要忘记写了
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,'user'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for("user.login"))

    return wrapper