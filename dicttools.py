def pluck_one(data, keys_path, sep='.',  default=KeyError, **rest):
    keys_path = keys_path.split(sep)
    print(f"keys_path= {keys_path}")
    value = data
    print(f"value={value}")
    for key in keys_path:
        print(f"\nkey={key}")
        try:
            value = value[key]
            print(f"\nvalue={value}")
        except KeyError as e:
            if default == KeyError:
                raise KeyError(key)
            else:
                return default
    return value


def pluck(data, *keys_paths, sep='.',  default=KeyError):
    if len(keys_paths) == 1:
        return pluck_one(data, keys_paths[0], sep, default)
    else:
        value = pluck_one(data, keys_paths[0], sep, default)
        values = [value]
        for keys_path in keys_paths[1:]:
            values.append(pluck_one(data, keys_path, sep, default))
        return tuple(values)

