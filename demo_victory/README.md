# Workflow Overview: demo_victory

The demo_victory demonstration serves as a practical implementation of the Energy Data Orchestrator.
It illustrates a manual, end-to-end workflow designed to bridge the gap between initial research data input and the
publication of formal metadata records.

This workflow ensures that research data originating from the Research Data Management Organiser (RDMO) is
structured, validated, and ultimately formatted for compliance with the Open Energy Platform (OEP).

The Process Lifecycle
The workflow consists of four primary stages, moving from unstructured user input to a standardized,
machine-readable metadata format:

## Data Capture (RDMO):

The user interacts with the Research Data Management Organiser.

Completion of the "Brief questionnaire" gathers the necessary context, provenance, and technical parameters
required for the dataset.

## Initial Serialization (RO-Crate):

The questionnaire output is transformed into an RO-Crate (Research Object Crate).

This provides a standardized, interoperable packaging format for the research data and its associated metadata.

## Refinement (NovaCrate):

The RO-Crate is imported into NovaCrate for manual editing or enrichment.

This stage allows for the correction of metadata, the addition of missing identifiers, or the refinement of
descriptions to ensure high data quality before publication.

## Final Transformation (OEP Integration):

The validated RO-Crate is transformed into a specific metadata schema required by the Open Energy Platform.

The final output is a metadata record ready for submission, ensuring seamless integration into the OEP’s data ecosystem.

## Key Objectives
**Interoperability:** Utilizing RO-Crate ensures that the data package remains machine-readable across different research
infrastructures.

**Standardization:** By forcing the transition through a structured workflow, the quality of metadata contributed to the
Open Energy Platform is significantly improved.

**Traceability:** The workflow preserves the link between the initial RDMO questionnaire and the final publication,
facilitating better research transparency.

| Stage | Tool | Function |
| :--- | :--- | :--- |
| **Input** | RDMO | Structured data collection via questionnaire. |
| **Packaging** | RO-Crate | Standardized container for research objects. |
| **Editing** | NovaCrate | Interactive refinement of the metadata package. |
| **Output** | OEP | Final metadata schema conversion for publication. |