import requests


def test_huggingface_token(api_token):
    # Define the endpoint to access Hugging Face API
    api_url = "https://huggingface.co/api/whoami-v2"  # Endpoint to check user authentication status
    
    # Set the authorization header with the provided token
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    
    try:
        # Make a GET request to check the token
        response = requests.get(api_url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Token is valid. User information:")
            print(response.json())
        elif response.status_code == 401:
            print("Token is invalid or unauthorized. Please check the token.")
        else:
            print(f"Unexpected response. Status code: {response.status_code}, Response: {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Replace 'your_huggingface_api_token' with your actual API token
api_token = "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"

# Test the token
test_huggingface_token(api_token)
