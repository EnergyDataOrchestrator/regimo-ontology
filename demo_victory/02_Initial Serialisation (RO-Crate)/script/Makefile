# Define variables for file paths
JSON_SCHEMA = schema/maDMP-schema-1.2.json
LINKML_SCHEMA = maDMP-schema.yaml

# Target to generate the LinkML schema
$(LINKML_SCHEMA): $(JSON_SCHEMA)
	@echo "Generating LinkML schema from $(JSON_SCHEMA)..."
	schema-automator import-json-schema $(JSON_SCHEMA) -o $(LINKML_SCHEMA)

# Helper target to clean up generated files
clean:
	rm -f $(LINKML_SCHEMA)

# Default target
all: $(LINKML_SCHEMA)