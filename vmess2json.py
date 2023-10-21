import json
import os
import base64
from datetime import datetime

# Initialize variables
address = None
host = None
server_name = None

# Read values from a text file
with open('config.txt', 'r') as file:
    for line in file:
        # Split each line into key and value
        key, value = line.strip().split(' = ')
        if key == "address":
            address = value
        elif key == "host":
            host = value
        elif key == "server_name":
            server_name = value

# Check if all values have been successfully read
if address is not None and host is not None and server_name is not None:
    print("Address:", address)
    print("Host:", host)
    print("Server Name:", server_name)
else:
    print("Not all values were found in the text file.")


# Load the original JSON template
with open('vmess_config.json', 'r') as template_file:
    original_config = json.load(template_file)

# Define the input and output text files
input_file_path = 'vmess_uris.txt'
# output_file_path = '/updated/updated_vmess_uris2json.txt'

# Create a folder with today's date as the name to store the output file
output_folder = datetime.now().strftime('%d-%m-%Y')
os.makedirs(output_folder, exist_ok=True)
# Specify the output file path within the new folder
output_file_path = os.path.join(output_folder, 'updated_vmess_uris2json.txt')


# Read vmess:// URIs from the input file and update the JSON
with open(input_file_path, 'r') as input_file:
    vmess_uris = input_file.readlines()

updated_configs = []

for vmess_uri in vmess_uris:
    # Decode the base64 part of the vmess URI
    data_part = vmess_uri.split('://')[1]
    decoded_data = base64.urlsafe_b64decode(data_part + '===').decode('utf-8')
    vmess_config = json.loads(decoded_data)
    # print(vmess_config)
    # Extract the ID from the vmess config
    id_value = vmess_config['id']
    name_value = vmess_config['ps']


    # Replace the fields with dynamic values
    original_config['remarks'] = name_value
    original_config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'] = id_value
    original_config['outbounds'][0]['settings']['vnext'][0]['address'] = address
    original_config['outbounds'][0]['streamSettings']['wsSettings']['headers']['Host'] = host
    original_config['outbounds'][0]['streamSettings']['tlsSettings']['serverName'] = server_name



    # Append the generated JSON to the list
    updated_configs.append(original_config)

# Write the updated JSON configurations to the output text file
with open(output_file_path, 'w') as output_file:
    for updated_config in updated_configs:
        output_file.write(json.dumps(updated_config, indent=4))
        output_file.write('\n\n ====================================================================================================== \n\n ')

print("Updated JSON configurations have been written to", output_file_path)
