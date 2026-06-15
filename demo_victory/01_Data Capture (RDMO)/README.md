# Stage 1: Data Capture (RDMO)

## Overview
The Data Capture stage initiates the EDO pipeline by transforming a researcher's input from the Research Data Management Organiser (RDMO) into a structured machine-readable format. This ensures that the technical and administrative parameters defined during the RDM planning phase serve as the root metadata for the subsequent orchestration stages.

## Objective
To convert an RDMO project export into a normalized JSON structure, bridging the gap between human-readable RDM questionnaires and the automated EDO toolchain.

## Workflow
1. **RDMO Export**: The researcher completes the project questionnaire in RDMO and generates an export (e.g., XML/JSON format).
2. **Ingestion**: The capture script parses the RDMO export, extracting key information regarding data types, project goals, and metadata standards.
3. **Staging**: The extracted metadata is transformed and stored in a clean JSON format, ready to be utilized as the base configuration for the RO-Crate and metadata orchestration.

## Technical Requirements
- **Language**: Python 3.x
- **Input Format**: RDMO project export (XML/JSON)
- **Environment**: Ensure the `edo` virtual environment is active.

## Usage
To execute the capture process, process your RDMO export:
```bash
python scripts/capture_rdmo.py --input ./path/to/rdmo_export.json --output ./data/raw/rdmo_metadata.json