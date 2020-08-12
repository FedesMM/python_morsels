from collections.abc import Hashable


def uniques_only_v_1_0(iterable):
    seen=set()
    new_iterable = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            new_iterable.append(item)
    return new_iterable


def uniques_only_v_2_0(iterable):
    seen=set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


def uniques_only_v_3_0(iterable):
    seen=[]
    for item in iterable:
        if item not in seen:
            seen.append(item)
            yield item


def uniques_only(iterable):
    seen_hashable = set()
    seen_unhashable = []
    for item in iterable:
        if isinstance(item, Hashable):
            if item not in seen_hashable:
                seen_hashable.add(item)
                yield item
        else:
            if item not in seen_unhashable:
                seen_unhashable.append(item)
                yield item
