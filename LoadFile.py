import os
import requests
import json
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID='57531bfd-82b3-4dbd-a75a-bd0212115eb5'
SCOPES=['Files.ReadWrite.All']

access_token = generate_access_token(APP_ID, SCOPES)
 
headers = {
    'Authorization' : 'Bearer ' + access_token['access_token']
}

file_path = 'C:\\Users\\Usuario\\OneDrive\\ProCanDis by Sergio v0.1\\Manual llave criptográfica.pdf'
file_name = os.path.basename(file_path)

with open(file_path, 'rb') as upload:
    media_content = upload.read()

#upload file
response = requests.put(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
    headers=headers,
    data=media_content
)
val = str(response.json())
print(val)  
