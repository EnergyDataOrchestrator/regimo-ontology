from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from rocrate.model import Organization

def create_publication_crate(output_path="./"):
    # 1. Initialize the Crate
    crate = ROCrate()
    crate.name = "Metadata Interoperability Analysis"
    crate.description = "This dataset represents a heterogeneous aggregation of metadata records."

    # 2. Add Contextual Entities (Person & Organization)
    # Adding the Person
    anis = crate.add(Person(crate, "#anis_koubaa", properties={
        "name": "Anis Koubaa",
        "identifier": "https://orcid.org/0000-0001-8552-2008",
        "email": "mohamed.koubaa@kit.ed"
    }))

    # Adding the Organization
    hmc = crate.add(Organization(crate, "#hmc", properties={
        "name": "Helmholtz Metadata Collaboration",
        "url": "https://helmholtz-metadaten.de/",
        "identifier": "https://ror.org/04s3j1c37"
    }))

    # 3. Add Research Project
    project = crate.add_project("#project", properties={
        "name": "Metadata Interoperability Analysis",
        "description": "To which extent are metadata records compatible with the Dublin Core.",
        "startDate": "2026-06-15",
        "funder": hmc
    })

    # 4. Add the Data File (Data Entity)
    # Assuming 'metadata_analysis_01.json' exists locally
    data_file = crate.add_file("metadata_analysis_01.json", properties={
        "name": "Curated collection of heterogeneous research metadata records",
        "description": "A curated collection of heterogeneous research metadata records, harvested via OAI-PMH and normalised to support FAIR-compliant analysis within the EDO toolchain.",
        "encodingFormat": "application/json",
        "creator": anis
    })

    # 5. Link properties to the Root Dataset
    crate.root_dataset.update({
        "creator": anis,
        "maintainer": hmc
    })

    # 6. Save the Crate
    crate.write(output_path)
    print(f"RO-Crate successfully created at {output_path}")

# Run the function
if __name__ == "__main__":
    create_publication_crate()