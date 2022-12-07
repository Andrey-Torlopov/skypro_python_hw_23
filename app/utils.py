'''
filter, map, unique, sort, limit
'''

def read_file(filepath: str) -> list[str]:
    res = []
    try:
        with open(filepath,'r', encoding='utf-8') as file:
            for row in file:
                res.append(row.strip('\n'))
    except FileNotFoundError:
        return []
    return res

def filter_query(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda row: param in row, data))

def map_query(param: str, data: list[str]) -> list[str]:
    try:
        col = int(param)
    except ValueError:
        return []    
    try:
        return list(map(lambda row: row.split(' ')[col], data))
    except IndexError:
        return []

def unique_query(data: list[str], *args, **kwargs) -> list[str]:
    result = []
    for row in data:
        if row not in result:
            result.append(row)
    return result

def sort_query(param: str, data: list[str]) -> list[str]:
    if param == "asc":
        return sorted(data)
    elif param == "desc":
        return sorted(data, reverse=True)
    else:
        return data

def limit_query(param: str, data: list[str]) -> list[str]:
    try:
        limit = int(param)
    except ValueError:
        return data

    return data[:limit]
