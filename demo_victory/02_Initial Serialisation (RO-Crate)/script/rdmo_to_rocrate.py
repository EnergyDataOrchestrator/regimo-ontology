import json


def transform_to_rocrate(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Flatten list of questions into a lookup dictionary
    flat = {item['question']: item['values'] for item in data}

    # Initialize RO-Crate structure
    crate = {
        "@context": "https://w3id.org/ro/crate/1.1/context",
        "@graph": [
            {
                "@id": "./",
                "@type": "Dataset",
                "name": "Metadata Interoperability Project",
                "description": flat.get("What is the main research question of the project?"),
                "startDate": flat.get("When does the project start?"),
                "endDate": flat.get("When does the project end?"),
                "contactPoint": {
                    "@type": "ContactPoint",
                    "name": flat.get(
                        "Who is the long-term contact person who can make decisions about the data? Please enter their name."),
                    "email": flat.get("Please enter the email address of the permanent contact named above.")
                },
                "hasPart": [
                    {
                        "@id": "my_dataset",
                        "@type": "Dataset",
                        "description": flat.get("What kind of data set is it?"),
                        "license": "https://creativecommons.org/publicdomain/zero/1.0/"
                    }
                ]
            }
        ]
    }

    with open(output_path, 'w') as f:
        json.dump(crate, f, indent=4)
    print(f"RO-Crate successfully generated at {output_path}")


if __name__ == "__main__":
    transform_to_rocrate('metadata_analysis_01.json', 'ro-crate-metadata.json')