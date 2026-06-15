import json


def transform_rdmo_to_config(input_file, output_file):
    """
    Transforms the RDMO export list format into a flat dictionary
    for easy access in metadata orchestration.
    """
    try:
        with open(input_file, 'r') as f:
            rdmo_data = json.load(f)

        # Flatten the list of questions/values into a clean dict
        config = {}
        for entry in rdmo_data:
            # We use the question as a key, sanitizing it to be variable-friendly
            # For specific fields, we map to standardized keys
            key = entry.get("question", "").strip()
            val = entry.get("values", "").strip()

            # Map specific important fields to standard config keys
            if "research question" in key.lower():
                config["project_research_question"] = val
            elif "project start" in key.lower():
                config["start_date"] = val
            elif "project end" in key.lower():
                config["end_date"] = val
            elif "long-term contact person" in key.lower():
                config["contact_person"] = val
            elif "email address of the permanent contact" in key.lower():
                config["contact_email"] = val

            # Store everything else under the raw question key as fallback
            config[key] = val

        # Save the clean configuration
        with open(output_file, 'w') as f:
            json.dump(config, f, indent=4)

        print(f"Successfully transformed RDMO export to: {output_file}")

    except Exception as e:
        print(f"Error during transformation: {e}")


if __name__ == "__main__":
    transform_rdmo_to_config('metadata_analysis_01.json', 'project_config.json')