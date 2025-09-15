import requests

# Define the API endpoint URL
api_url = "https://official-joke-api.appspot.com/random_joke"

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # example response
    # {"type":"general","setup":"Why do chicken coops only have two doors?","punchline":"Because if they had four, they would be chicken sedans","id":48}

    # Print the retrieved data
    print("API Call Successful!")
    print(f"type: {data['type']}")
    print(f"setup: {data['setup']}")
    print(f"punchlin: {data['punchline']}")

except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the API call
    print(f"API Call Failed: {e}")
