import json
import os
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


def resolve_schema():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, '..', 'schema', 'aa_maDMP-schema-1.2.json')
    output_path = os.path.join(script_dir, '..', 'schema', 'ab_maDMP-schema-resolved.json')

    with open(input_path, 'r') as f:
        schema_data = json.load(f)

    # Use the $id from the schema if available, otherwise use a local base
    base_uri = schema_data.get("$id", "http://ma-dmp.org/schema")

    # 1. Create the resource
    resource = Resource.from_contents(schema_data, default_specification=DRAFT202012)

    # 2. Bind the resource to the base_uri in the registry
    registry = Registry().with_resource(base_uri, resource)

    def inline_refs(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref_path = obj["$ref"]

                # Resolve the pointer relative to the base_uri
                # If ref starts with #, it is a pointer within the base_uri
                resolved_uri = base_uri + ref_path if ref_path.startswith("#") else ref_path

                try:
                    # Lookup the definition and recurse
                    resolved = registry.resolver().lookup(resolved_uri).contents
                    return inline_refs(resolved)
                except Exception as e:
                    print(f"Warning: Could not resolve {ref_path}")
                    return obj
            return {k: inline_refs(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [inline_refs(i) for i in obj]
        return obj

    # Run the resolution
    resolved_data = inline_refs(schema_data)

    with open(output_path, 'w') as f:
        json.dump(resolved_data, f, indent=2)

    print(f"Inlining complete: {output_path} created.")


if __name__ == "__main__":
    resolve_schema()