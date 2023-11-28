import requests
import json

url = 'https://api.deepinfra.com/v1/inference/meta-llama/Llama-2-70b-chat-hf'
data = {'input': 'Current Employer: Tutti Fruity Corporation as Fruit Picker for 1 year, Previous Employer: Del Monte Corporation as Fruit Sorter for 3 years, Achievements and Awards: Best Worker 2022 at Del Monte Corporation, Skills: hardworking, can speak english, fast learning and honest. With my details create cover letter for Farm Supervisor at Farmy Canada.'}
headers = {'Authorization': f'Bearer HTj80cPBu4Qaiw80oIUZAs6J9Nzg73XK', 'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())