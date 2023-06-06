import requests

# Define the API endpoint for protein search
url = "https://www.ebi.ac.uk/proteins/api/proteins"

# Set the search parameters
params = {
    "offset": 0,
    "size": 10,
    "query": "apple",
}

# Make the API request
response = requests.get(url, params=params)

# Handle the API response
if response.status_code == 200:
    data = response.json()
    # Process the protein data as needed
    print(data)
else:
    print("Error occurred:", response.status_code)
