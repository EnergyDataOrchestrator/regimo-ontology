import json
import os

def lift_schema(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Dictionary to hold new global definitions
    if '$defs' not in data:
        data['$defs'] = {}

    def lift_nested_objects(obj, path=""):
        if isinstance(obj, dict):
            for key, value in list(obj.items()):
                # If we find a nested 'type: object' with properties
                if isinstance(value, dict) and value.get('type') == 'object' and 'properties' in value:
                    # Create a name for the new definition
                    new_name = value.get('title', key.capitalize())
                    # Lift the object into $defs
                    data['$defs'][new_name] = value
                    # Replace the inline object with a $ref to the new definition
                    obj[key] = {"$ref": f"#/$defs/{new_name}"}
                else:
                    lift_nested_objects(value, path + "/" + key)
        elif isinstance(obj, list):
            for item in obj:
                lift_nested_objects(item, path)

    lift_nested_objects(data)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

script_dir = os.path.dirname(os.path.abspath(__file__))
lift_schema(
    os.path.join(script_dir, '..', 'schema', 'maDMP-schema-normalized.json'),
    os.path.join(script_dir, '..', 'schema', 'maDMP-schema-lifted.json')
)