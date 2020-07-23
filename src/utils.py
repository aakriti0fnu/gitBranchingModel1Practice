import time
import argparse
from datetime import datetime, timezone
import functools

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = time.strftime("%H:%M:%S" , time.gmtime((te - ts)))
        else:
            # print('%r took  %2.2f ms' % \
            #       (method.__name__, (te - ts) * 1000))
            print("{} took {}.".format(method.__name__,time.strftime("%H:%M:%S" , time.gmtime((te - ts))) ))
        return result
    return timed

def current_local_datetime():
    return datetime.now()

def current_UTC_datetime():
    return datetime.now(timezone.utc)

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected. ['yes', 'true', 't', 'y', '1', 'no', 'false', 'f', 'n', '0']" )

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
