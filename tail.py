import collections


def tail(secuencia, cantidad):
    #secuencia = list(secuencia)
    if cantidad > 0:
        d1 = collections.deque(maxlen=cantidad)
        for element in secuencia:
            d1.append(element)
            print(f"element={element}")
        '''
        print(f"secuencia={secuencia}")
        reversed_iterable = secuencia[::-1]
        print(f"reversed= {reversed_iterable}")
        reversed_sol = reversed_iterable[:cantidad]
        print(f"reversed_sol= {reversed_sol}")
        sol= reversed_sol[::-1]
        print(f"sol= {sol}")
        '''
        print(f"d1={d1}")
        return list(d1)

    else:
        return []