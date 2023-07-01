from common.observations import observations
from common.exceptions import InvalidObserverException
from inspect import signature


def observer(url):
    """
    :param url: the target URL of the observer function
    :return: a decorator for the observer
    """
    def decorator(func):
        """
        :param func: function f: html -> dict for which we wish to add to the observations
        :return: a wrapper for the function that appends it to observations
        """
        f_sig = signature(func)
        f_name = func.__name__
        f_params = f_sig.parameters
        fp_len = len(f_params)
        if fp_len != 1:
            raise InvalidObserverException(f"Invalid parameter count at observer'{f_name}'."
                                           f"Expected 1 argument, got {fp_len}.")
        f_data = {
            "f_name": f_name,
            "f_ref": func,
            "url": url
        }
        observations.append(f_data)
        return func

    return decorator
