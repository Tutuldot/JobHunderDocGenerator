import requests
import json



url = 'https://api.deepinfra.com/v1/inference/meta-llama/Llama-2-70b-chat-hf'
headers = {
    'Authorization': f'Bearer HTj80cPBu4Qaiw80oIUZAs6J9Nzg73XK',
    'Content-Type': 'application/json'
}
data = {
    'input': 'Current Employer: Sun Crest Fruits for 1 year, Previous Employer: Del Monte Coporation as Fruit Sorter for 6 years, Skills: Efficient interpersonal skills, Hardworking,Flexibility, Reliability, Team player . please generate a cover letter for senior data analyst at ABC Corporation.'
}, 

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())