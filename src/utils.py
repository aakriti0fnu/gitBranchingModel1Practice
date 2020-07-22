import time
import argparse
from datetime import datetime, timezone

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
