import datetime
import json


class UnstractToolUtils:
    log_level = 'INFO'
    start_time = None

    def __init__(self, log_level='INFO'):
        self.log_level = log_level
        self.start_time = datetime.datetime.now()

    def elapsed_time(self) -> float:
        return (datetime.datetime.now() - self.start_time).total_seconds()

    def spec(self, spec_file='config/json_schema.json'):
        with open(spec_file, 'r') as f:
            spec = json.load(f)
            compact_json = json.dumps(spec, separators=(',', ':'))
            return compact_json

    def stream_spec(self, spec: str):
        record = {
            'type': 'SPEC',
            'spec': spec,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def properties(self, properties_file='config/properties.json'):
        with open(properties_file, 'r') as f:
            properties = json.load(f)
            compact_json = json.dumps(properties, separators=(',', ':'))
            return compact_json

    def stream_properties(self, properties: str):
        record = {
            'type': 'PROPERTIES',
            'properties': properties,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def icon(self, icon_file='config/icon.svg'):
        with open(icon_file, 'r') as f:
            icon = f.read()
            return icon

    def stream_icon(self, icon: str):
        record = {
            'type': 'ICON',
            'icon': icon,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def stream_log(self, log: str, level: str = 'INFO'):
        levels = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']
        if levels.index(level) < levels.index(self.log_level):
            return
        record = {
            'type': 'LOG',
            'level': level,
            'log': log,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def stream_cost(self, cost: float, cost_units):
        record = {
            'type': 'COST',
            'cost': cost,
            'cost_units': cost_units,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def stream_single_step_message(self, message: str):
        record = {
            'type': 'SINGLE_STEP_MESSAGE',
            'message': message,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def stream_result(self, result: dict):
        record = {
            'type': 'RESULT',
            'result': result,
            'emitted_at': datetime.datetime.now().isoformat()
        }
        print(json.dumps(record))

    def handle_static_command(self, command: str):
        if command == 'SPEC':
            self.stream_spec(self.spec())
        elif command == 'PROPERTIES':
            self.stream_properties(self.properties())
        elif command == 'ICON':
            self.stream_icon(self.icon())
        else:
            raise ValueError(f'Unknown command {command}')
