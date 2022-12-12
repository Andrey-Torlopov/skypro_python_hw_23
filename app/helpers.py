def read_file_generator(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip('\n')


def filter_query(param: str, data) -> list[str]:
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data) -> list[str]:
    try:
        col = int(param)
    except ValueError:
        return []
    try:
        return list(map(lambda row: row.split(' ')[col], data))
    except IndexError:
        return []


def unique_query(data: list[str], *args, **kwargs) -> list[str]:
    return list(set(data))


def sort_query(param: str, data) -> list[str]:
    if param == "asc":
        return sorted(data)
    elif param == "desc":
        return sorted(data, reverse=True)
    else:
        return data


def limit_query(param: str, data) -> list[str]:
    try:
        limit = int(param)
    except ValueError:
        return data

    return data[:limit]
