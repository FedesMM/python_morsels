def with_previous(iterable, *, fillvalue = None):
    lista = []
    first = True
    previo = fillvalue
    for i in iterable:
        yield (i, previo,)
        previo = i


