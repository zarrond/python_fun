def dict_print(*args, **kwargs):
    print()
    options = {
        'str': '__'
    }
    options.update(kwargs)
    _str = options['str']
    if len(_str) == 0:
        print([x for x in args[0]])
    else:
        print([x for x in args[0] if _str not in x])


def dprint(*args, **kwargs):
    print()
    options = {
            'type': True,
            'dir': False,
            'value': True,
            'line': True,
            'size': False}
    
    options.update(kwargs)
    
    for obj in args:

        if options['value']:
            print('value: {}'.format(obj))
        
        if options['type']:
            print('type: {}'.format(type(obj)))
        
        if options['dir']:
            print('dir: {}'.format(dir(obj)))
        
        if options['size']:
            try:
                print('size: {}'.format(len(obj)))
            except TypeError:
                print('size: Not available')
        
        if options['line']:
            from inspect import currentframe, getframeinfo
            print('in_code line: {}'.format(getframeinfo(currentframe().f_back).lineno))


def is_simple(num, **kwargs):
    print()
    _time = kwargs.get('time', False)
    if _time:
        import time
        start_time = time.perf_counter_ns()

    try:
        s = all(num % i for i in range(2, num))
    except TypeError as e:
        print("{}\nPlease enter integer".format(e))
        return
    finally:
        if _time:
            end_time = time.perf_counter_ns()
            print("{} ms".format((end_time-start_time)/1000))
    return s


if __name__ == '__main__':
    dprint(10, dir=True, size=True)
    print(is_simple(-21, time=True))
    dict_print(locals().keys(), str='d')
