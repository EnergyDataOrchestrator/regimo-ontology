import json
import os

def normalize_schema(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    slots_to_fix = ['contact_id', 'contributor_id', 'creator_id', 'metadata_standard_id']

    def extract_array_items(one_of_list):
        # Look for the block that defines the array
        for item in one_of_list:
            if item.get("type") == "array":
                return item.get("items")
        return None

    def recursive_update(obj):
        if isinstance(obj, dict):
            for key, value in list(obj.items()):
                if key in slots_to_fix and isinstance(value, dict) and 'oneOf' in value:
                    items_def = extract_array_items(value['oneOf'])
                    if items_def:
                        obj[key] = {
                            "type": "array",
                            "items": items_def,
                            "minItems": 0
                        }
                else:
                    recursive_update(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_update(item)

    recursive_update(data)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, '..', 'schema', 'maDMP-schema-resolved.json')
output_path = os.path.join(script_dir, '..', 'schema', 'maDMP-schema-normalized.json')

normalize_schema(input_path, output_path)
print(f"Normalization applied successfully to {output_path}")