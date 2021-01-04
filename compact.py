def compact(sequence):
    print(sequence)

    iterable, rest = next(sequence)
    print(f"iterable={iterable}")
    for element in rest:
        print(f"Compare {iterable[-1]} with {element}: ", end='')
        if iterable[-1] != element:
            print(f"Add -> iterable={iterable}")
            iterable.append(element)
        else:
            print(f"Discard-> iterable={iterable}")
    print(iterable)
    return iterable
