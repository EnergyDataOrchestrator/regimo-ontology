import json
import yaml
from rocrate.rocrate import ROCrate


def transform_with_rocrate(source_json, mapping_yaml, output_dir):
    # 1. Load source data and mapping configuration
    with open(source_json, 'r') as f:
        source_data = json.load(f)

    with open(mapping_yaml, 'r') as f:
        mapping_config = yaml.safe_load(f)

    # Flatten source for lookup
    flat_source = {item['question']: item['values'] for item in source_data}

    # 2. Initialize RO-Crate
    crate = ROCrate()
    root = crate.root_dataset

    # 3. Apply mapping
    for mapping in mapping_config['mappings']:
        source_field = mapping['source_field']
        target_slot = mapping['target_slot']

        # Match source data based on partial string matching
        val = next((flat_source[k] for k in flat_source if source_field in k), None)

        if val:
            # Map using standard RO-Crate/Schema.org properties
            clean_slot = target_slot.replace("schema:", "")
            # Update the root dataset property
            root[clean_slot] = val
            # or we add property to the root dataset
            # root.append_to(clean_slot, val)

    # 4. Save the crate
    crate.write_zip(output_dir + ".zip")
    crate.write(output_dir)
    print(f"RO-Crate written to {output_dir}")


if __name__ == "__main__":
    transform_with_rocrate('metadata_analysis_01_2.json', 'schema/mapping_RDMO_maDMP.yaml', 'output_crate')