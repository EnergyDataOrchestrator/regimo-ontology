import json

def normalize_rocrate_to_zenodo(input_file, output_file):
    with open(input_file, 'r') as f:
        crate = json.load(f)

    # Locate the Root Dataset and Creator Person entity
    graph = crate.get("@graph", [])
    root = next((e for e in graph if e.get("@id") == "./"), {})
    creator_id = root.get("creator", {}).get("@id")
    person = next((e for e in graph if e.get("@id") == creator_id), {})

    # Construct Zenodo-compatible JSON payload
    payload = {
        "metadata": {
            "title": root.get("name"),
            "description": root.get("description"),
            "upload_type": "dataset",
            "creators": [{
                "name": person.get("name"),
                "orcid": person.get("identifier", "").replace("https://orcid.org/", "")
            }],
            "keywords": ["Metadata Interoperability", "FAIR", "RO-Crate"]
        }
    }

    with open(output_file, 'w') as f:
        json.dump(payload, f, indent=4)
    print(f"Record generated: {output_file}")

if __name__ == "__main__":
    normalize_rocrate_to_zenodo('ro-crate-metadata.json', 'zenodo_normalized.json')