# RDA maDMP Common Standard: Transformation & Serialisation Repository

## Overview
This repository contains the master schema definitions and the automated transformation pipeline used to convert the **RDA maDMP Common Standard (v1.2)** from its native JSON Schema format into unified, machine-actionable LinkML models and semantic RDF serialisations.

## Directory Structure
* `schema/`:
    * `maDMP-schema-1.2.json`: The authoritative JSON Schema source.
    * `maDMP-schema-resolved.json`: Intermediate artifact with all `$ref` pointers inlined.
    * `maDMP-schema-normalized.json`: Cleaned version with ambiguous `oneOf` unions resolved to standard arrays.
    * `maDMP-model.yaml`: The final LinkML-compatible model generated for downstream integration.
* `scripts/`:
    * `resolve_json_schema.py`: Resolves external/internal `$ref` dependencies.
    * `normalize_schema.py`: Automatically patches ambiguous JSON schema slots (`contact_id`, etc.) to standard array types.

## Transformation Workflow
To maintain interoperability between local RDMO instances and the global RDA standard, the build pipeline is automated via `uv`:

1.  **Resolve References**: Inlines all `$ref` pointers.
    ```bash
    uv run scripts/resolve_json_schema.py
    ```
2.  **Normalize**: Patches complex schema branches into predictable types.
    ```bash
    uv run scripts/normalize_schema.py
    ```
3.  **Generate LinkML**: Converts the cleaned JSON schema into the LinkML model.
    ```bash
    PYTHONWARNINGS="ignore" uv run schemauto import-json-schema schema/maDMP-schema-normalized.json > schema/maDMP-model.yaml
    ```



## Mapping & Usage
The generated `maDMP-model.yaml` is designed for direct RDF/OWL serialisation. Domain-specific attributes required for KIT research infrastructure follow the `https://kit.edu/terms/` URI namespace to ensure global identifier uniqueness and schema alignment with existing triple stores.

---
*Maintained by: Research Fellow, Karlsruhe Institute of Technology*