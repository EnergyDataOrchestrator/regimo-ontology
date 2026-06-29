import json
from linkml_runtime.utils.schema_builder import SchemaBuilder
from linkml_runtime.dumpers import yaml_dumper


def build_model(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Initialize a clean LinkML SchemaBuilder
    sb = SchemaBuilder(name="ma-dmp-model")

    # Map your top-level properties to LinkML Classes
    # (Simplified example: focus on the 'dmp' root)
    if 'properties' in data and 'dmp' in data['properties']:
        dmp_props = data['properties']['dmp'].get('properties', {})
        sb.add_class("DMP", slots=list(dmp_props.keys()))

        # Add slots for each property
        for slot_name, slot_info in dmp_props.items():
            sb.add_slot(slot_name, range="string")  # Adjust range as needed

    # Write the YAML
    with open(output_path, 'w') as f:
        f.write(yaml_dumper.dumps(sb.schema))


build_model('schema/maDMP-schema-clean.json', 'schema/maDMP-model.yaml')