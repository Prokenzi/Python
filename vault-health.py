import json
import requests

# Send a GET request to Vault healthcheck endpoint
response = requests.get('https://sa-vault-itg.its.hpecorp.net/v1/sys/health')

# Load the JSON response into a Python dictionary
healthcheck_data = json.loads(response.text)

# Access the keys and values of the healthcheck data
is_initialized = healthcheck_data['initialized']
is_sealed = healthcheck_data['sealed']
is_standby = healthcheck_data['standby']

# Print the healthcheck data
if is_initialized and not is_sealed and not is_standby:
    print("Vault is healthy!")
else:
    print("Vault is not healthy.")