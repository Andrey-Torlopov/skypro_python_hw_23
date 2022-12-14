from dataclasses import dataclass
from helpers import read_file_generator, filter_query, map_query, sort_query, limit_query, unique_query


@dataclass(slots=False)
class Command:
    name: str
    value: str


class CommandEnginge:
    def __init__(self, params: dict[str, str]):
        params_value = params.get('queries')
        if params_value is None:
            raise Exception("Can't parse params!")

        self._params = params_value
        self.commands = []

        result = self._prepeare_commands()
        if not result:
            raise Exception("Can't parse params!")

    # Public
    def execute(self):
        data = read_file_generator(f'data/{self.filename}')

        for item in self.commands:
            if item.name == 'filter':
                data = filter_query(item.value, data)
            if item.name == 'map':
                data = map_query(item.value, data)
            if item.name == 'unique':
                data = unique_query(data)
            if item.name == 'sort':
                data = sort_query(item.value, data)
            if item.name == 'limit':
                data = limit_query(item.value, data)
        return data

    # Private

    def _prepeare_commands(self) -> bool:
        self.filename = self._params.get('file_name')

        if self.filename is None:
            return False

        cmd1 = self._params.get('cmd1')
        value1 = self._params.get('value1')

        cmd2 = self._params.get('cmd2')
        value2 = self._params.get('value2')

        if cmd1 and value1:
            self.commands.append(Command(cmd1, value1))

        if cmd2 and value2:
            self.commands.append(Command(cmd2, value2))

        return len(self.commands) > 0
