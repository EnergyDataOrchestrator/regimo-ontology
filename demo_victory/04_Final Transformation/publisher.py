import json
import requests


def publish_metadata(file_path='zenodo_normalized.json'):
    # Replace 'ACCESS_TOKEN' with your actual Sandbox token
    access_token = 'DmvLytsv3alB5iFUo1rzgvfHhYaFOU8h91q361mUzA2bt1FKgwpAsx5K2pZ6'

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    url = "https://sandbox.zenodo.org/api/deposit/depositions"

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Perform the POST request to create the deposition
        r = requests.post(url, json=data, headers=headers)

        # Check if the request was successful
        if r.status_code in [200, 201]:
            print("Deposition created successfully!")
            print(r.json())  # Outputs the deposition ID and link
        else:
            print(f"Failed to create deposition. Status Code: {r.status_code}")
            print(r.text)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not valid JSON.")


if __name__ == "__main__":
    publish_metadata()