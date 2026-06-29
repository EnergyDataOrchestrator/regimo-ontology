import json
import os


def sanitize(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Keywords that break LinkML's strict parser
    forbidden = ['$schema', '$id']

    def clean(obj):
        if isinstance(obj, dict):
            return {k: clean(v) for k, v in obj.items() if k not in forbidden}
        elif isinstance(obj, list):
            return [clean(i) for i in obj]
        return obj

    sanitized = clean(data)
    with open(output_path, 'w') as f:
        json.dump(sanitized, f, indent=2)


script_dir = os.path.dirname(os.path.abspath(__file__))
sanitize(
    os.path.join(script_dir, '..', 'schema', 'maDMP-schema-lifted.json'),
    os.path.join(script_dir, '..', 'schema', 'maDMP-schema-clean.json')
)