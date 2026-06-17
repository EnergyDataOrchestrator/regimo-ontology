# RDA maDMP Common Standard: Transformation & Serialisation Repository

## Overview
This folder contains the master schema definitions and the transformation pipeline used to convert the **RDA maDMP Common Standard (v1.2)** from its native JSON Schema format into various semantic and machine-actionable serialisations.

## Directory Structure
* `maDMP-schema-1.2.json`: The authoritative JSON Schema source for the maDMP standard.
* `maDMP-model.yaml`: The normalized, LinkML-based intermediate model, generated to resolve `$ref` dependencies and provide a unified typing system.
* `maDMP-model-flattened.yaml`: The resolved version of the model, with all external references inlined for easier graph construction.
* `ontology/`: Contains the Turtle (`.ttl`) and OWL serialisations derived from the model for use in triple stores.
* `docs/`: Visualization assets, including Mermaid/PlantUML diagrams of the schema structure.

## Transformation Workflow
To maintain interoperability between your local RDMO instance and the global RDA standard, use the following procedure:

1.  **Resolution**: Run `python resolve_schema.py` to generate `maDMP-model-flattened.yaml` from the source model.
2.  **RDF Generation**: Use the resolved model to generate RDF triples, ensuring compliance with your KIT-specific ontology mapping:
    ```bash
    gen-rdf --model maDMP-model-flattened.yaml instance.json > dmp-graph.ttl
    ```
3.  **Visualization**: Update class diagrams automatically:
    ```bash
    gen-mermaid-class-diagram maDMP-model-flattened.yaml > docs/schema.mmd
    ```

## Mapping Strategy
The mapping between your internal RDMO attributes (e.g., `pigeon_instruments`) and the maDMP standard is documented in the central mapping matrix. All domain-specific attributes follow the `https://kit.edu/terms/` URI namespace to ensure global identifier uniqueness.

---
*Maintained by: Research Fellow, Karlsruhe Institute of Technology*