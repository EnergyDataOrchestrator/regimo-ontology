from linkml_runtime.utils.schemaview import SchemaView
import yaml
import sys

# Load the schema
sv = SchemaView("maDMP-model.yaml")

# Export the fully resolved (inlined) schema to a new file
with open("maDMP-model-flattened.yaml", "w") as f:
    # sv.all_classes() and sv.all_slots() contain the merged definitions
    yaml.dump(sv.schema, f, sort_keys=False)

print("Schema flattened successfully to maDMP-model-flattened.yaml")